# Book My Show Alert

Get notified when movie tickets become available on BookMyShow.

When booking opens for your requested date, it plays the **faa sound** alert. It keeps polling until tickets are found — retrying every 30 minutes if not available, and replaying the alert every 10 minutes once found.

## How it works

BookMyShow always redirects to the nearest available date if the requested date isn't open yet. The script detects this by comparing the active (highlighted) date on the page with the date in the URL — if they match, booking is open.

## Setup

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

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
- `faa.mp3` — alert sound played when booking is found

## Requirements

- Python 3.8+
- Google Chrome installed
- ChromeDriver is auto-managed via `webdriver-manager`
