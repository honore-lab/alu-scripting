#!/usr/bin/python3
"""
Recursive function to get all hot post titles
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """Recursively collect titles"""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)

    headers = {"User-Agent": "HonoreAPI/1.0"}

    params = {
        "after": after
    }

    res = requests.get(url, headers=headers, params=params,
                       allow_redirects=False)

    if res.status_code != 200:
        return None

    data = res.json().get("data")

    posts = data.get("children")

    for post in posts:
        hot_list.append(post.get("data").get("title"))

    after = data.get("after")

    if after is None:
        return hot_list

    return recurse(subreddit, hot_list, after)