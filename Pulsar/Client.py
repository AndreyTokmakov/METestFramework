import pulsar

PULSAR_HOST: str = 'pulsar://localhost:6650'
PULSAR_API: str = "http://localhost:8080/admin/v2/"

if __name__ == '__main__':
    client: pulsar.Client = pulsar.Client(PULSAR_HOST)

    client.get_topic_partitions()

    client.close()
