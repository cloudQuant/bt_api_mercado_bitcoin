from __future__ import annotations

from unittest.mock import MagicMock

from bt_api_mercado_bitcoin.feeds.live_mercado_bitcoin.request_base import MercadoBitcoinRequestData


def test_mercado_bitcoin_disconnect_closes_http_client() -> None:
    request_data = MercadoBitcoinRequestData()
    request_data._http_client.close = MagicMock()

    request_data.disconnect()

    request_data._http_client.close.assert_called_once_with()
