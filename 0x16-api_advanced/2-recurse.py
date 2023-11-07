#!/usr/bin/python3
'''
    recursive function that queries the Reddit API
    and returns a list containing the titles of all
    hot articles for a given subreddit
'''
import requests


def recurse(subreddit, hot_list=[], count=0, after=""):
    '''recursively query reddit api'''
    apiURL = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        "User-Agent": "Thulani_Ndlovu"
    }
    params = {
        "count": count,
        "after": after
    }
    res = requests.get(apiURL, headers=headers, params=params,
                       allow_redirects=False)
    if res.status_code == 404:
        return None
    result = res.json().get("data")
    after = result.get("after")
    count += result.get("dist")
    for i in result.get("children"):
        hot_list.append(i.get("data").get("title"))
    if after is not None:
        return recurse(subreddit, hot_list, count, after)
    return hot_list
