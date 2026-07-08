import aiohttp


class BinanceClient:
    BASE_URL = "https://fapi.binance.com"

    async def get_exchange_info(self):
        async with aiohttp.ClientSession() as session:
            async with session.get(f"{self.BASE_URL}/fapi/v1/exchangeInfo") as resp:
                resp.raise_for_status()
                return await resp.json()

    async def get_usdt_symbols(self):
        data = await self.get_exchange_info()

        symbols = [
            s["symbol"]
            for s in data["symbols"]
            if s["status"] == "TRADING"
            and s["quoteAsset"] == "USDT"
        ]
    async def get_klines(
        self,
        symbol: str,
        interval: str = "1h",
        limit: int = 200,
    ):
        params = {
            "symbol": symbol,
            "interval": interval,
            "limit": limit,
        }

        async with aiohttp.ClientSession() as session:
            async with session.get(
                f"{self.BASE_URL}/fapi/v1/klines",
                params=params,
            ) as resp:
                resp.raise_for_status()
                return await resp.json()

        return sorted(symbols)
