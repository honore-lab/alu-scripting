#!/usr/bin/python3
"""Module to query Reddit API for subreddit subscribers."""

import requests


def number_of_subscribers(subreddit):
    """Queries Reddit API and returns total subscribers for a subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'custom-agent/1.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        return data.get("data", {}).get("subscribers", 0)
    return 0
