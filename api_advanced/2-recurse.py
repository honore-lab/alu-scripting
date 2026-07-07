#!/usr/bin/python3
"""Queries the Reddit API recursively to return all hot article titles."""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """Recursively returns titles of all hot articles for a subreddit."""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    params = {'after': after} if after else {}
    
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code != 200:
        return None
        
    data = response.json().get('data', {})
    children = data.get('children', [])
    for post in children:
        hot_list.append(post.get('data', {}).get('title'))
        
    next_page = data.get('after')
    if next_page:
        return recurse(subreddit, hot_list, next_page)
    return hot_list
