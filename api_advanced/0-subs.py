#!/usr/bin/python3
"""Queries the Reddit API and returns the number of subscribers."""
import requests


def number_of_subscribers(subreddit):
    """Returns the total subscriber count for a given subreddit, else 0."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)

        # If it redirects (302) or errors out (404, 403), it is invalid
        if response.status_code != 200:
            return 0

        results = response.json()
        if 'data' not in results:
            return 0

        subscribers = results.get('data', {}).get('subscribers')
        if subscribers is None:
            return 0

        return subscribers
    except Exception:
        return 0
