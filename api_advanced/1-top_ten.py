#!/usr/bin/python3
"""Module for task 1-top_ten."""
import requests


def top_ten(subreddit):
    """Print the first 10 hot posts for a given subreddit."""
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {'User-Agent': 'custom-agent/1.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        print(None)
        return
    try:
        results = response.json().get("data", {}).get("children", [])
        if not results:
            print(None)
            return
        for post in results:
            print(post.get("data", {}).get("title"))
    except Exception:
        print(None)
