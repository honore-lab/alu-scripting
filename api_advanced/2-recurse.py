#!/usr/bin/python3
"""
Module docstring: A recursive function that queries the Reddit API and
returns a list containing the titles of all hot articles for a given subreddit.
"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """Recursively fetches all hot article titles for a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'custom-agent/1.0'}
    params = {'after': after} if after else {}
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code != 200:
        return None

    data = response.json().get("data", {})
    children = data.get("children", [])
    after = data.get("after")

    for child in children:
        hot_list.append(child.get("data", {}).get("title"))

    if after is not None:
        return recurse(subreddit, hot_list, after)
    return hot_list
