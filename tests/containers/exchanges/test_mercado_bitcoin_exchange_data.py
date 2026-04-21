"""Tests for MercadoBitcoinExchangeData container."""

from __future__ import annotations

from bt_api_mercado_bitcoin.exchange_data import MercadoBitcoinExchangeData


class TestMercadoBitcoinExchangeData:
    """Tests for MercadoBitcoinExchangeData."""

    def test_init(self):
        """Test initialization."""
        exchange = MercadoBitcoinExchangeData()

        assert exchange.exchange_name == "MERCADO_BITCOIN___SPOT"
