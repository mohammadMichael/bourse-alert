import requests

BOT_TOKEN = "8682677437:AAGLa5uwyFFD3quE23kjhREeJWuw7GuaZV4"
CHAT_ID = "37309327"


def send_message(text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {
        "chat_id": CHAT_ID,
        "text": text
    }
    requests.post(url, data=data)
