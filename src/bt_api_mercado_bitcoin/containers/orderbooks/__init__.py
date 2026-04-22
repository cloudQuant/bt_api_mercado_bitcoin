from __future__ import annotations

import json
import time
from typing import Any

from bt_api_base.containers.orderbooks.orderbook import OrderBookData


class MercadoBitcoinOrderBookData(OrderBookData):
    def __init__(
        self,
        orderbook_info: str | dict[str, Any],
        symbol_name: str,
        asset_type: str,
        has_been_json_encoded: bool = False,
    ) -> None:
        super().__init__(orderbook_info, has_been_json_encoded)
        self.exchange_name = "MERCADO_BITCOIN"
        self.local_update_time = time.time()
        self.symbol_name = symbol_name
        self.asset_type = asset_type
        self.orderbook_data: dict[str, Any] | None = (
            orderbook_info if has_been_json_encoded and isinstance(orderbook_info, dict) else None
        )
        self.bids: list[list[float]] | None = None
        self.asks: list[list[float]] | None = None
        self.has_been_init_data = False

    def init_data(self) -> MercadoBitcoinOrderBookData:
        if not self.has_been_json_encoded:
            self.orderbook_data = (
                json.loads(self.orderbook_info) if isinstance(self.orderbook_info, str) else {}
            )
            self.has_been_json_encoded = True
        if self.has_been_init_data:
            return self

        if isinstance(self.orderbook_data, dict):
            data = self.orderbook_data
            bid_list = data.get("bids", []) if isinstance(data.get("bids", []), list) else []
            ask_list = data.get("asks", []) if isinstance(data.get("asks", []), list) else []
            self.bids = [
                [float(item[0]) if len(item) > 0 else 0.0, float(item[1]) if len(item) > 1 else 0.0]
                for item in bid_list
                if isinstance(item, list)
            ]
            self.asks = [
                [float(item[0]) if len(item) > 0 else 0.0, float(item[1]) if len(item) > 1 else 0.0]
                for item in ask_list
                if isinstance(item, list)
            ]

        self.has_been_init_data = True
        return self

    def get_exchange_name(self) -> str:
        return self.exchange_name

    def get_symbol_name(self) -> str:
        return self.symbol_name

    def get_asset_type(self) -> str:
        return self.asset_type

    def get_bids(self) -> list[list[float]]:
        self.init_data()
        return self.bids or []

    def get_asks(self) -> list[list[float]]:
        self.init_data()
        return self.asks or []

    def get_local_update_time(self) -> float:
        return float(self.local_update_time)


class MercadoBitcoinRequestOrderBookData(MercadoBitcoinOrderBookData):
    pass


class MercadoBitcoinWssOrderBookData(MercadoBitcoinOrderBookData):
    pass
