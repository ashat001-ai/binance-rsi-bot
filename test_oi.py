import asyncio

from app.binance_client import BinanceClient


async def main():

    async with BinanceClient() as client:

        oi = await client.get_open_interest("BTCUSDT")

        print("BTC Open Interest:", oi)


asyncio.run(main())

