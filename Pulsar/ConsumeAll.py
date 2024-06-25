import random
import signal
import string
import pulsar
import requests
import multiprocessing.queues

from dataclasses import dataclass
from http import HTTPStatus
from multiprocessing import Process, Queue, Event
from queue import Empty
from typing import Any, List, Tuple
from _pulsar import Timeout
from requests import Response

PULSAR_HOST: str = 'pulsar://localhost:6650'


@dataclass
class Params(object):
    tenant_name: str
    namespace: str
    topic: str


def generate_random_string(length: int = 32):
    letters = string.ascii_letters + string.digits + string.hexdigits
    return ''.join(random.choice(letters) for i in range(length))


class PulsarAdmin(object):
    PULSAR_API: str = "http://localhost:8080/admin/v2/"

    @staticmethod
    def get_tenants() -> List[str]:
        response = requests.get(PulsarAdmin.PULSAR_API + "tenants")
        if HTTPStatus.OK == response.status_code:
            return list(response.json())
        else:
            return []

    @staticmethod
    def namespaces_by_tenant(tenant: str):
        response = requests.get(PulsarAdmin.PULSAR_API + f"namespaces/{tenant}")
        if HTTPStatus.OK == response.status_code:
            return list(response.json())
        else:
            return []

    @staticmethod
    def enum_all_persistent_topics():
        persistent_topics: List[str] = []
        tenants_list: List[str] = PulsarAdmin.get_tenants()
        for tenant in tenants_list:
            namespaces_list: List[str] = PulsarAdmin.namespaces_by_tenant(tenant)
            for namespace in namespaces_list:
                response: Response = requests.get(PulsarAdmin.PULSAR_API + f"persistent/{namespace}")

                topics: List[str] = list(response.json())
                if topics:
                    persistent_topics.extend(topics)

        topics: List[Params] = []
        for full_name in persistent_topics:
            parts: List[str] = full_name.replace('persistent://', '').split('/')
            if 3 == len(parts):
                topics.append(Params(tenant_name=parts[0], namespace=parts[1], topic=parts[2]))

        return topics


def consume_from_topic(queue: multiprocessing.Queue,
                       event: Event,
                       params: Params) -> None:
    while True:
        topic_name: str = f'persistent://{params.tenant_name}/{params.namespace}/{params.topic}'
        subscription_name: str = 'subscription_' + generate_random_string(5)

        client: pulsar.Client = pulsar.Client(PULSAR_HOST)
        consumer: pulsar.Consumer = client.subscribe(topic=topic_name,
                                                     subscription_name=subscription_name)
        print('Start listening messages on: ' + topic_name)
        while True:
            try:
                msg: pulsar.Message = consumer.receive(timeout_millis=250)
                queue.put((msg.topic_name(), msg.data()))
                consumer.acknowledge(msg)
            except Timeout as timeout:
                if event.is_set():
                    return
                continue
            except Exception as exc:
                print(exc)
                continue

        client.close()


def printer(queue: multiprocessing.Queue, event: Event):
    while True:
        try:
            item: Tuple[str, str] = queue.get(timeout=0.25)
            print('==' * 30 + item[0] + "==" * 30 + "\n")
            print(item[1])
            print()
        except Empty:
            if event.is_set():
                break
            continue


# TODO: Check if new Topics has been created + subscribe

if __name__ == '__main__':
    all_existing_topics: List[Params] = PulsarAdmin.enum_all_persistent_topics()
    message_queue: Queue = Queue()
    stop_event: Event = Event()

    def signal_handler(sig, frame):
        print('Stopping consumers.....')
        stop_event.set()

    signal.signal(signal.SIGINT, signal_handler)

    print_process: Process = Process(target=printer, args=(message_queue, stop_event,))
    print_process.start()

    consumer_proc_list: List[Process] = []
    for consumer_params in all_existing_topics:
        consumer_proc_list.append(Process(target=consume_from_topic, args=(message_queue, stop_event, consumer_params,)))
        consumer_proc_list[-1].start()

    print_process.join()
    for proc in consumer_proc_list:
        proc.join()
