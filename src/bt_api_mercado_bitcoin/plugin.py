from __future__ import annotations

from bt_api_base.gateway.registrar import GatewayRuntimeRegistrar
from bt_api_base.plugins.protocol import PluginInfo
from bt_api_base.registry import ExchangeRegistry

from bt_api_mercado_bitcoin import __version__
from bt_api_mercado_bitcoin.registry_registration import register_mercado_bitcoin


def register_plugin(
    registry: type[ExchangeRegistry],
    runtime_factory: type[GatewayRuntimeRegistrar],
) -> PluginInfo:
    register_mercado_bitcoin(registry)
    return PluginInfo(
        name="bt_api_mercado_bitcoin",
        version=__version__,
        core_requires=">=0.15,<1.0",
        supported_exchanges=("MERCADO_BITCOIN___SPOT",),
        supported_asset_types=("SPOT",),
    )
