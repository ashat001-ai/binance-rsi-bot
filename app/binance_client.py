import asyncio

import aiohttp

from app.config import config


class BinanceClient:

    def __init__(self):
        self.session = None

    async def __aenter__(self):
        timeout = aiohttp.ClientTimeout(total=config.REQUEST_TIMEOUT)
        self.session = aiohttp.ClientSession(timeout=timeout)
        return self

    async def __aexit__(self, exc_type, exc, tb):
        if self.session:
            await self.session.close()

    async def request(self, endpoint, params=None):

        url = f"{config.BASE_URL}{endpoint}"

        for attempt in range(3):

            try:

                async with self.session.get(url, params=params) as response:

                    response.raise_for_status()

                    return await response.json()

            except (
                aiohttp.ClientError,
                asyncio.TimeoutError,
            ):

                if attempt == 2:
                    raise

                await asyncio.sleep(1)

    async def get_symbols(self):

        data = await self.request("/fapi/v1/exchangeInfo")

        return [
            s["symbol"]
            for s in data["symbols"]
            if s["quoteAsset"] == "USDT"
            and s["status"] == "TRADING"
        ]

    async def get_klines(self, symbol):

        return await self.request(
            "/fapi/v1/klines",
            {
                "symbol": symbol,
                "interval": config.INTERVAL,
                "limit": config.LIMIT,
            },
        )

    async def get_price(self, symbol):

        data = await self.request(
            "/fapi/v2/ticker/price",
            {
                "symbol": symbol,
            },
        )

        return float(data["price"])
