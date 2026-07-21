#!/usr/bin/python3
"""
Module docstring: A function that queries the Reddit API and returns
the number of subscribers for a given subreddit.
"""

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
