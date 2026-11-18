#!/usr/bin/python3
"""Recursively collect the titles of all hot posts of a subreddit."""
import requests


def recurse(subreddit, hot_list=None, after=None):
    """Return a list of all hot post titles, or None if nothing is found."""
    if hot_list is None:
        hot_list = []
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "linux:alu.scripting:v1.0 (by /u/honore-lab)"}
    params = {"limit": 100, "after": after}
    try:
        res = requests.get(url, headers=headers, params=params,
                           allow_redirects=False, timeout=10)
        if res.status_code != 200:
            return hot_list or None
        data = res.json().get("data", {})
    except (requests.RequestException, ValueError):
        return hot_list or None
    for child in data.get("children", []):
        hot_list.append(child.get("data", {}).get("title"))
    next_page = data.get("after")
    if next_page:
        return recurse(subreddit, hot_list, next_page)
    return hot_list or None
