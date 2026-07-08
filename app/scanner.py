import asyncio

from app.indicators import rsi


class Scanner:

    def __init__(self, client):
        self.client = client
        self.sem = asyncio.Semaphore(20)

    async def scan_symbol(self, symbol):

        async with self.sem:

            try:

                candles = await self.client.get_klines(symbol)

                if not candles or len(candles) < 20:
                    return None

                closed = candles[:-1]

                closes = [float(c[4]) for c in closed]

                value = rsi(closes)

                if value is None:
                    return None

                last = closed[-1]

                return {
                    "symbol": symbol,
                    "rsi": round(value, 2),
                    "price": float(last[4]),
                    "volume": float(last[7]),
                    "close_time": last[6],
                }

            except Exception:
                return None

    async def scan(self):

        symbols = await self.client.get_symbols()

        tasks = [self.scan_symbol(symbol) for symbol in symbols]

        result = await asyncio.gather(*tasks)

        return [x for x in result if x is not None]
