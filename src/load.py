import os
from dotenv import load_dotenv
from sqlalchemy import create_engine

load_dotenv()

def load_data(df):
    if df.empty:
       print("No data to load")
    return
    # Get DB credentials from .env
    username = os.getenv("DB_USER")
    password = os.getenv("DB_PASSWORD")
    host = os.getenv("DB_HOST")
    database = os.getenv("DB_NAME")

    # Create MySQL connection
    engine = create_engine(
        f"mysql+pymysql://{username}:{password}@{host}/{database}"
    )

    # Step 1 — Remove duplicates
    df.drop_duplicates(subset=["title"], inplace=True)

    # Step 2 — Save to CSV 
    try:
        df.to_csv("news_data.csv", mode='a', index=False, header=False)
        print("Data saved to CSV")
    except Exception as e:
        print(" CSV Error:", e)

    # Step 3 — Save to MySQL 
    try:
        df.to_sql("news", con=engine, if_exists="append", index=False)
        print("Data inserted into MySQL")
    except Exception as e:
        print("MySQL Error:", e)