import json
import pulsar
from typing import Dict

from Modules.Order import Order, OrderStopCondition, OrderType, OrderSide, OrderActionType, OrderTimeCondition, \
    SelfTradeProtectionType, TriggerType, OrderMatchedType, OrderStatusType


class Commands:

    @staticmethod
    def send_test_command(client: pulsar.Client):
        producer: pulsar.Producer = client.create_producer('persistent://OPNX-V1/PRETRADE-ME/CMD-IN')
        message: Dict = {
            "action": "TEST_TEST_TEST",
            "data": 5
        }

        payload: str = json.dumps(message)
        producer.send(payload.encode('utf-8'))

    @staticmethod
    def send_set_open_order_limits(client: pulsar.Client):
        producer: pulsar.Producer = client.create_producer('persistent://OPNX-V1/PRETRADE-ME/CMD-IN')
        message: Dict = {
            "action": "openOrdersLimit",
            "data": 5
        }

        payload: str = json.dumps(message)
        producer.send(payload.encode('utf-8'))

    @staticmethod
    def send_markets_command(client: pulsar.Client):
        market_id: int = 10000000001
        producer: pulsar.Producer = client.create_producer('persistent://OPNX-V1/PRETRADE-ME/CMD-IN')
        message: Dict = {
            "action": "markets",
            "pair": "BTC/USDT",
            "data": [
                {"marketId": market_id, "marketCode": "BTC-USD"}
            ]
        }

        payload: str = json.dumps(message)
        producer.send(payload.encode('utf-8'))

    @staticmethod
    def send_add_markets_command(client: pulsar.Client):
        market_id: int = 10000000001
        producer: pulsar.Producer = client.create_producer('persistent://OPNX-V1/PRETRADE-ME/CMD-IN')
        message: Dict = {
            "action": "addMarkets",
            "pair": "BTC/USDT",
            "data": [
                {"marketId": market_id, "marketCode": "BTC-USD"}
            ]
        }

        payload: str = json.dumps(message)
        producer.send(payload.encode('utf-8'))


class Orders:

    @staticmethod
    def publish_order(producer: pulsar.Producer,
                      order: Order) -> None:
        payload: bytes = json.dumps(order).encode('utf-8')
        producer.send(payload)

    @staticmethod
    def send_stop_recovery_order(client: pulsar.Client):
        market_id: int = 10000000001
        producer: pulsar.Producer = client.create_producer(f'persistent://OPNX-V1/PRETRADE-ME/ORDER-IN-{market_id}')

        order: Order = Order()

        order.order_id = get_next_order_id()
        order.account_id = 1234567
        order.parent_account_id = 2
        order.market_id = market_id
        order.action = OrderActionType.RECOVERY_END

        Orders.publish_order(producer, order)

    @staticmethod
    def send_test_order(client: pulsar.Client):
        market_id: int = 10000000001
        producer: pulsar.Producer = client.create_producer(f'persistent://OPNX-V1/PRETRADE-ME/ORDER-IN-{market_id}')

        order: Order = Order()

        order.order_id = get_next_order_id()
        order.account_id = 1234567
        order.parent_account_id = 2
        order.market_id = market_id
        order.price = 100
        order.amount = 25
        # order.quantity = 50
        order.display_quantity = 11
        order.remain_quantity = 31
        order.remain_amount = 25
        order.upper_bound = 10
        order.lower_bound = 22

        order.side = OrderSide.SELL
        order.type = OrderType.TAKE_PROFIT_MARKET
        order.stop_condition = OrderStopCondition.GREATER_EQUAL
        order.action = OrderActionType.NEW
        order.time_condition = OrderTimeCondition.MAKER_ONLY_REPRICE
        order.trigger_type = TriggerType.MARK_PRICE
        order.self_trade_protection = SelfTradeProtectionType.STP_BOTH
        order.status = OrderStatusType.OPEN
        order.matched_type = OrderMatchedType.TAKER

        order.is_triggered = True
        order.timestamp = 1233

        Orders.publish_order(producer, order)


#------------------------------------------------------------------------------

def send_snapshot_cmd(client: pulsar.Client):
    market_id: int = 10000000001
    producer: pulsar.Producer = client.create_producer(f'non-persistent://OPNX-V1/ME-WS/MD-SNAPSHOT-{market_id}')
    message: Dict = {
        "action": "markets",
        "pair": "BTC/USDT",
        "data": [
            {"marketId": 2001000000000, "marketCode": "BTC-USD"}
        ]
    }

    payload: str = json.dumps(message)
    producer.send(payload.encode('utf-8'))


def send_to_test_topic(client: pulsar.Client):
    producer: pulsar.Producer = client.create_producer('persistent://public/default/my-topic')
    # producer: pulsar.Producer = client.create_producer('persistent://OPNX-V1/PRETRADE-ME/CMD-IN')
    message: Dict = {
        "action": "markets",
        "payload": "bla_bla_bla"
    }

    payload: str = json.dumps(message)
    producer.send(payload.encode('utf-8'))


def send_order_stop_recovery(client: pulsar.Client):
    market_id: int = 10000000001
    producer: pulsar.Producer = client.create_producer(f'persistent://OPNX-V1/PRETRADE-ME/ORDER-IN-{market_id}')
    message: Dict = {
        "action": "markets",
        "extra": "RECOVERY_END",
        "payload": "SOME DATA"
    }

    payload: str = json.dumps(message)
    producer.send(payload.encode('utf-8'))


# TODO: Create a Order Builder
def send_new_order_1(client: pulsar.Client):
    market_id: int = 10000000001
    producer: pulsar.Producer = client.create_producer(f'persistent://OPNX-V1/PRETRADE-ME/ORDER-IN-{market_id}')

    order: Order = Order()

    order.order_id = 100000006
    order.account_id = 1234567
    order.parent_account_id = 2
    order.market_id = market_id
    order.price = 100
    order.amount = 25
    # order.quantity = 50
    order.display_quantity = 11
    order.remain_quantity = 31
    order.remain_amount = 25
    order.upper_bound = 10
    order.lower_bound = 22

    order.side = OrderSide.BUY
    order.type = OrderType.TAKE_PROFIT_MARKET
    order.stop_condition = OrderStopCondition.GREATER_EQUAL
    order.action = OrderActionType.NEW
    order.time_condition = OrderTimeCondition.MAKER_ONLY_REPRICE
    order.trigger_type = TriggerType.MARK_PRICE
    order.self_trade_protection = SelfTradeProtectionType.STP_BOTH
    order.status = OrderStatusType.OPEN
    order.matched_type = OrderMatchedType.TAKER

    order.is_triggered = True
    order.timestamp = 1233

    payload: bytes = json.dumps(order).encode('utf-8')
    producer.send(payload)


def get_next_order_id() -> int:
    with open(file='/tmp/order_id.txt', mode='r+') as file:
        value: int = int(file.read())
        file.seek(0)
        value += 1
        file.write(str(value))

    return value


# TODO: Add ALL TOPICS consumer

if __name__ == '__main__':
    pulsar_client: pulsar.Client = pulsar.Client('pulsar://localhost:6650')

    # send_order_stop_recovery(pulsar_client)                       # <---- Create Framework
    # send_new_order_1(pulsar_client)

    # send_snapshot_cmd(pulsar_client)
    # send_to_test_topic(pulsar_client)

    # Commands.send_markets_command(pulsar_client)                  # <---- Create Framework
    # Commands.send_add_markets_command(pulsar_client)
    # Commands.send_set_open_order_limits(pulsar_client)
    # Commands.send_test_command(pulsar_client)

    # Orders.send_stop_recovery_order(pulsar_client)
    Orders.send_test_order(pulsar_client)

    pulsar_client.close()
