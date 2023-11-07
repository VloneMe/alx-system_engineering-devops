#!/usr/bin/python3
"""
A function that queries the Reddit API and returns the number of subscribers.
"""

import requests

def number_of_subscribers(subreddit):
    # Reddit API URL for a subreddit's information (about.json)
    api_url = f"https://www.reddit.com/r/{subreddit}/about.json"

    # Set a custom User-Agent to avoid Too Many Requests errors
    headers = {
        "User-Agent": "YourAppName/1.0 by YourUsername"
    }

    # Send a GET request to the API
    response = requests.get(api_url, headers=headers)

    # Check if the response status code is 200 (OK)
    if response.status_code == 200:
        try:
            # Parse the JSON response
            data = response.json()
            # Extract the number of subscribers from the response
            subscribers = data["data"]["subscribers"]
            return subscribers
        except (KeyError, ValueError):
            # Handle any JSON parsing errors
            return 0
    else:
        # Handle non-200 response status codes (e.g., invalid subreddit)
        return 0

# Example usage:
subreddit_name = "learnpython"  # Replace with the subreddit you want to query
subscribers_count = number_of_subscribers(subreddit_name)
if subscribers_count > 0:
    print(f"The subreddit '{subreddit_name}' has {subscribers_count} subscribers.")
else:
    print(f"The subreddit '{subreddit_name}' is invalid or doesn't exist.")
