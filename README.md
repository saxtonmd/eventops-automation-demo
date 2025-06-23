
# EventOps Automation Demo

This is a demonstration Python script that simulates syncing event attendee data between Airtable and a second platform (e.g., Swapcard). The goal is to showcase a lightweight automation that could support event operations tasks using real data structures and API calls (or simulations thereof).

## 1. Prerequisites

- Python 3.x installed
- An Airtable account with a base and table set up for event attendees
- A personal access token (not an API key) with access to your Airtable workspace
- Git installed if you're cloning or pushing changes
- `requests` library installed

## 2. Install dependencies

From your terminal, install the required library:

```bash
pip install requests
```

## 3. Set up your config file

Create a file named `config.json` in the root directory with the following structure:

```json
{
  "AIRTABLE_TOKEN_KEY": "your_airtable_personal_access_token",
  "BASE_ID": "your_base_id",
  "TABLE_NAME": "Event Attendees"
}
```

> ⚠️ Replace the placeholder values with your actual Airtable token, base ID, and table name.

## 4. Run the script

Run the following command in the terminal:

```bash
python airtable_sync_demo.py
```

You should see a log output showing a simulated sync of attendee data.

## 5. File structure

```
.
├── airtable_sync_demo.py     # Main Python script
├── config.json               # Local configuration file with token and base info
├── README.md                 # This file
└── LICENSE                   # Optional license file
```

## 6. Notes

- This is a demonstration only — Swapcard is simulated.
- Ensure your Airtable base includes sample records in the correct table.
- This repo uses `.gitignore` to prevent your config file from being accidentally committed. Keep your token private.

## License

MIT License

![image](https://github.com/user-attachments/assets/1e60eae2-bbd5-4197-bdb1-9cf3e05b03bc)
