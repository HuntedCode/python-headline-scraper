#!/usr/bin/env python3
from scraper import fetch_headlines
from headline_feed import HeadlineFeed

if __name__ == "__main__":

    response = fetch_headlines(limit=5)
    feed = HeadlineFeed(response)

    feed.keyword_filter("data")
    feed.score_sort()
    feed.print_feed()