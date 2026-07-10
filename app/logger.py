import logging
import os

from logging.handlers import RotatingFileHandler

os.makedirs("logs", exist_ok=True)

logger = logging.getLogger("scanner")
logger.setLevel(logging.INFO)

formatter = logging.Formatter(
    "%(asctime)s | %(levelname)s | %(message)s"
)

console = logging.StreamHandler()
console.setFormatter(formatter)

file_handler = RotatingFileHandler(
    "logs/bot.log",
    maxBytes=10 * 1024 * 1024,
    backupCount=5,
    encoding="utf-8",
)

file_handler.setFormatter(formatter)

logger.addHandler(console)
logger.addHandler(file_handler)
