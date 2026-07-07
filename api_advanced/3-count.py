#!/usr/bin/python3
"""Recursively counts keywords within hot article titles from Reddit."""
import requests


def count_words(subreddit, word_list, after=None, counts={}):
    """Recursively parses hot titles and counts specified keywords."""
    if not counts:
        for word in word_list:
            counts[word.lower()] = 0

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    params = {'after': after} if after else {}

    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code != 200:
        return

    data = response.json().get('data', {})
    children = data.get('children', [])

    for post in children:
        title = post.get('data', {}).get('title', '').lower().split()
        for word in title:
            # Clean symbols off the word boundaries
            cleaned = word.strip('!. _')
            if cleaned in counts:
                counts[cleaned] += 1

    next_page = data.get('after')
    if next_page:
        return count_words(subreddit, word_list, next_page, counts)

    # Sort results once complete
    sorted_words = sorted(counts.items(), key=lambda kv: (-kv[1], kv[0]))
    for word, count in sorted_words:
        if count > 0:
            print("{}: {}".format(word, count))
