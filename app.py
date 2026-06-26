import time
from telegram_bot import send_message
from market import get_market_data
from filters import apply_filter

print("Bot Started", flush=True)
send_message("📡 Bot Started")

while True:
    print("STEP 1: getting data", flush=True)

    data = get_market_data()
    print("DATA LEN:", len(data), flush=True)

    count = 0

    for item in data:
        result = apply_filter(item)

        if result:
            count += 1
            print("SIGNAL:", result, flush=True)

            send_message(f"{result['symbol']} → {result['score']}")

    print("TOTAL SIGNALS:", count, flush=True)

    time.sleep(60)
