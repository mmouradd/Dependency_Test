"""
Fetches data from a public API.
"""

import requests

from src.config import API_TIMEOUT


def fetch_data():
    """Fetch a list of sample posts from a public JSON API."""
    url = "https://jsonplaceholder.typicode.com/posts"
    try:
        response = requests.get(url, timeout=API_TIMEOUT)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Fetch failed, using fallback data. ({e})")
        return [
            {"userId": 1, "id": 1, "title": "sample title", "body": "sample body"},
            {"userId": 2, "id": 2, "title": "another title", "body": "another body"},
        ]
