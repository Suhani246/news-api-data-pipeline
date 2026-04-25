import os
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()

def analyze_data():
    username = os.getenv("DB_USER")
    password = os.getenv("DB_PASSWORD")
    host = os.getenv("DB_HOST")
    database = os.getenv("DB_NAME")

    engine = create_engine(
        f"mysql+pymysql://{username}:{password}@{host}/{database}"
    )

    df = pd.read_sql("SELECT * FROM news", con=engine)

    print(" Total Articles:", len(df))

    print("\n Articles per day:")
    print(df['published_at'].dt.date.value_counts())

    print("\n Top Sources:")
    print(df['source'].value_counts().head(5))


# 🔥 THIS LINE WAS MISSING
if __name__ == "__main__":
    analyze_data()