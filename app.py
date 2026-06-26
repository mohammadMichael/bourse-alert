import time
from telegram_bot import send_message
from market import get_market_data
from filters import apply_filter

print("BOT STARTED", flush=True)
send_message("📡 Bot Started")

while True:
    data = get_market_data()

    print("DATA LEN:", len(data), flush=True)

    found = 0

    for item in data:
        result = apply_filter(item)

        if result:
            found += 1
            print("SIGNAL:", result, flush=True)
            send_message(f"{result['symbol']} → {result['score']}")

    print("FOUND SIGNALS:", found, flush=True)

    time.sleep(60)
