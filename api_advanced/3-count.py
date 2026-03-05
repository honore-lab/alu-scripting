#!/usr/bin/python3
"""
Counts keywords in hot article titles
"""
import requests


def count_words(subreddit, word_list, after=None, counts=None):
    """Recursive keyword counter"""
    if counts is None:
        counts = {}

    headers = {"User-Agent": "HonoreAPI/1.0"}

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)

    params = {"after": after}

    res = requests.get(url, headers=headers, params=params,
                       allow_redirects=False)

    if res.status_code != 200:
        return

    data = res.json().get("data")

    posts = data.get("children")

    for post in posts:
        title = post.get("data").get("title").lower().split()

        for word in word_list:
            w = word.lower()
            counts[w] = counts.get(w, 0) + title.count(w)

    after = data.get("after")

    if after is not None:
        return count_words(subreddit, word_list, after, counts)

    sorted_words = sorted(counts.items(),
                          key=lambda x: (-x[1], x[0]))

    for word, count in sorted_words:
        if count > 0:
            print("{}: {}".format(word, count))