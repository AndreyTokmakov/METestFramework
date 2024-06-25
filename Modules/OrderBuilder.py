import typing
import json
from enum import Enum, IntEnum


class OrderSide(IntEnum):
    BUY = 0
    SELL = 1


class OrderType(IntEnum):
    LIMIT = 0x00
    MARKET = 0x01
    STOP_LIMIT = 0x02
    STOP_MARKET = 0x03
    TAKE_PROFIT_LIMIT = 0x04
    TAKE_PROFIT_MARKET = 0x05


class OrderStopCondition(Enum):
    NONE = 0x00
    GREATER_EQUAL = 0x01
    LESS_EQUAL = 0x02


class OrderActionType(Enum):
    NEW = 0x00
    AMEND = 0x01
    CANCEL = 0x02
    RECOVERY = 0x03
    RECOVERY_END = 0x04


class OrderTimeCondition(Enum):
    GTC = 0x00
    IOC = 0x01
    FOK = 0x02
    MAKER_ONLY = 0x03
    MAKER_ONLY_REPRICE = 0x04


class TriggerType(Enum):
    MARK_PRICE = 0
    LAST_PRICE = 1
    TRIGGER_NONE = 2


class SelfTradeProtectionType(Enum):
    STP_NONE = 0
    STP_TAKER = 1
    STP_MAKER = 2
    STP_BOTH = 3


class OrderStatusType(Enum):
    OPEN = 0
    PARTIAL_FILL = 1
    FILLED = 2
    CANCELED_BY_USER = 3
    CANCELED_BY_MARKET_ORDER_NOT_FULL_MATCHED = 4
    CANCELED_BY_MARKET_ORDER_NOTHING_MATCH = 5
    CANCELED_ALL_BY_IOC = 6
    CANCELED_PARTIAL_BY_IOC = 7
    CANCELED_BY_FOK = 8
    CANCELED_BY_MAKER_ONLY = 9
    CANCELED_BY_AMEND = 10
    CANCELED_BY_SELF_TRADE_PROTECTION = 11
    REJECT_CANCEL_ORDER_ID_NOT_FOUND = 12
    REJECT_AMEND_ORDER_ID_NOT_FOUND = 13
    REJECT_DISPLAY_QUANTITY_ZERO = 14
    REJECT_DISPLAY_QUANTITY_LARGER_THAN_QUANTITY = 15
    REJECT_QUANTITY_AND_AMOUNT_ZERO = 16
    REJECT_LIMIT_ORDER_WITH_MARKET_PRICE = 17
    REJECT_MATCHING_ENGINE_RECOVERING = 18
    REJECT_STOP_CONDITION_IS_NONE = 19
    REJECT_STOP_TRIGGER_PRICE_IS_NONE = 20
    REJECT_QUANTITY_AND_AMOUNT_LARGER_ZERO = 21
    REJECT_PRICE_LESS_ZERO = 22
    REJECT_ORDER_QUANTITY_GREATER_THAN_MAX = 22
    REJECT_ORDER_AMOUNT_GREATER_THAN_MAX = 23
    REJECT_MAXIMUM_OPEN_ORDERS_LIMIT_REACHED = 24


class OrderMatchedType(Enum):
    MAKER = 0x00
    TAKER = 0x01


class OrderKeys(str, Enum):
    AccountId = 'aid'
    ParentAccountId = 'paid'
    MarketId = 'mid'
    Price = 'p'
    Quantity = 'q'
    DisplayQuantity = 'dq'
    RemainQuantity = 'rq'
    Amount = 'a'
    RemainAmount = 'ra'
    UpperBound = 'ub'
    LowerBound = 'lb'
    LastMatchPrice = 'mp'
    Leg2Price = 'l2p'
    AveragePrice = 'ap'
    LastMatchQuantity = 'mq'
    OrderId = 'id'
    ClientOrderId = 'cid'
    LastMatchedOrderId = 'lmid'
    LastMatchedOrderId2 = 'lmid2'
    MatchedId = 'mtid'
    SortId = 'sid'
    TriggerPrice = 'tp'
    IsTriggered = 'it'
    TriggerType = 'tt'
    Side = 's'
    Type = 'ty'
    StopCondition = 'stc'
    TimeCondition = 'tc'
    ActionType = 'ac'
    Status = 'st'
    MatchedType = 'mt'
    Timestamp = 't'
    OrderCreated = 'oc'
    Source = 'sc'
    Tag = 'tag'
    SelfTradeProtection = 'stp'
    TotalTradeAmount = 'tta'
    TotalTradeQuantity = 'ttq'

    def __repr__(self) -> str:
        return f'{self.value}'

    def __str__(self) -> str:
        return f'{self.value}'


class Order(typing.Dict):

    @property
    def side(self) -> OrderSide:
        return OrderSide(self[OrderKeys.Side])

    @side.setter
    def side(self, side: OrderSide):
        self[OrderKeys.Side] = side.value

    @property
    def type(self) -> OrderType:
        return OrderType(self[OrderKeys.Type])

    @type.setter
    def type(self, _type: OrderType):
        self[OrderKeys.Type] = _type.value

    @property
    def stop_condition(self) -> OrderStopCondition:
        return OrderStopCondition(self[OrderKeys.StopCondition])

    @stop_condition.setter
    def stop_condition(self, condition: OrderStopCondition):
        self[OrderKeys.StopCondition] = condition.value

    @property
    def action(self) -> OrderActionType:
        return OrderActionType(self[OrderKeys.ActionType])

    @action.setter
    def action(self, condition: OrderActionType):
        self[OrderKeys.ActionType] = condition.value

    @property
    def time_condition(self) -> OrderTimeCondition:
        return OrderTimeCondition(self[OrderKeys.TimeCondition])

    @time_condition.setter
    def time_condition(self, condition: OrderTimeCondition):
        self[OrderKeys.TimeCondition] = condition.value

    @property
    def trigger_type(self) -> TriggerType:
        return TriggerType(self[OrderKeys.TriggerType])

    @trigger_type.setter
    def trigger_type(self, condition: TriggerType):
        self[OrderKeys.TriggerType] = condition.value

    @property
    def self_trade_protection(self) -> SelfTradeProtectionType:
        return SelfTradeProtectionType(self[OrderKeys.SelfTradeProtection])

    @self_trade_protection.setter
    def self_trade_protection(self, condition: SelfTradeProtectionType):
        self[OrderKeys.SelfTradeProtection] = condition.value

    @property
    def status(self) -> OrderStatusType:
        return OrderStatusType(self[OrderKeys.Status])

    @status.setter
    def status(self, condition: OrderStatusType):
        self[OrderKeys.Status] = condition.value

    @property
    def matched_type(self) -> OrderMatchedType:
        return OrderMatchedType(self[OrderKeys.MatchedType])

    @matched_type.setter
    def matched_type(self, condition: OrderMatchedType):
        self[OrderKeys.MatchedType] = condition.value

    @property
    def account_id(self) -> int:
        return self[OrderKeys.AccountId]

    @account_id.setter
    def account_id(self, value: int):
        self[OrderKeys.AccountId] = value

    @property
    def parent_account_id(self) -> int:
        return self[OrderKeys.ParentAccountId]

    @parent_account_id.setter
    def parent_account_id(self, value):
        self[OrderKeys.ParentAccountId] = value

    @property
    def market_id(self) -> int:
        return self[OrderKeys.MarketId]

    @market_id.setter
    def market_id(self, value):
        self[OrderKeys.MarketId] = value

    @property
    def price(self) -> int:
        return self[OrderKeys.Price]

    @price.setter
    def price(self, value):
        self[OrderKeys.Price] = value

    @property
    def quantity(self) -> int:
        return self[OrderKeys.Quantity]

    @quantity.setter
    def quantity(self, value):
        self[OrderKeys.Quantity] = value

    @property
    def display_quantity(self) -> int:
        return self[OrderKeys.DisplayQuantity]

    @display_quantity.setter
    def display_quantity(self, value):
        self[OrderKeys.DisplayQuantity] = value

    @property
    def remain_quantity(self) -> int:
        return self[OrderKeys.RemainQuantity]

    @remain_quantity.setter
    def remain_quantity(self, value):
        self[OrderKeys.RemainQuantity] = value

    @property
    def amount(self) -> int:
        return self[OrderKeys.Amount]

    @amount.setter
    def amount(self, value):
        self[OrderKeys.Amount] = value

    @property
    def remain_amount(self) -> int:
        return self[OrderKeys.RemainAmount]

    @remain_amount.setter
    def remain_amount(self, value):
        self[OrderKeys.RemainAmount] = value

    @property
    def upper_bound(self) -> int:
        return self[OrderKeys.UpperBound]

    @upper_bound.setter
    def upper_bound(self, value):
        self[OrderKeys.UpperBound] = value

    @property
    def lower_bound(self) -> int:
        return self[OrderKeys.LowerBound]

    @lower_bound.setter
    def lower_bound(self, value):
        self[OrderKeys.LowerBound] = value

    @property
    def last_match_price(self) -> int:
        return self[OrderKeys.LastMatchPrice]

    @last_match_price.setter
    def last_match_price(self, value):
        self[OrderKeys.LastMatchPrice] = value

    @property
    def leg_to_price(self) -> int:
        return self[OrderKeys.Leg2Price]

    @leg_to_price.setter
    def leg_to_price(self, value):
        self[OrderKeys.Leg2Price] = value

    @property
    def average_price(self) -> int:
        return self[OrderKeys.AveragePrice]

    @average_price.setter
    def average_price(self, value):
        self[OrderKeys.AveragePrice] = value

    @property
    def last_match_quantity(self) -> int:
        return self[OrderKeys.LastMatchQuantity]

    @last_match_quantity.setter
    def last_match_quantity(self, value):
        self[OrderKeys.LastMatchQuantity] = value

    @property
    def order_id(self) -> int:
        return self[OrderKeys.OrderId]

    @order_id.setter
    def order_id(self, value):
        self[OrderKeys.OrderId] = value

    @property
    def client_order_id(self) -> int:
        return self[OrderKeys.ClientOrderId]

    @client_order_id.setter
    def client_order_id(self, value):
        self[OrderKeys.ClientOrderId] = value

    @property
    def last_matched_order_id(self) -> int:
        return self[OrderKeys.LastMatchedOrderId]

    @last_matched_order_id.setter
    def last_matched_order_id(self, value):
        self[OrderKeys.LastMatchedOrderId] = value

    @property
    def last_matched_order_id2(self) -> int:
        return self[OrderKeys.LastMatchedOrderId2]

    @last_matched_order_id2.setter
    def last_matched_order_id2(self, value):
        self[OrderKeys.LastMatchedOrderId2] = value

    @property
    def matched_id(self) -> int:
        return self[OrderKeys.MatchedId]

    @matched_id.setter
    def matched_id(self, value):
        self[OrderKeys.MatchedId] = value

    @property
    def sort_id(self) -> int:
        return self[OrderKeys.SortId]

    @sort_id.setter
    def sort_id(self, value):
        self[OrderKeys.SortId] = value

    @property
    def trigger_price(self) -> int:
        return self[OrderKeys.TriggerPrice]

    @trigger_price.setter
    def trigger_price(self, value):
        self[OrderKeys.TriggerPrice] = value

    @property
    def is_triggered(self) -> bool:
        return bool(self[OrderKeys.IsTriggered])

    @is_triggered.setter
    def is_triggered(self, value: bool):
        self[OrderKeys.IsTriggered] = bool(value)

    # TODO: Check Type
    @property
    def timestamp(self) -> int:
        return self[OrderKeys.Timestamp]

    @timestamp.setter
    def timestamp(self, value):
        self[OrderKeys.Timestamp] = value

    # TODO: IS BOOL
    @property
    def order_created(self) -> int:
        return self[OrderKeys.OrderCreated]

    @order_created.setter
    def order_created(self, value):
        self[OrderKeys.OrderCreated] = value

    @property
    def total_trade_amount(self) -> int:
        return self[OrderKeys.TotalTradeAmount]

    @total_trade_amount.setter
    def total_trade_amount(self, value):
        self[OrderKeys.TotalTradeAmount] = value

    @property
    def total_trade_quantity(self) -> int:
        return self[OrderKeys.TotalTradeQuantity]

    @total_trade_quantity.setter
    def total_trade_quantity(self, value):
        self[OrderKeys.TotalTradeQuantity] = value

    @property
    def source(self) -> int:
        return self[OrderKeys.Source]

    @source.setter
    def source(self, value):
        self[OrderKeys.Source] = value

    @property
    def tag(self) -> int:
        return self[OrderKeys.Tag]

    @tag.setter
    def tag(self, value):
        self[OrderKeys.Tag] = value


if __name__ == '__main__':
    order: Order = Order()

    order.side = OrderSide.BUY
    print(order.side)

    order.type = OrderType.LIMIT
    print(order.type)

    order.stop_condition = OrderStopCondition.GREATER_EQUAL
    print(order.stop_condition)

    order.action = OrderActionType.CANCEL
    print(order.action)

    order.time_condition = OrderTimeCondition.MAKER_ONLY_REPRICE
    print(order.time_condition)

    order.trigger_type = TriggerType.MARK_PRICE
    print(order.trigger_type)

    order.self_trade_protection = SelfTradeProtectionType.STP_BOTH
    print(order.self_trade_protection)

    order.status = OrderStatusType.CANCELED_BY_MARKET_ORDER_NOTHING_MATCH
    print(order.status)

    order.matched_type = OrderMatchedType.TAKER
    print(order.matched_type)



    order.is_triggered = 33
    print(order.is_triggered)


    print('\n' + '==' * 50 + '\n\n' + str(order))
    print('\n' + '==' * 50 + '\n\n' + json.dumps(order, indent=4))
