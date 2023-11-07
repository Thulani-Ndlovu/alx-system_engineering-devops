#!/usr/bin/python3
'''
    queries the Reddit API and prints the titles
    of the first 10 hot posts listed for a given subreddit
'''
import requests


def top_ten(subreddit):
    '''Prints first 10 titles of hot posts in subreddit'''
    apiURL = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {
        "User-Agent": "Thulani_Ndlovu"
    }

    res = requests.get(apiURL, headers=headers, allow_redirects=False)
    if res.status_code == 404:
        print("None")
        return
    result = res.json().get("data")
    [print(i.get("data").get("title")) for i in result.get("children")]
