#!/usr/bin/python3
"""Module for task 3-count."""

import requests


def count_words(subreddit, word_list, after=None, counts=None):
    """Recursively count keyword occurrences in hot articles."""
    if counts is None:
        counts = {}
        word_list = [w.lower() for w in word_list]
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "custom-agent/1.0"}
    params = {"after": after} if after else {}
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code != 200:
        return
    data = response.json().get("data", {})
    for child in data.get("children", []):
        title = child.get("data", {}).get("title", "").lower()
        words = "".join([c if c.isalnum() or c.isspace() else " "
                         for c in title]).split()
        for word in words:
            if word in word_list:
                counts[word] = counts.get(word, 0) + 1
    after = data.get("after")
    if after:
        return count_words(subreddit, word_list, after, counts)
    if not counts:
        return
    for word, count in sorted(counts.items(), key=lambda x: (-x[1], x[0])):
        print(f"{word}: {count}")
