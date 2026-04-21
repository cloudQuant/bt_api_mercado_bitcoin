from __future__ import annotations

from typing import Any

from bt_api_mercado_bitcoin.feeds.live_mercado_bitcoin.request_base import MercadoBitcoinRequestData


def test_mercado_bitcoin_accepts_public_private_key_aliases(monkeypatch: Any) -> None:
    request_data = MercadoBitcoinRequestData(public_key="public-key", private_key="secret-key")
    monkeypatch.setattr(
        "bt_api_mercado_bitcoin.feeds.live_mercado_bitcoin.request_base.time.time",
        lambda: 1700000000.0,
    )

    headers = request_data._get_headers("get_balance")

    assert request_data._params.api_key == "public-key"
    assert request_data._params.api_secret == "secret-key"
    assert headers["TAPI-ID"] == "public-key"
    assert headers["TAPI-MAC"]
