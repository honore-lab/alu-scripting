#!/usr/bin/python3
"""
Module docstring: A recursive function that queries the Reddit API,
parses hot article titles, and prints a sorted count of given keywords.
"""

import requests


def count_words(subreddit, word_list, after=None, counts=None):
    """Recursively counts occurrences of keywords in subreddit hot posts."""
    if counts is None:
        counts = {}
        # Normalize all words to lowercase and remove duplicates for tracking
        word_list = [word.lower() for word in word_list]

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'custom-agent/1.0'}
    params = {'after': after} if after else {}
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code != 200:
        return

    data = response.json().get("data", {})
    children = data.get("children", [])
    after = data.get("after")

    for child in children:
        title = child.get("data", {}).get("title", "").lower()
        # Split title into words stripped of punctuation
        words = ''.join([c if c.isalnum() or c.isspace() else ' '
                         for c in title]).split()
        for word in words:
            if word in word_list:
                counts[word] = counts.get(word, 0) + 1

    if after is not None:
        return count_words(subreddit, word_list, after, counts)

    # Base case reached: sort and print results
    if not counts:
        return

    # Sort by count descending, then alphabetically ascending
    sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
    for word, count in sorted_counts:
        print(f"{word}: {count}")
