import asyncio

from app.binance_client import BinanceClient
from app.indicators import calculate_rsi


async def main():
    client = BinanceClient()

    symbol = "BTCUSDT"

    klines = await client.get_klines(symbol)

    closes = [float(k[4]) for k in klines]

    rsi = calculate_rsi(closes)

    print(f"{symbol}")
    print(f"Свечей: {len(closes)}")
    print(f"RSI: {rsi}")


if __name__ == "__main__":
    asyncio.run(main())
