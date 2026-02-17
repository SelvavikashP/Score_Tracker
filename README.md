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
## Live Output Preview

Below is a representation of how the dashboard looks when tracking top competitive programmers.

| #Rank | User | Platform | Rating / Rank | Problems Solved | Total Contests |
| :---: | :--- | :--- | :--- | :---: | :---: |
| #1 | **Gennady Korotkevich** | `Codeforces` | **3592** (LGM) | 670 | 297 |
| #2 | **tourist** | `AtCoder` | **3782** | 450 | 139 |
| #3 | **sids** | `LeetCode` | **2200** (Guardian) | 1240 | 45 |
| #4 | **vjudge_user** | `CodeChef` | **2450** (6★) | 320 | 88 |

> [!TIP]
> Information is updated in real-time across all platforms. The "Problems Solved" column tracks unique problems solved, and "Global Ranking" shows the user's standing in the last contest or historically.

---
© 2024 Global Score Tracker. All rights reserved.
