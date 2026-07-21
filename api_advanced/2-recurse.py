#!/usr/bin/python3
"""Module for task 2-recurse."""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """Recursively return all hot article titles for a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "custom-agent/1.0"}
    params = {"after": after} if after else {}
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code != 200:
        return None
    data = response.json().get("data", {})
    for child in data.get("children", []):
        hot_list.append(child.get("data", {}).get("title"))
    after = data.get("after")
    if after:
        return recurse(subreddit, hot_list, after)
    return hot_list
