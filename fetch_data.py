import requests
import pandas as pd
import os

API_KEY = "93d3d9634aac4a5c82ac95240946c384ne"
API_URL = f"https://newsapi.org/v2/everything?q=stock market&sortBy=publishedAt&pageSize=100&apiKey={API_KEY}"

csv_path = "/Users/opium/ai_data_project/stock_market_news.csv"

# Fetch latest stock market news
response = requests.get(API_URL)
data = response.json()

if "articles" in data and data["articles"]:
    df = pd.DataFrame(data["articles"])
    expected_columns = {"title", "description", "url", "publishedAt"}

    if expected_columns.issubset(df.columns):
        df = df[["title", "description", "url", "publishedAt"]]

        # Convert 'publishedAt' to datetime for sorting
        df["publishedAt"] = pd.to_datetime(df["publishedAt"])

        # Append new data without duplicates
        if os.path.exists(csv_path):
            existing_df = pd.read_csv(csv_path)
            existing_df["publishedAt"] = pd.to_datetime(existing_df["publishedAt"])
        else:
            existing_df = pd.DataFrame()

        combined_df = pd.concat([existing_df, df]).drop_duplicates(subset=["url"]).sort_values(by="publishedAt", ascending=False)

        # Save back to CSV
        combined_df.to_csv(csv_path, index=False)
        print(f"Fetched {len(df)} fresh stock market news articles and updated {csv_path} without duplicates!")
    else:
        print("Error: Expected columns not found.")
else:
    print("Error: No stock market articles found or API response is invalid.", data)