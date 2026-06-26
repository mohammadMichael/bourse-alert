import time
from telegram_bot import send_message

print("Bourse Bot Started", flush=True)

send_message("📡 Bot Started Successfully")

while True:
    print("alive...", flush=True)
    time.sleep(10)
