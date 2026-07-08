import asyncio

from app.telegram_client import TelegramClient


async def main():
    telegram = TelegramClient()
    await telegram.send_message("✅ Telegram подключен!")


asyncio.run(main())
