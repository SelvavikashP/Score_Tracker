import pandas as pd
import os
from datetime import datetime

EXCEL_FILE = "contest_data.xlsx"

def update_excel(users):
    """
    Appends or updates user data in the Excel file.
    """
    data = []
    for user in users:
        data.append({
            "Name": user.name,
            "Platform": user.platform,
            "Rating": user.rating,
            "Rank": user.rank,
            "Global/Last Contest Rank": user.global_rank,
            "Country Rank": user.country_rank,
            "Problems Solved": user.recent_problems,
            "Total Contests": user.total_contests,
            "Date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })
    
    df_new = pd.DataFrame(data)
    
    try:
        df_new.to_excel(EXCEL_FILE, index=False)
    except Exception as e:
        print(f"Error updating Excel: {e}")

def get_excel_path():
    return os.path.abspath(EXCEL_FILE)
