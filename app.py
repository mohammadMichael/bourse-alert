import time

print("APP STARTED", flush=True)

try:
    from market import get_market_data
    print("MARKET IMPORT OK", flush=True)
except Exception as e:
    print("MARKET IMPORT FAILED:", e, flush=True)

while True:
    print("loop alive", flush=True)
    time.sleep(10)
