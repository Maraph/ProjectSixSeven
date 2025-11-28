
from flask import Flask
import threading
import time
import yfinance as yf
import requests

app = Flask(__name__)

# ----------------------------
# Pushover credentials
# ----------------------------
token = "a6bmku29c3dgtk7u2pwak17721ab1u"
user = "ux7rirjnno7dkdn3mv4bcfbaky1ior"

EUR = 1.0
USD = 1.16
Conversion_Rate = EUR / USD

def background_loop():
    while True:
        try:
            symbol = yf.Ticker("ALM")
            data = symbol.history(period="1d")
            if not data.empty:
                price = data["Close"].iloc[0] * Conversion_Rate
                message = f"ALM stock price is €{price:.2f}"
                requests.post(
                    "https://api.pushover.net/1/messages.json",
                    data={"token": token, "user": user, "message": message}
                )
                print("Sent notification:", message)
            time.sleep(1800)  # 5 minutes
        except Exception as e:
            print("Error:", e)
            time.sleep(10)

# Start the infinite loop on a background thread
threading.Thread(target=background_loop, daemon=True).start()

@app.route("/")
def home():
    return "Stock notifier running!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
