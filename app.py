import time
from telegram_bot import send_message
from market import get_market_data
from filters import apply_filter

print("BOT STARTED", flush=True)
send_message("📡 Bot Started")

while True:
    data = get_market_data()

    for item in data:
        result = apply_filter(item)

        if result:
            send_message(f"{result['symbol']} → {result['score']}")

    time.sleep(60)
