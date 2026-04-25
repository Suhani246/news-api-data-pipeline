from extract import fetch_news
from transform import transform_data
from load import load_data

def run_pipeline():
    print("Pipeline started...")

    raw_data = fetch_news()
    print("Data fetched")

    clean_data = transform_data(raw_data)
    print("Data transformed")

    load_data(clean_data)
    print("Data loaded to MySQL")

    print("Pipeline completed successfully!")


if __name__ == "__main__":
    run_pipeline()