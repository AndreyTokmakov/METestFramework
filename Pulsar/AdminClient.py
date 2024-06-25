import json
from http import HTTPStatus

import requests
from typing import Dict, List

from requests import Response

PULSAR_API: str = "http://localhost:8080/admin/v2/"


def bookies_all():
    response = requests.get(PULSAR_API + "bookies/all")
    print(response.json())


def clusters():
    response = requests.get(PULSAR_API + "clusters")
    print(response.json())


def cluster_info(cluster: str):
    response = requests.get(PULSAR_API + f"clusters/{cluster}")
    print(json.dumps(response.json(), indent=4))


def get_brokers():
    response = requests.get(PULSAR_API + "brokers")
    print(response.json())


def get_tenants() -> List[str]:
    response = requests.get(PULSAR_API + "tenants")
    if HTTPStatus.OK == response.status_code:
        return list(response.json())
    else:
        return []


def namespaces_by_tenant(tenant: str):
    response = requests.get(PULSAR_API + f"namespaces/{tenant}")
    if HTTPStatus.OK == response.status_code:
        return list(response.json())
    else:
        return []


def enum_all_namespaces():
    tenants_list: List[str] = get_tenants()
    for tenant in tenants_list:
        namespaces: List[str] = namespaces_by_tenant(tenant)
        print(tenant + '\n\t' + str(namespaces))


def enum_all_persistent_topics():
    tenants_list: List[str] = get_tenants()
    for tenant in tenants_list:
        namespaces_list: List[str] = namespaces_by_tenant(tenant)
        for namespace in namespaces_list:
            response: Response = requests.get(PULSAR_API + f"persistent/{namespace}")

            print(response.json())


if __name__ == '__main__':
    # clusters()
    # cluster_info('standalone')

    # get_brokers()

    # tenants: List[str] = get_tenants()
    # print(tenants)

    # bookies_all()

    # namespaces: List[str] = namespaces_by_tenant('public')
    # print(namespaces)

    # enum_all_namespaces()

    enum_all_persistent_topics()

