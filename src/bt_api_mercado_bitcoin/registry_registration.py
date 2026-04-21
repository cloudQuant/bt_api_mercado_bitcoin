from __future__ import annotations

from bt_api_base.balance_utils import simple_balance_handler as _mercado_bitcoin_balance_handler
from bt_api_base.registry import ExchangeRegistry

from bt_api_mercado_bitcoin.exchange_data import MercadoBitcoinExchangeDataSpot
from bt_api_mercado_bitcoin.feeds.live_mercado_bitcoin.spot import MercadoBitcoinRequestDataSpot


def register_mercado_bitcoin(registry: type[ExchangeRegistry]) -> None:
    registry.register_feed("MERCADO_BITCOIN___SPOT", MercadoBitcoinRequestDataSpot)
    registry.register_exchange_data("MERCADO_BITCOIN___SPOT", MercadoBitcoinExchangeDataSpot)
    registry.register_balance_handler("MERCADO_BITCOIN___SPOT", _mercado_bitcoin_balance_handler)
