import os
import json
import time
import logging
import requests
from typing import List, Dict

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Load config from environment or config.json fallback
AIRTABLE_API_KEY = os.getenv("AIRTABLE_TOKEN_KEY")

def load_config_fallback():
    try:
        with open("config.json") as f:
            config = json.load(f)
            return config
    except FileNotFoundError:
        logging.error("No environment variables or config file found.")
        return {}

if not AIRTABLE_API_KEY:
    config = load_config_fallback()
    AIRTABLE_API_KEY = AIRTABLE_API_KEY or config.get("AIRTABLE_TOKEN_KEY")
    AIRTABLE_BASE_ID = config.get("AIRTABLE_BASE_ID")
    AIRTABLE_TABLE_NAME = config.get("AIRTABLE_TABLE_NAME")
else:
    AIRTABLE_BASE_ID = os.getenv("AIRTABLE_BASE_ID")
    AIRTABLE_TABLE_NAME = os.getenv("AIRTABLE_TABLE_NAME")

HEADERS = {
    "Authorization": f"Bearer {AIRTABLE_API_KEY}",
    "Content-Type": "application/json"
}

def fetch_airtable_records() -> List[Dict]:
    url = f"https://api.airtable.com/v0/{AIRTABLE_BASE_ID}/{AIRTABLE_TABLE_NAME}"
    response = requests.get(url, headers=HEADERS)
    if response.status_code == 200:
        records = response.json().get("records", [])
        logging.info(f"Fetched {len(records)} records from Airtable.")
        return records
    else:
        logging.error(f"Failed to fetch records: {response.status_code} - {response.text}")
        return []

def simulate_swapcard_sync(records: List[Dict]):
    for record in records:
        name = record.get("fields", {}).get("Name", "Unnamed")
        email = record.get("fields", {}).get("Email", "NoEmail@example.com")
        logging.info(f"Syncing attendee '{name}' ({email}) to Swapcard...")
        time.sleep(0.2)
    logging.info("Swapcard sync simulation complete.")

def sync_back_to_airtable():
    logging.info("Simulating updated data from Swapcard to Airtable...")
    logging.info("Update: Marked 'CheckedIn = True' for record ID rec12345 (simulated).")

def main():
    logging.info("Starting Airtable <> Swapcard 2-way sync simulation...")
    records = fetch_airtable_records()
    if records:
        simulate_swapcard_sync(records)
        sync_back_to_airtable()
    else:
        logging.warning("No records to sync.")

if __name__ == "__main__":
    main()
