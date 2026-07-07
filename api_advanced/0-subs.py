#!/usr/bin/python3
"""Queries the Reddit API and returns the number of subscribers."""
import requests


def number_of_subscribers(subreddit):
    """Returns the total subscriber count for a given subreddit, else 0."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        return response.json().get('data', {}).get('subscribers', 0)
    return 0
