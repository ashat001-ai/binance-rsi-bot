from dataclasses import dataclass
from dotenv import load_dotenv
import os

load_dotenv()

@dataclass
class Config:
    BINANCE_URL = "https://fapi.binance.com"

    INTERVAL = "1h"
    RSI_PERIOD = 14
    RSI_LEVEL = 30
    RSI_RESET = 35

    KLINES_LIMIT = 200

    CHECK_INTERVAL = 60

    BOT_TOKEN = os.getenv("BOT_TOKEN")
    CHAT_ID = os.getenv("CHAT_ID")

    DB_PATH = "data/bot.db"

config = Config()
