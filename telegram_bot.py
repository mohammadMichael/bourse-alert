import requests

BOT_TOKEN = "توکن_اینجا"
CHAT_ID = "چت_آیدی_اینجا"


def send_message(text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {
        "chat_id": CHAT_ID,
        "text": text
    }
    requests.post(url, data=data)
