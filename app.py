import time

print("Bot Started", flush=True)

# تست import مرحله‌ای
try:
    from telegram_bot import send_message
    print("telegram ok", flush=True)
except Exception as e:
    print("telegram import error:", e, flush=True)
    send_message = None

try:
    from market import get_market_data
    print("market ok", flush=True)
except Exception as e:
    print("market import error:", e, flush=True)

try:
    from filters import apply_filter
    print("filters ok", flush=True)
except Exception as e:
    print("filters import error:", e, flush=True)

# تست تلگرام بدون crash
if send_message:
    try:
        send_message("📡 Bot Started")
    except Exception as e:
        print("telegram send error:", e, flush=True)

while True:
    print("loop alive", flush=True)
    time.sleep(10)
