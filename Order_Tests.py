import json
import pulsar
from typing import Dict

from Modules.Order import Order, OrderStopCondition, OrderType, OrderSide, OrderActionType, OrderTimeCondition, \
    SelfTradeProtectionType, TriggerType, OrderMatchedType, OrderStatusType

if __name__ == '__main__':

    '''
    order.triggerPrice
    timestamp
    order.orderCreated,
    order.source
    order.tag
    '''

    order: Order = Order()

    order.account_id = 1234567
    order.parent_account_id = 2
    order.market_id = 111222333444
    order.price = 100
    order.amount = 25
    order.quantity = 50
    order.display_quantity = 51
    order.remain_quantity = 31
    order.remain_amount = 25
    order.upper_bound = 10
    order.lower_bound = 22

    order.side = OrderSide.BUY
    order.type = OrderType.TAKE_PROFIT_MARKET
    order.stop_condition = OrderStopCondition.GREATER_EQUAL
    order.action = OrderActionType.CANCEL
    order.time_condition = OrderTimeCondition.MAKER_ONLY_REPRICE
    order.trigger_type = TriggerType.MARK_PRICE
    order.self_trade_protection = SelfTradeProtectionType.STP_BOTH
    order.status = OrderStatusType.CANCELED_BY_MARKET_ORDER_NOTHING_MATCH
    order.matched_type = OrderMatchedType.TAKER

    order.is_triggered = True
    order.timestamp = 1233

    '''
    print(order.time_condition)
    print(order.action)
    print(order.stop_condition)
    print(order.type)
    print(order.side)
    print(order.trigger_type)
    print(order.self_trade_protection)
    print(order.status)
    print(order.matched_type)
    print(order.is_triggered)
    '''

    print('\n' + '==' * 50 + '\n\n' + str(order))
    print('\n' + '==' * 50 + '\n\n' + order.asJson())
    print('\n' + '==' * 50 + '\n\n' + json.dumps(order, indent=4))
