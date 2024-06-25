import typing
import json
from enum import Enum, IntEnum


class OrderSide(str, Enum):
    BUY = 'BUY'
    SELL = 'SELL'


class OrderType(str, Enum):
    LIMIT = 'LIMIT'
    MARKET = 'MARKET'
    STOP_LIMIT = 'STOP_LIMIT'
    STOP_MARKET = 'STOP_MARKET'
    TAKE_PROFIT_LIMIT = 'TAKE_PROFIT_LIMIT'
    TAKE_PROFIT_MARKET = 'TAKE_PROFIT_MARKET'


class OrderStopCondition(str, Enum):
    NONE = 'NONE'
    GREATER_EQUAL = 'GREATER_EQUAL'
    LESS_EQUAL = 'LESS_EQUAL'


class OrderActionType(str, Enum):
    NEW = 'NEW'
    AMEND = 'CANCEL'
    CANCEL = 'CANCEL'
    RECOVERY = 'RECOVERY'
    RECOVERY_END = 'RECOVERY_END'


class OrderTimeCondition(str, Enum):
    GTC = 'GTC'
    IOC = 'IOC'
    FOK = 'FOK'
    MAKER_ONLY = 'MAKER_ONLY'
    MAKER_ONLY_REPRICE = 'MAKER_ONLY_REPRICE'


class TriggerType(str, Enum):
    MARK_PRICE = 'MARK_PRICE'
    LAST_PRICE = 'LAST_PRICE'
    TRIGGER_NONE = 'NONE'


class SelfTradeProtectionType(str, Enum):
    STP_NONE = 'NONE'
    STP_TAKER = 'EXPIRE_TAKER'
    STP_MAKER = 'EXPIRE_MAKER'
    STP_BOTH = 'EXPIRE_BOTH'


class OrderStatusType(str, Enum):
    OPEN = 'OPEN'
    PARTIAL_FILL = 'PARTIAL_FILL'
    FILLED = 'FILLED'
    CANCELED_BY_USER = 'CANCELED_BY_USER'
    CANCELED_BY_MARKET_ORDER_NOT_FULL_MATCHED = 'CANCELED_BY_MARKET_ORDER_NOT_FULL_MATCHED'
    CANCELED_BY_MARKET_ORDER_NOTHING_MATCH = 'CANCELED_BY_MARKET_ORDER_NOTHING_MATCH'
    CANCELED_ALL_BY_IOC = 'CANCELED_ALL_BY_IOC'
    CANCELED_PARTIAL_BY_IOC = 'CANCELED_PARTIAL_BY_IOC'
    CANCELED_BY_FOK = 'CANCELED_BY_FOK'
    CANCELED_BY_MAKER_ONLY = 'CANCELED_BY_MAKER_ONLY'
    CANCELED_BY_AMEND = 'CANCELED_BY_AMEND'
    CANCELED_BY_SELF_TRADE_PROTECTION = 'CANCELED_BY_SELF_TRADE_PROTECTION'
    REJECT_CANCEL_ORDER_ID_NOT_FOUND = 'REJECT_CANCEL_ORDER_ID_NOT_FOUND'
    REJECT_AMEND_ORDER_ID_NOT_FOUND = 'REJECT_AMEND_ORDER_ID_NOT_FOUND'
    REJECT_DISPLAY_QUANTITY_ZERO = 'REJECT_DISPLAY_QUANTITY_ZERO'
    REJECT_DISPLAY_QUANTITY_LARGER_THAN_QUANTITY = 'REJECT_DISPLAY_QUANTITY_LARGER_THAN_QUANTITY'
    REJECT_QUANTITY_AND_AMOUNT_ZERO = 'REJECT_QUANTITY_AND_AMOUNT_ZERO'
    REJECT_LIMIT_ORDER_WITH_MARKET_PRICE = 'REJECT_LIMIT_ORDER_WITH_MARKET_PRICE'
    REJECT_MATCHING_ENGINE_RECOVERING = 'REJECT_MATCHING_ENGINE_RECOVERING'
    REJECT_STOP_CONDITION_IS_NONE = 'REJECT_STOP_CONDITION_IS_NONE'
    REJECT_STOP_TRIGGER_PRICE_IS_NONE = 'REJECT_STOP_TRIGGER_PRICE_IS_NONE'
    REJECT_QUANTITY_AND_AMOUNT_LARGER_ZERO = 'REJECT_QUANTITY_AND_AMOUNT_LARGER_ZERO'
    REJECT_PRICE_LESS_ZERO = 'REJECT_PRICE_LESS_ZERO'
    REJECT_ORDER_QUANTITY_GREATER_THAN_MAX = 'REJECT_ORDER_QUANTITY_GREATER_THAN_MAX'
    REJECT_ORDER_AMOUNT_GREATER_THAN_MAX = 'REJECT_ORDER_AMOUNT_GREATER_THAN_MAX'
    REJECT_MAXIMUM_OPEN_ORDERS_LIMIT_REACHED = 'REJECT_MAXIMUM_OPEN_ORDERS_LIMIT_REACHED'


class OrderMatchedType(str, Enum):
    MAKER = 'MAKER'
    TAKER = 'TAKER'


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

    def asJson(self) -> str:
        return json.dumps(self)
