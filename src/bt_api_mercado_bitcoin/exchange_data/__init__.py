from __future__ import annotations

from bt_api_base.containers.exchanges.exchange_data import ExchangeData


class MercadoBitcoinExchangeData(ExchangeData):
    def __init__(self) -> None:
        super().__init__()
        self.exchange_name = "MERCADO_BITCOIN___SPOT"
        self.rest_url = "https://www.mercadobitcoin.net/api"
        self.rest_private_url = "https://www.mercadobitcoin.net/tapi"
        self.rest_v4_url = "https://api.mercadobitcoin.net/api/v4"
        self.wss_url = "wss://ws.mercadobitcoin.net"
        self.rest_paths = {}
        self.wss_paths = {}
        self.kline_periods = {
            "15m": "15m",
            "1h": "1h",
            "3h": "3h",
            "1d": "1d",
            "1w": "1w",
            "1M": "1M",
        }
        self.legal_currency = ["BRL"]

    def get_symbol(self, symbol: str) -> str:
        return symbol

    def get_period(self, key, default=None):
        return self.kline_periods.get(key, default or key)


class MercadoBitcoinExchangeDataSpot(MercadoBitcoinExchangeData):
    def __init__(self) -> None:
        super().__init__()
        self.asset_type = "spot"
