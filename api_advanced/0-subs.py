#!/usr/bin/python3
"""Queries the Reddit API and returns the number of subscribers."""
import requests


def number_of_subscribers(subreddit):
    """Returns the total subscriber count for a given subreddit, else 0."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

    response = requests.get(url, headers=headers, allow_redirects=False)

    # If the subreddit is invalid, it will return a redirect (302) or error (404)
    if response.status_code != 200:
        return 0

    try:
        data = response.json().get('data', {})
        subscribers = data.get('subscribers')

        if subscribers is None:
            return 0

        return subscribers
    except Exception:
        return 0
