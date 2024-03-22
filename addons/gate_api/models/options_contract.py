# coding: utf-8

"""
    Gate API v4

    Welcome to Gate.io API  APIv4 provides spot, margin and futures trading operations. There are public APIs to retrieve the real-time market statistics, and private APIs which needs authentication to trade on user's behalf.  # noqa: E501

    Contact: support@mail.gate.io
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from odoo.addons.gate_api.configuration import Configuration


class OptionsContract(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'name': 'str',
        'tag': 'str',
        'create_time': 'float',
        'expiration_time': 'float',
        'is_call': 'bool',
        'multiplier': 'str',
        'underlying': 'str',
        'underlying_price': 'str',
        'last_price': 'str',
        'mark_price': 'str',
        'index_price': 'str',
        'maker_fee_rate': 'str',
        'taker_fee_rate': 'str',
        'order_price_round': 'str',
        'mark_price_round': 'str',
        'order_size_min': 'int',
        'order_size_max': 'int',
        'order_price_deviate': 'str',
        'ref_discount_rate': 'str',
        'ref_rebate_rate': 'str',
        'orderbook_id': 'int',
        'trade_id': 'int',
        'trade_size': 'int',
        'position_size': 'int',
        'orders_limit': 'int',
    }

    attribute_map = {
        'name': 'name',
        'tag': 'tag',
        'create_time': 'create_time',
        'expiration_time': 'expiration_time',
        'is_call': 'is_call',
        'multiplier': 'multiplier',
        'underlying': 'underlying',
        'underlying_price': 'underlying_price',
        'last_price': 'last_price',
        'mark_price': 'mark_price',
        'index_price': 'index_price',
        'maker_fee_rate': 'maker_fee_rate',
        'taker_fee_rate': 'taker_fee_rate',
        'order_price_round': 'order_price_round',
        'mark_price_round': 'mark_price_round',
        'order_size_min': 'order_size_min',
        'order_size_max': 'order_size_max',
        'order_price_deviate': 'order_price_deviate',
        'ref_discount_rate': 'ref_discount_rate',
        'ref_rebate_rate': 'ref_rebate_rate',
        'orderbook_id': 'orderbook_id',
        'trade_id': 'trade_id',
        'trade_size': 'trade_size',
        'position_size': 'position_size',
        'orders_limit': 'orders_limit',
    }

    def __init__(
        self,
        name=None,
        tag=None,
        create_time=None,
        expiration_time=None,
        is_call=None,
        multiplier=None,
        underlying=None,
        underlying_price=None,
        last_price=None,
        mark_price=None,
        index_price=None,
        maker_fee_rate=None,
        taker_fee_rate=None,
        order_price_round=None,
        mark_price_round=None,
        order_size_min=None,
        order_size_max=None,
        order_price_deviate=None,
        ref_discount_rate=None,
        ref_rebate_rate=None,
        orderbook_id=None,
        trade_id=None,
        trade_size=None,
        position_size=None,
        orders_limit=None,
        local_vars_configuration=None,
    ):  # noqa: E501
        # type: (str, str, float, float, bool, str, str, str, str, str, str, str, str, str, str, int, int, str, str, str, int, int, int, int, int, Configuration) -> None
        """OptionsContract - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._tag = None
        self._create_time = None
        self._expiration_time = None
        self._is_call = None
        self._multiplier = None
        self._underlying = None
        self._underlying_price = None
        self._last_price = None
        self._mark_price = None
        self._index_price = None
        self._maker_fee_rate = None
        self._taker_fee_rate = None
        self._order_price_round = None
        self._mark_price_round = None
        self._order_size_min = None
        self._order_size_max = None
        self._order_price_deviate = None
        self._ref_discount_rate = None
        self._ref_rebate_rate = None
        self._orderbook_id = None
        self._trade_id = None
        self._trade_size = None
        self._position_size = None
        self._orders_limit = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if tag is not None:
            self.tag = tag
        if create_time is not None:
            self.create_time = create_time
        if expiration_time is not None:
            self.expiration_time = expiration_time
        if is_call is not None:
            self.is_call = is_call
        if multiplier is not None:
            self.multiplier = multiplier
        if underlying is not None:
            self.underlying = underlying
        if underlying_price is not None:
            self.underlying_price = underlying_price
        if last_price is not None:
            self.last_price = last_price
        if mark_price is not None:
            self.mark_price = mark_price
        if index_price is not None:
            self.index_price = index_price
        if maker_fee_rate is not None:
            self.maker_fee_rate = maker_fee_rate
        if taker_fee_rate is not None:
            self.taker_fee_rate = taker_fee_rate
        if order_price_round is not None:
            self.order_price_round = order_price_round
        if mark_price_round is not None:
            self.mark_price_round = mark_price_round
        if order_size_min is not None:
            self.order_size_min = order_size_min
        if order_size_max is not None:
            self.order_size_max = order_size_max
        if order_price_deviate is not None:
            self.order_price_deviate = order_price_deviate
        if ref_discount_rate is not None:
            self.ref_discount_rate = ref_discount_rate
        if ref_rebate_rate is not None:
            self.ref_rebate_rate = ref_rebate_rate
        if orderbook_id is not None:
            self.orderbook_id = orderbook_id
        if trade_id is not None:
            self.trade_id = trade_id
        if trade_size is not None:
            self.trade_size = trade_size
        if position_size is not None:
            self.position_size = position_size
        if orders_limit is not None:
            self.orders_limit = orders_limit

    @property
    def name(self):
        """Gets the name of this OptionsContract.  # noqa: E501

        Futures contract  # noqa: E501

        :return: The name of this OptionsContract.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this OptionsContract.

        Futures contract  # noqa: E501

        :param name: The name of this OptionsContract.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def tag(self):
        """Gets the tag of this OptionsContract.  # noqa: E501

        标记  # noqa: E501

        :return: The tag of this OptionsContract.  # noqa: E501
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """Sets the tag of this OptionsContract.

        标记  # noqa: E501

        :param tag: The tag of this OptionsContract.  # noqa: E501
        :type: str
        """

        self._tag = tag

    @property
    def create_time(self):
        """Gets the create_time of this OptionsContract.  # noqa: E501

        Creation time  # noqa: E501

        :return: The create_time of this OptionsContract.  # noqa: E501
        :rtype: float
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this OptionsContract.

        Creation time  # noqa: E501

        :param create_time: The create_time of this OptionsContract.  # noqa: E501
        :type: float
        """

        self._create_time = create_time

    @property
    def expiration_time(self):
        """Gets the expiration_time of this OptionsContract.  # noqa: E501

        Expiration time  # noqa: E501

        :return: The expiration_time of this OptionsContract.  # noqa: E501
        :rtype: float
        """
        return self._expiration_time

    @expiration_time.setter
    def expiration_time(self, expiration_time):
        """Sets the expiration_time of this OptionsContract.

        Expiration time  # noqa: E501

        :param expiration_time: The expiration_time of this OptionsContract.  # noqa: E501
        :type: float
        """

        self._expiration_time = expiration_time

    @property
    def is_call(self):
        """Gets the is_call of this OptionsContract.  # noqa: E501

        `true` means call options, while `false` is put options  # noqa: E501

        :return: The is_call of this OptionsContract.  # noqa: E501
        :rtype: bool
        """
        return self._is_call

    @is_call.setter
    def is_call(self, is_call):
        """Sets the is_call of this OptionsContract.

        `true` means call options, while `false` is put options  # noqa: E501

        :param is_call: The is_call of this OptionsContract.  # noqa: E501
        :type: bool
        """

        self._is_call = is_call

    @property
    def multiplier(self):
        """Gets the multiplier of this OptionsContract.  # noqa: E501

        Multiplier used in converting from invoicing to settlement currency  # noqa: E501

        :return: The multiplier of this OptionsContract.  # noqa: E501
        :rtype: str
        """
        return self._multiplier

    @multiplier.setter
    def multiplier(self, multiplier):
        """Sets the multiplier of this OptionsContract.

        Multiplier used in converting from invoicing to settlement currency  # noqa: E501

        :param multiplier: The multiplier of this OptionsContract.  # noqa: E501
        :type: str
        """

        self._multiplier = multiplier

    @property
    def underlying(self):
        """Gets the underlying of this OptionsContract.  # noqa: E501

        Underlying  # noqa: E501

        :return: The underlying of this OptionsContract.  # noqa: E501
        :rtype: str
        """
        return self._underlying

    @underlying.setter
    def underlying(self, underlying):
        """Sets the underlying of this OptionsContract.

        Underlying  # noqa: E501

        :param underlying: The underlying of this OptionsContract.  # noqa: E501
        :type: str
        """

        self._underlying = underlying

    @property
    def underlying_price(self):
        """Gets the underlying_price of this OptionsContract.  # noqa: E501

        Underlying price  # noqa: E501

        :return: The underlying_price of this OptionsContract.  # noqa: E501
        :rtype: str
        """
        return self._underlying_price

    @underlying_price.setter
    def underlying_price(self, underlying_price):
        """Sets the underlying_price of this OptionsContract.

        Underlying price  # noqa: E501

        :param underlying_price: The underlying_price of this OptionsContract.  # noqa: E501
        :type: str
        """

        self._underlying_price = underlying_price

    @property
    def last_price(self):
        """Gets the last_price of this OptionsContract.  # noqa: E501

        Last trading price  # noqa: E501

        :return: The last_price of this OptionsContract.  # noqa: E501
        :rtype: str
        """
        return self._last_price

    @last_price.setter
    def last_price(self, last_price):
        """Sets the last_price of this OptionsContract.

        Last trading price  # noqa: E501

        :param last_price: The last_price of this OptionsContract.  # noqa: E501
        :type: str
        """

        self._last_price = last_price

    @property
    def mark_price(self):
        """Gets the mark_price of this OptionsContract.  # noqa: E501

        Current mark price  # noqa: E501

        :return: The mark_price of this OptionsContract.  # noqa: E501
        :rtype: str
        """
        return self._mark_price

    @mark_price.setter
    def mark_price(self, mark_price):
        """Sets the mark_price of this OptionsContract.

        Current mark price  # noqa: E501

        :param mark_price: The mark_price of this OptionsContract.  # noqa: E501
        :type: str
        """

        self._mark_price = mark_price

    @property
    def index_price(self):
        """Gets the index_price of this OptionsContract.  # noqa: E501

        Current index price  # noqa: E501

        :return: The index_price of this OptionsContract.  # noqa: E501
        :rtype: str
        """
        return self._index_price

    @index_price.setter
    def index_price(self, index_price):
        """Sets the index_price of this OptionsContract.

        Current index price  # noqa: E501

        :param index_price: The index_price of this OptionsContract.  # noqa: E501
        :type: str
        """

        self._index_price = index_price

    @property
    def maker_fee_rate(self):
        """Gets the maker_fee_rate of this OptionsContract.  # noqa: E501

        Maker fee rate, where negative means rebate  # noqa: E501

        :return: The maker_fee_rate of this OptionsContract.  # noqa: E501
        :rtype: str
        """
        return self._maker_fee_rate

    @maker_fee_rate.setter
    def maker_fee_rate(self, maker_fee_rate):
        """Sets the maker_fee_rate of this OptionsContract.

        Maker fee rate, where negative means rebate  # noqa: E501

        :param maker_fee_rate: The maker_fee_rate of this OptionsContract.  # noqa: E501
        :type: str
        """

        self._maker_fee_rate = maker_fee_rate

    @property
    def taker_fee_rate(self):
        """Gets the taker_fee_rate of this OptionsContract.  # noqa: E501

        Taker fee rate  # noqa: E501

        :return: The taker_fee_rate of this OptionsContract.  # noqa: E501
        :rtype: str
        """
        return self._taker_fee_rate

    @taker_fee_rate.setter
    def taker_fee_rate(self, taker_fee_rate):
        """Sets the taker_fee_rate of this OptionsContract.

        Taker fee rate  # noqa: E501

        :param taker_fee_rate: The taker_fee_rate of this OptionsContract.  # noqa: E501
        :type: str
        """

        self._taker_fee_rate = taker_fee_rate

    @property
    def order_price_round(self):
        """Gets the order_price_round of this OptionsContract.  # noqa: E501

        Minimum order price increment  # noqa: E501

        :return: The order_price_round of this OptionsContract.  # noqa: E501
        :rtype: str
        """
        return self._order_price_round

    @order_price_round.setter
    def order_price_round(self, order_price_round):
        """Sets the order_price_round of this OptionsContract.

        Minimum order price increment  # noqa: E501

        :param order_price_round: The order_price_round of this OptionsContract.  # noqa: E501
        :type: str
        """

        self._order_price_round = order_price_round

    @property
    def mark_price_round(self):
        """Gets the mark_price_round of this OptionsContract.  # noqa: E501

        Minimum mark price increment  # noqa: E501

        :return: The mark_price_round of this OptionsContract.  # noqa: E501
        :rtype: str
        """
        return self._mark_price_round

    @mark_price_round.setter
    def mark_price_round(self, mark_price_round):
        """Sets the mark_price_round of this OptionsContract.

        Minimum mark price increment  # noqa: E501

        :param mark_price_round: The mark_price_round of this OptionsContract.  # noqa: E501
        :type: str
        """

        self._mark_price_round = mark_price_round

    @property
    def order_size_min(self):
        """Gets the order_size_min of this OptionsContract.  # noqa: E501

        Minimum order size the contract allowed  # noqa: E501

        :return: The order_size_min of this OptionsContract.  # noqa: E501
        :rtype: int
        """
        return self._order_size_min

    @order_size_min.setter
    def order_size_min(self, order_size_min):
        """Sets the order_size_min of this OptionsContract.

        Minimum order size the contract allowed  # noqa: E501

        :param order_size_min: The order_size_min of this OptionsContract.  # noqa: E501
        :type: int
        """

        self._order_size_min = order_size_min

    @property
    def order_size_max(self):
        """Gets the order_size_max of this OptionsContract.  # noqa: E501

        Maximum order size the contract allowed  # noqa: E501

        :return: The order_size_max of this OptionsContract.  # noqa: E501
        :rtype: int
        """
        return self._order_size_max

    @order_size_max.setter
    def order_size_max(self, order_size_max):
        """Sets the order_size_max of this OptionsContract.

        Maximum order size the contract allowed  # noqa: E501

        :param order_size_max: The order_size_max of this OptionsContract.  # noqa: E501
        :type: int
        """

        self._order_size_max = order_size_max

    @property
    def order_price_deviate(self):
        """Gets the order_price_deviate of this OptionsContract.  # noqa: E501

        deviation between order price and current index price. If price of an order is denoted as order_price, it must meet the following condition:      abs(order_price - mark_price) <= mark_price * order_price_deviate  # noqa: E501

        :return: The order_price_deviate of this OptionsContract.  # noqa: E501
        :rtype: str
        """
        return self._order_price_deviate

    @order_price_deviate.setter
    def order_price_deviate(self, order_price_deviate):
        """Sets the order_price_deviate of this OptionsContract.

        deviation between order price and current index price. If price of an order is denoted as order_price, it must meet the following condition:      abs(order_price - mark_price) <= mark_price * order_price_deviate  # noqa: E501

        :param order_price_deviate: The order_price_deviate of this OptionsContract.  # noqa: E501
        :type: str
        """

        self._order_price_deviate = order_price_deviate

    @property
    def ref_discount_rate(self):
        """Gets the ref_discount_rate of this OptionsContract.  # noqa: E501

        Referral fee rate discount  # noqa: E501

        :return: The ref_discount_rate of this OptionsContract.  # noqa: E501
        :rtype: str
        """
        return self._ref_discount_rate

    @ref_discount_rate.setter
    def ref_discount_rate(self, ref_discount_rate):
        """Sets the ref_discount_rate of this OptionsContract.

        Referral fee rate discount  # noqa: E501

        :param ref_discount_rate: The ref_discount_rate of this OptionsContract.  # noqa: E501
        :type: str
        """

        self._ref_discount_rate = ref_discount_rate

    @property
    def ref_rebate_rate(self):
        """Gets the ref_rebate_rate of this OptionsContract.  # noqa: E501

        Referrer commission rate  # noqa: E501

        :return: The ref_rebate_rate of this OptionsContract.  # noqa: E501
        :rtype: str
        """
        return self._ref_rebate_rate

    @ref_rebate_rate.setter
    def ref_rebate_rate(self, ref_rebate_rate):
        """Sets the ref_rebate_rate of this OptionsContract.

        Referrer commission rate  # noqa: E501

        :param ref_rebate_rate: The ref_rebate_rate of this OptionsContract.  # noqa: E501
        :type: str
        """

        self._ref_rebate_rate = ref_rebate_rate

    @property
    def orderbook_id(self):
        """Gets the orderbook_id of this OptionsContract.  # noqa: E501

        Current orderbook ID  # noqa: E501

        :return: The orderbook_id of this OptionsContract.  # noqa: E501
        :rtype: int
        """
        return self._orderbook_id

    @orderbook_id.setter
    def orderbook_id(self, orderbook_id):
        """Sets the orderbook_id of this OptionsContract.

        Current orderbook ID  # noqa: E501

        :param orderbook_id: The orderbook_id of this OptionsContract.  # noqa: E501
        :type: int
        """

        self._orderbook_id = orderbook_id

    @property
    def trade_id(self):
        """Gets the trade_id of this OptionsContract.  # noqa: E501

        Current trade ID  # noqa: E501

        :return: The trade_id of this OptionsContract.  # noqa: E501
        :rtype: int
        """
        return self._trade_id

    @trade_id.setter
    def trade_id(self, trade_id):
        """Sets the trade_id of this OptionsContract.

        Current trade ID  # noqa: E501

        :param trade_id: The trade_id of this OptionsContract.  # noqa: E501
        :type: int
        """

        self._trade_id = trade_id

    @property
    def trade_size(self):
        """Gets the trade_size of this OptionsContract.  # noqa: E501

        Historical accumulated trade size  # noqa: E501

        :return: The trade_size of this OptionsContract.  # noqa: E501
        :rtype: int
        """
        return self._trade_size

    @trade_size.setter
    def trade_size(self, trade_size):
        """Sets the trade_size of this OptionsContract.

        Historical accumulated trade size  # noqa: E501

        :param trade_size: The trade_size of this OptionsContract.  # noqa: E501
        :type: int
        """

        self._trade_size = trade_size

    @property
    def position_size(self):
        """Gets the position_size of this OptionsContract.  # noqa: E501

        Current total long position size  # noqa: E501

        :return: The position_size of this OptionsContract.  # noqa: E501
        :rtype: int
        """
        return self._position_size

    @position_size.setter
    def position_size(self, position_size):
        """Sets the position_size of this OptionsContract.

        Current total long position size  # noqa: E501

        :param position_size: The position_size of this OptionsContract.  # noqa: E501
        :type: int
        """

        self._position_size = position_size

    @property
    def orders_limit(self):
        """Gets the orders_limit of this OptionsContract.  # noqa: E501

        Maximum number of open orders  # noqa: E501

        :return: The orders_limit of this OptionsContract.  # noqa: E501
        :rtype: int
        """
        return self._orders_limit

    @orders_limit.setter
    def orders_limit(self, orders_limit):
        """Sets the orders_limit of this OptionsContract.

        Maximum number of open orders  # noqa: E501

        :param orders_limit: The orders_limit of this OptionsContract.  # noqa: E501
        :type: int
        """

        self._orders_limit = orders_limit

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(lambda x: x.to_dict() if hasattr(x, "to_dict") else x, value))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(
                    map(
                        lambda item: (item[0], item[1].to_dict()) if hasattr(item[1], "to_dict") else item,
                        value.items(),
                    )
                )
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, OptionsContract):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OptionsContract):
            return True

        return self.to_dict() != other.to_dict()
