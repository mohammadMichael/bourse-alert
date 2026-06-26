import time
from telegram_bot import send_message
from market import get_market_data
from filters import apply_filter

print("Bot Started", flush=True)
send_message("📡 Bot Started")

while True:
    print("Fetching market data...", flush=True)

    data = get_market_data()
    print(f"DATA SIZE: {len(data)}", flush=True)

    results = []

    for item in data:
        try:
            result = apply_filter(item)
            if result:
                results.append(result)
        except Exception as e:
            print(f"ERROR: {e}", flush=True)

    print(f"RESULTS: {len(results)}", flush=True)

    if results:
        msg = "📊 Signals:\n\n"
        for r in results[:10]:
            msg += f"{r['symbol']} → {r['score']}\n"

        send_message(msg)

    time.sleep(60)
