#!/usr/bin/python3
'''Queries the Reddit API and returns the number of subscribers'''
import requests


def number_of_subscribers(subreddit):
    '''Total number of subscribers in reddit'''
    apiURL = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "Thulani_Ndlovu"
    }
    res = requests.get(apiURL, headers=headers, allow_redirects=False)
    if res.status_code == 404:
        return 0
    result = res.json().get("data")
    return result.get("subscribers")
