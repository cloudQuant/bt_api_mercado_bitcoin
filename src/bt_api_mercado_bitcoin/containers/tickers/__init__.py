from __future__ import annotations

import json
import time
from typing import Any

from bt_api_base._compat import Self
from bt_api_base.containers.tickers.ticker import TickerData
from bt_api_base.functions.utils import from_dict_get_float


class MercadoBitcoinTickerData(TickerData):
    def __init__(
        self,
        ticker_info: str | dict[str, Any],
        symbol_name: str,
        asset_type: str,
        has_been_json_encoded: bool = False,
    ) -> None:
        super().__init__(ticker_info, has_been_json_encoded)
        self.exchange_name = "MERCADO_BITCOIN"
        self.local_update_time = time.time()
        self.symbol_name = symbol_name
        self.asset_type = asset_type
        self.ticker_data: dict[str, Any] | None = (
            ticker_info if has_been_json_encoded and isinstance(ticker_info, dict) else None
        )
        self.ticker_symbol_name: str | None = None
        self.server_time: float | None = None
        self.last_price: float | None = None
        self.bid_price: float | None = None
        self.ask_price: float | None = None
        self.bid_volume: float | None = None
        self.ask_volume: float | None = None
        self.volume: float | None = None
        self.high: float | None = None
        self.low: float | None = None
        self.has_been_init_data = False

    def init_data(self) -> Self:
        if not self.has_been_json_encoded:
            self.ticker_data = json.loads(self.ticker_info)
            self.has_been_json_encoded = True
        if self.has_been_init_data:
            return self

        data = self.ticker_data or {}
        if isinstance(data, dict):
            ticker = data.get("ticker", data)
            if isinstance(ticker, dict):
                self.ticker_symbol_name = self.symbol_name
                self.last_price = from_dict_get_float(ticker, "last")
                self.bid_price = from_dict_get_float(ticker, "buy")
                self.ask_price = from_dict_get_float(ticker, "sell")
                self.volume = from_dict_get_float(ticker, "vol")
                self.high = from_dict_get_float(ticker, "high")
                self.low = from_dict_get_float(ticker, "low")
                self.server_time = from_dict_get_float(ticker, "date")

        self.has_been_init_data = True
        return self

    def get_exchange_name(self) -> str:
        return self.exchange_name

    def get_symbol_name(self) -> str:
        return self.symbol_name

    def get_asset_type(self) -> str:
        return self.asset_type

    def get_last_price(self) -> float | None:
        self.init_data()
        return self.last_price

    def get_bid_price(self) -> float | None:
        self.init_data()
        return self.bid_price

    def get_ask_price(self) -> float | None:
        self.init_data()
        return self.ask_price

    def get_bid_volume(self) -> float | None:
        self.init_data()
        return self.bid_volume

    def get_ask_volume(self) -> float | None:
        self.init_data()
        return self.ask_volume

    def get_high(self) -> float | None:
        self.init_data()
        return self.high

    def get_low(self) -> float | None:
        self.init_data()
        return self.low

    def get_volume(self) -> float | None:
        self.init_data()
        return self.volume


class MercadoBitcoinRequestTickerData(MercadoBitcoinTickerData):
    pass


class MercadoBitcoinWssTickerData(MercadoBitcoinTickerData):
    pass
