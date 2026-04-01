import os
import requests
from dotenv import load_dotenv

load_dotenv()

_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")


def send_telegram(message: str) -> None:
    if not _BOT_TOKEN or not _CHAT_ID:
        print("[Telegram] Skipping — BOT_TOKEN or CHAT_ID not set in .env")
        return

    try:
        url = f"https://api.telegram.org/bot{_BOT_TOKEN}/sendMessage"
        response = requests.get(url, params={"chat_id": _CHAT_ID, "text": message}, timeout=10)
        if not response.ok:
            print(f"[Telegram] Failed to send message: {response.text}")
    except Exception as e:
        print(f"[Telegram] Error: {e}")
