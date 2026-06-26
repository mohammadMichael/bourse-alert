import time
from telegram_bot import send_message
from market import get_market_data
from filters import apply_filter

print("Bot Started", flush=True)

send_message("📡 Bot Started")

while True:
    data = get_market_data()

    results = []

    for item in data:
        result = apply_filter(item)
        if result:
            results.append(result)

    if results:
        msg = "📊 سیگنال‌ها:\n\n"
        for r in results:
            msg += f"{r['symbol']} → {r['score']}\n"

        send_message(msg)

    time.sleep(600)  # هر 10 دقیقه
