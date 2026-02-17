# Global Contest Rank & Score Tracker

A web application to track and monitor competitive programming rankings and scores across platforms like Codeforces.

## Prerequisites
- Python 3.8+
- SQLite (included with Python)

## Installation

1. **Clone the repository** (or navigate to the project folder).
2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Running Locally

1. **Start the Flask server**:
   ```bash
   python app.py
   ```
2. **Access the application**:
   Open your browser and go to `http://127.0.0.1:5000`.

## Features
- **Registration**: Add users by their platform and profile URL.
- **Auto-Fetch**: Automatically retrieves rating, rank, and score from platform APIs.
- **Excel Export**: All data is automatically synchronized with `contest_data.xlsx`.
- **Leaderboard**: View top performers sorted by rating.
- **Scheduler**: Data for all users is updated daily in the background.

## Supported Platforms
- [x] Codeforces (Official API)
- [x] LeetCode (GraphQL API)
- [x] CodeChef (Scraping)
- [x] AtCoder (Kenkoooo API)
- [x] HackerRank (REST API)

## Troubleshooting
- **Invalid Profile URL**: Ensure the URL matches the expected format (e.g., `https://codeforces.com/profile/handle`).
- **Excel Busy**: Close the `contest_data.xlsx` file if it's open in another application before registering new users or downloading.
