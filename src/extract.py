import os
import requests
import random
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")

def fetch_news():
    print(" Fetching news from API...")

    url = "https://api.thenewsapi.com/v1/news/all"

    topics = ["technology", "business", "sports", "health"]
    all_articles = []

    for page in range(1, 2):
        params = {
            "api_token": API_KEY,
            "language": "en",
            "limit": 5,
            "page": page,
            "search": random.choice(topics),
            "sort": "published_desc"
        }

        response = requests.get(url, params=params)
        print(f"📡 Page {page} Status:", response.status_code)

        if response.status_code != 200:
            if response.status_code == 402:
                print(" API limit reached. Skipping fetch.")
                return {"data": []}
            else:
                print(f" API Error: {response.status_code}")
                return {"data": []}

        data = response.json()
        articles = data.get("data", [])
        all_articles.extend(articles)

    print(f" Total articles fetched: {len(all_articles)}")

    return {"data": all_articles}