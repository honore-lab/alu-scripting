#!/usr/bin/python3
"""Queries the Reddit API and returns the number of subscribers."""
import requests


def number_of_subscribers(subreddit):
    """Returns the total subscriber count for a given subreddit, else 0."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)

        # Catch normal errors or redirects instantly
        if response.status_code in [302, 404, 403, 500]:
            return 0

        data = response.json()
        if not isinstance(data, dict):
            return 0

        sub_count = data.get('data', {}).get('subscribers', 0)
        return sub_count if sub_count is not None else 0

    except Exception:
        return 0
