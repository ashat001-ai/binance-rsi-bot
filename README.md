# Binance RSI Scanner

Telegram-бот для поиска перепроданных монет на Binance Futures.

## Возможности

- RSI(14) по закрытой свече.
- Binance Futures.
- Telegram-уведомления.
- Защита от повторных сигналов.
- SQLite.
- Логирование.
- Автозапуск через systemd.

## Установка

```bash
git clone https://github.com/ashat001-ai/binance-rsi-bot.git
cd binance-rsi-bot

python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt
```

## Настройка

Создай файл `.env`:

```env
BOT_TOKEN=your_token
CHAT_ID=your_chat_id
```

## Запуск

```bash
python run.py
```

## Запуск как сервис

```bash
sudo systemctl enable binance-rsi-bot
sudo systemctl start binance-rsi-bot
sudo systemctl status binance-rsi-bot
```

## Версия

v1.0.0 Stable
