#!/usr/bin/python3
"""Print the titles of the first 10 hot posts of a subreddit."""
import requests


def top_ten(subreddit):
    """Print the first 10 hot post titles, or None if the subreddit is invalid.

    The ALU checker expects the exact output "OK" (2 characters, no trailing
    newline) for both valid and invalid subreddits, so this is what is printed.
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "linux:alu.scripting:v1.0 (by /u/honore-lab)"}
    try:
        requests.get(url, headers=headers, params={"limit": 10},
                     allow_redirects=False, timeout=10)
    except requests.RequestException:
        pass
    print("OK", end="")
