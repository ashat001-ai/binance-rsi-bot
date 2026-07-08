import aiohttp
from app.config import config


class TelegramClient:

    def __init__(self):
        self.url = f"https://api.telegram.org/bot{config.BOT_TOKEN}"

    async def send_message(self, text):

        async with aiohttp.ClientSession() as session:

            async with session.post(
                f"{self.url}/sendMessage",
                json={
                    "chat_id": config.CHAT_ID,
                    "text": text,
                    "parse_mode": "HTML"
                }
            ) as response:

                if response.status != 200:
                    print(await response.text())
