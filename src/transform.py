import pandas as pd

def transform_data(raw_data):
    data = raw_data.get("data", [])

    # 🔥 Handle empty API response
    if not data:
        print("⚠️ No data received from API")
        return pd.DataFrame()

    df = pd.DataFrame(data)

    # ✅ Only convert if column exists
    if "published_at" in df.columns:
        df["published_at"] = pd.to_datetime(df["published_at"])

    return df