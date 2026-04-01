import os
import time
from datetime import datetime
from playsound import playsound
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from webdriver_manager.chrome import ChromeDriverManager

SOUND_FILE = os.path.join(os.path.dirname(__file__), "faa.mp3")


def create_driver():
    service = Service(ChromeDriverManager().install())
    return webdriver.Chrome(service=service)


def is_booking_available(driver, url):
    """
    Check if booking is available for the date in the URL.

    BMS always loads the nearest available date as selected. The selected
    date element has id in YYYYMMDD format. We compare that id with the
    date in the URL — if they match, booking is open for that date.

    Args:
        driver : Selenium WebDriver instance
        url    : BookMyShow buytickets URL ending in YYYYMMDD e.g. .../20260403

    Returns:
        True if booking is open for the requested date, False otherwise
    """
    requested_date = url.strip("/").split("/")[-1]  # e.g. "20260403"

    driver.get(url)

    try:
        # Wait until at least one date element with a YYYYMMDD id is present
        WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.XPATH, f"//*[@id='{requested_date}']"))
        )

        # Use JS to find which date element is active by checking background color
        # All date elements have 8-digit numeric ids (YYYYMMDD format)
        selected_date = driver.execute_script("""
            const els = document.querySelectorAll('[id]');
            for (const el of els) {
                if (/^\\d{8}$/.test(el.id)) {
                    const bg = window.getComputedStyle(el).backgroundColor;
                    // Active date has a colored (non-transparent) background
                    if (bg && bg !== 'rgba(0, 0, 0, 0)' && bg !== 'rgb(255, 255, 255)') {
                        return el.id;
                    }
                }
            }
            return null;
        """)

        print(f"Requested: {requested_date}, Active on page: {selected_date}")
        return selected_date == requested_date

    except TimeoutException:
        print("Page did not load in time")
        return False


if __name__ == "__main__":
    print("Example URL: https://in.bookmyshow.com/movies/bengaluru/project-hail-mary/buytickets/ET00481564/20260403")
    url = input("Enter BookMyShow URL: ").strip()

    while True:
        print(f"\n[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Checking availability...")
        driver = create_driver()
        try:
            available = is_booking_available(driver, url)
        finally:
            driver.quit()

        print(f"Booking available: {available}")

        if available:
            playsound(SOUND_FILE)
            print("Replaying in 10 mins...")
            time.sleep(600)
        else:
            print("Retrying in 30 mins...")
            time.sleep(1800)
