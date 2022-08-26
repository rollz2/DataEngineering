
import pandas as pd

# Creating list to append tweet data to
from twitter import TwitterSearchScraper

tweets_list2 = []

# Using TwitterSearchScraper to scrape data and append tweets to list
for i, tweet in enumerate(
        TwitterSearchScraper('Russia').get_items()):
    if i > 10:
        break
    tweets_list2.append(tweet.json())

print(tweets_list2)