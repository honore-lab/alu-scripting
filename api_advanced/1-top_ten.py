#!/usr/bin/python3
"""Module for task 1-top_ten."""
import requests


def top_ten(subreddit):
    """Print the first 10 hot posts for a given subreddit."""
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {'User-Agent': 'alu-student:v1.0'}
    response = requests.get(url, headers=headers, params={'raw_json': 1})
    if response.status_code != 200:
        print(None)
        return
    try:
        data = response.json().get("data", {})
        children = data.get("children", [])
        if not children:
            print(None)
            return
        for post in children:
            print(post.get("data", {}).get("title"))
    except Exception:
        print(None)
