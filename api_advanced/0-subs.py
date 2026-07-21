#!/usr/init/python3
"""Module for task 0-subs."""

import requests


def number_of_subscribers(subreddit):
    """Query Reddit API for total subscribers."""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "custom-agent/1.0"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        return response.json().get("data", {}).get("subscribers", 0)
    return 0
