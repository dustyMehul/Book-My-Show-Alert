# Book My Show Alert

Get notified when movie tickets become available on BookMyShow.

When booking opens for your requested date, it plays the **faa sound** alert and sends a **Telegram message**. It keeps polling until tickets are found — retrying every 30 minutes if not available, and replaying the alert every 10 minutes once found.

## How it works

BookMyShow always redirects to the nearest available date if the requested date isn't open yet. The script detects this by comparing the active (highlighted) date on the page with the date in the URL — if they match, booking is open.

## Setup

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Telegram Notifications (optional)

Get a Telegram message on your phone the moment booking opens.

### Step 1 — Create a Telegram bot

1. Open Telegram and search for **@BotFather**
2. Send `/newbot` and follow the prompts (pick any name and username)
3. BotFather will give you a token like `123456789:ABCDefgh...` — copy it

### Step 2 — Get your Chat ID

1. Search for **@userinfobot** on Telegram and start it
2. It will immediately reply with your user info — copy the **Id** number (e.g. `987654321`)

### Step 3 — Configure your `.env` file

Copy the example file and fill in your values:

```bash
cp .env.example .env
```

Open `.env` and set:

```
TELEGRAM_BOT_TOKEN=123456789:ABCDefgh...
TELEGRAM_CHAT_ID=987654321
```

### Step 4 — Test it

Start the script and you should receive a "Started monitoring" message on Telegram immediately. When booking opens, you'll get another message with the URL.

> **Note:** `.env` is gitignored — your credentials will never be committed.

## Usage

```bash
python check_availability.py
```

You'll be prompted to enter a BookMyShow URL:

```
Example URL: https://in.bookmyshow.com/movies/bengaluru/project-hail-mary/buytickets/ET00481564/20260403
Enter BookMyShow URL:
```

The date at the end of the URL (`20260403`) is the date you want to check booking for.

## Files

- `check_availability.py` — main script
- `notifier.py` — Telegram notification helper
- `faa.mp3` — alert sound played when booking is found
- `.env.example` — template for Telegram credentials

## Requirements

- Python 3.8+
- Google Chrome installed
- ChromeDriver is auto-managed via `undetected-chromedriver`
