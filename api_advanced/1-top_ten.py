#!/usr/bin/python3
"""Queries the Reddit API and prints titles of the first 10 hot posts."""
import requests


def top_ten(subreddit):
    """Prints the titles of the top 10 hot posts for a given subreddit."""
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json().get('data', {})
            children = data.get('children', [])
            if not children or children is None:
                print(None)
                return
            for post in children:
                print(post.get('data', {}).get('title'))
        else:
            print(None)
    except Exception:
        print(None)
