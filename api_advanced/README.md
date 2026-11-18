# alu-scripting / api_advanced

Python scripts that query the Reddit API using the `requests` module.

## Learning Objectives

- How to read API documentation to find the endpoints you need
- How to use an API with pagination
- How to parse JSON results from an API
- How to make a recursive API call
- How to sort a dictionary by value

## Requirements

- Python 3 on Ubuntu 14.04 LTS, `requests` module for all HTTP calls
- PEP 8 style, imports in alphabetical order
- Every file starts with `#!/usr/bin/python3`, ends with a new line and is executable
- Every module has a docstring
- Redirects are never followed, so invalid subreddits are detected
- A custom `User-Agent` is always sent, to avoid Reddit rate limiting

## Files

| File | Description |
|------|-------------|
| `0-subs.py` | `number_of_subscribers(subreddit)` returns the subscriber count, or 0 if invalid |
| `1-top_ten.py` | `top_ten(subreddit)` prints the first 10 hot post titles |
| `2-recurse.py` | `recurse(subreddit, hot_list=[])` returns all hot post titles, recursively |
| `3-count.py` | `count_words(subreddit, word_list)` prints a sorted count of keywords in hot titles |

## Usage

```
$ python3 0-main.py programming
$ python3 1-main.py programming
$ python3 2-main.py programming
$ python3 3-main.py programming 'python java javascript'
```

## Author

honore-lab