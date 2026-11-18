#!/usr/bin/python3
"""Recursively count keywords in the titles of a subreddit's hot posts."""
import requests


def get_page(subreddit, after):
    """Return the data of one page of hot posts, or {} on any failure."""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "linux:alu.scripting:v1.0 (by /u/honore-lab)"}
    params = {"limit": 100, "after": after}
    try:
        res = requests.get(url, headers=headers, params=params,
                           allow_redirects=False, timeout=10)
        if res.status_code != 200:
            return {}
        return res.json().get("data", {})
    except (requests.RequestException, ValueError):
        return {}


def count_words(subreddit, word_list, after=None, counts=None):
    """Print a sorted count of keywords found in the hot post titles."""
    if counts is None:
        counts = {}
    data = get_page(subreddit, after)
    for child in data.get("children", []):
        title = child.get("data", {}).get("title") or ""
        for token in title.lower().split():
            counts[token] = counts.get(token, 0) + 1
    next_page = data.get("after")
    if next_page:
        return count_words(subreddit, word_list, next_page, counts)
    wanted = {}
    for word in word_list:
        key = word.lower()
        wanted[key] = wanted.get(key, 0) + 1
    results = {}
    for key, times in wanted.items():
        total = counts.get(key, 0) * times
        if total > 0:
            results[key] = total
    for key, total in sorted(results.items(), key=lambda kv: (-kv[1], kv[0])):
        print("{}: {}".format(key, total))
