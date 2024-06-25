import pulsar

PULSAR_HOST: str = 'pulsar://localhost:6650'


def consume_messages(tenant_name: str,
                     namespace: str,
                     topic: str):
    full_topic_name: str = f'persistent://{tenant_name}/{namespace}/{topic}'

    client: pulsar.Client = pulsar.Client(PULSAR_HOST)
    consumer: pulsar.Consumer = client.subscribe(full_topic_name, 'my-subscription')

    while True:
        msg: pulsar.Message = consumer.receive()
        try:
            print(f'--------------------------- {msg.message_id()} ------------------------------')
            print(msg.data())

            # Acknowledge successful processing of the message
            consumer.acknowledge(msg)
        except Exception as exc:
            # Message failed to be processed
            print(exc)
            consumer.negative_acknowledge(msg)

    client.close()


def consume_orders_out():
    market_id: int = 10000000001
    consume_messages('OPNX-V1', 'ME-POSTTRADE', f'ORDER-OUT-{market_id}')


if __name__ == '__main__':
    # consume_messages('OPNX-V1', 'PRETRADE-ME', 'ORDER-IN-111222333444')
    # consume_messages('OPNX-V1', 'ME-POSTTRADE', 'ORDER-OUT-111222333003')

    consume_orders_out()
