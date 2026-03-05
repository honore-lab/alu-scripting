#!/usr/bin/python3
"""Return the number of subscribers of a subreddit."""
import requests


def number_of_subscribers(subreddit):
    """Query Reddit API and return subscriber count."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)

    headers = {
        "User-Agent": "alu-api-project"
    }

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        return 0

    results = response.json().get("data")

    return results.get("subscribers")