import time
from telegram_bot import send_message
from market import get_market_data
from filters import apply_filter

print("BOT STARTED", flush=True)
send_message("📡 Bot Started")

while True:
    print("GET DATA", flush=True)

    data = get_market_data()
    print("DATA LEN:", len(data), flush=True)

    for item in data:
        result = apply_filter(item)

        print("RESULT:", result, flush=True)

        if result:
            send_message(f"{result['symbol']} → {result['score']}")

    time.sleep(30)
