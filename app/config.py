import os
import sys
from dataclasses import dataclass

from dotenv import load_dotenv

load_dotenv()


@dataclass(frozen=True)
class Config:
    VERSION = "1.0.0"

    BASE_URL = os.getenv("BASE_URL", "https://fapi.binance.com")

    INTERVAL = os.getenv("INTERVAL", "1h")
    LIMIT = int(os.getenv("LIMIT", "200"))

    RSI_PERIOD = int(os.getenv("RSI_PERIOD", "14"))
    RSI_LEVEL = float(os.getenv("RSI_LEVEL", "30"))

    CHECK_INTERVAL = int(os.getenv("CHECK_INTERVAL", "60"))

    REQUEST_TIMEOUT = int(os.getenv("REQUEST_TIMEOUT", "15"))

    BOT_TOKEN = os.getenv("BOT_TOKEN")
    CHAT_ID = os.getenv("CHAT_ID")


config = Config()


def validate_config():
    errors = []

    if not config.BOT_TOKEN:
        errors.append("BOT_TOKEN")

    if not config.CHAT_ID:
        errors.append("CHAT_ID")

    if errors:
        print("\n========================================")
        print(" CONFIGURATION ERROR")
        print("========================================")
        for item in errors:
            print(f"Missing: {item}")
        print("Please check your .env file.")
        print("========================================\n")
        sys.exit(1)
