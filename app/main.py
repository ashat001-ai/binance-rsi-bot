import asyncio
import time

from app.binance_client import BinanceClient
from app.config import config, validate_config
from app.database import Database
from app.logger import logger
from app.scanner import Scanner
from app.telegram_client import TelegramClient

validate_config()


async def main():
    logger.info("=" * 60)
    logger.info(f"Binance Futures RSI Scanner v{config.VERSION}")
    logger.info("=" * 60)

    db = Database()
    await db.init()

    telegram = TelegramClient()

    async with BinanceClient() as client:

        scanner = Scanner(client)

        while True:

            started = time.time()

            try:

                signals = await scanner.scan()

                checked = len(signals)
                sent = 0
                skipped = 0
                removed = 0

                logger.info(f"Проверено монет: {checked}")

                for signal in signals:

                    symbol = signal["symbol"]
                    rsi = signal["rsi"]
                    price = signal["price"]
                    volume = signal["volume"]

                    if rsi <= config.RSI_LEVEL:

                        if await db.exists(symbol):
                            skipped += 1
                            logger.info(f"Уже отправлен: {symbol}")
                            continue

                        text = (
                            "🟢 <b>LONG SIGNAL</b>\n\n"
                            f"🪙 Монета: <b>{symbol}</b>\n"
                            f"💰 Цена: <b>{price:.6f}</b>\n"
                            f"📉 RSI({config.RSI_PERIOD}): <b>{rsi}</b>\n"
                            f"📊 Объем: <b>{volume:,.0f}</b>\n"
                            f"⏰ Таймфрейм: <b>{config.INTERVAL}</b>\n\n"
                            f"🔗 https://www.binance.com/en/futures/{symbol}"
                        )

                        try:
                            await telegram.send_message(text)
                            await db.save(symbol, rsi)

                            sent += 1
                            logger.info(f"Отправлен сигнал: {symbol}")

                        except Exception:
                            logger.exception(f"Ошибка Telegram ({symbol})")

                    elif rsi > 35:

                        if await db.exists(symbol):
                            await db.delete(symbol)
                            removed += 1
                            logger.info(f"Сигнал сброшен: {symbol}")

                elapsed = round(time.time() - started, 2)

                logger.info("-" * 60)
                logger.info(f"Проверено       : {checked}")
                logger.info(f"Новых сигналов  : {sent}")
                logger.info(f"Пропущено       : {skipped}")
                logger.info(f"Сброшено        : {removed}")
                logger.info(f"Время цикла     : {elapsed} сек")
                logger.info("-" * 60)

            except Exception:
                logger.exception("Ошибка во время сканирования")

            await asyncio.sleep(config.CHECK_INTERVAL)


if __name__ == "__main__":
    asyncio.run(main())
