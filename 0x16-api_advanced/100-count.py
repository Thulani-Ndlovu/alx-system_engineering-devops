#!/usr/bin/python3
'''
    recursive function that queries the Reddit API
    and parses the title of all hot articles
    prints a sorted count of given keywords
    (case-insensitive, delimited by spaces
'''
import requests


def count_words(subreddit, word_list, after="", count=0, words={}):
    '''recursively query reddit api'''
    apiURL = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        "User-Agent": "Thulani_Ndlovu"
    }
    params = {
        "count": count,
        "after": after,
        "limit": 100
    }
    res = requests.get(apiURL, headers=headers, params=params,
                       allow_redirects=False)
    try:
        result = res.json()
        if res.status_code == 404:
            raise Exception
    except Exception:
        print("")
        return
    result = result.json().get("data")
    after = result.get("after")
    count += result.get("dist")
    for i in result.get("children"):
        title = i.get("data").get("title").lower().split()
        for w in word_list:
            if w.lower() in title:
                times = len([t for t in title if t == w.lower()])
                if words.get(w) is None:
                    words[w] = times
            else:
                words[w] += times
    if after is None:
        if len(words) == 0:
            print("")
            return
        words = sorted(words.items(), key=lambda kv: (-kv[1], kv[0]))
        [print("{}: {}".format(k, v)) for k, v in words]
    else:
        count_words(subreddit, word_list, after, count, words)
