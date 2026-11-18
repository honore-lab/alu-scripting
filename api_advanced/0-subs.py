#!/usr/bin/python3
"""Query the Reddit API for the number of subscribers of a subreddit."""
import requests


def number_of_subscribers(subreddit):
    """Return the total subscribers of a subreddit, or 0 if it is invalid."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "linux:alu.scripting:v1.0 (by /u/honore-lab)"}
    try:
        res = requests.get(url, headers=headers, allow_redirects=False,
                           timeout=10)
        if res.status_code != 200:
            return 0
        data = res.json().get("data", {})
    except (requests.RequestException, ValueError):
        return 0
    return data.get("subscribers") or 0
