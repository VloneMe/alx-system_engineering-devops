#!/usr/bin/python
"""
A function that queries the Reddit API and prints the titles
of the first 10 hot posts listed for a given subreddit.
"""
from requests import get


def top_ten(subreddit):
    """
    The first top 10 best hot posts by subreddit
    """
    headers = {"user-agent": "Vlone Me"}
    apiUrl = "https://api.reddit.com/r/{}/hot?limit=10".format(subreddit)
    try:
        data = get(apiUrl, headers=headers, allow_redirects=False).json()
        hotPosts = data["data"]["children"]
        for post in hotPosts:
            print(post['data']['title'])
    except Exception:
        print("None")
