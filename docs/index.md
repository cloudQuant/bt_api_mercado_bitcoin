# MERCADO_BITCOIN Documentation

## English

Welcome to the MERCADO_BITCOIN documentation for bt_api.

### Quick Start

```bash
pip install bt_api_mercado_bitcoin
```

```python
from bt_api_mercado_bitcoin import MercadoBitcoinApi
feed = MercadoBitcoinApi(api_key="your_key", secret="your_secret")
ticker = feed.get_ticker("BTCUSDT")
```

## 中文

欢迎使用 bt_api 的 MERCADO_BITCOIN 文档。

### 快速开始

```bash
pip install bt_api_mercado_bitcoin
```

```python
from bt_api_mercado_bitcoin import MercadoBitcoinApi
feed = MercadoBitcoinApi(api_key="your_key", secret="your_secret")
ticker = feed.get_ticker("BTCUSDT")
```

## API Reference

See source code in `src/bt_api_mercado_bitcoin/` for detailed API documentation.
