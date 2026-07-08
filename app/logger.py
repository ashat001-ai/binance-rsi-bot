import logging
import os

os.makedirs("logs", exist_ok=True)

logger = logging.getLogger("scanner")
logger.setLevel(logging.INFO)

formatter = logging.Formatter(
    "%(asctime)s | %(levelname)s | %(message)s"
)

console = logging.StreamHandler()
console.setFormatter(formatter)

file = logging.FileHandler("logs/bot.log")
file.setFormatter(formatter)

logger.addHandler(console)
logger.addHandler(file)
