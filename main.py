import requests
import time

BOT_TOKEN = "7107877908:AAFHyeZX1p1775HLixLcYyK7f0oVu22psAc"
CHAT_ID = "1003326346"

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": message}
    response = requests.post(url, data=data)
    return response.json()

def track_nifty():
    # Dummy NIFTY price simulation
    nifty_price = 22450  # Simulated data
    message = f"NIFTY Tracker Update: Current Price = {nifty_price}"
    send_telegram_message(message)

if __name__ == "__main__":
    send_telegram_message("Telegram Auto Alert System Started")
    while True:
        track_nifty()
        time.sleep(300)  # 5 minutes
