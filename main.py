#!/usr/bin/env python3
from scraper import fetch_headlines

class Headline:
    """Represents a headline from Hacker News (ycombinator.com)."""

    def __init__(self, data):
        self._title = data['title']
        self._link = data['link']
        self._score = data['score']

    def __str__(self):
        return f"Title: {self._title} | Link: {self._link} | {self._score}"

    def get_title(self):
        return self._title

    def get_link(self):
        return self._link
    
    def get_score(self):
        return self._score

if __name__ == "__main__":

    headline_feed = []
    response = fetch_headlines(limit=5)

    for item in response:
        headline = Headline(item)
        headline_feed.append(headline)

    for h in headline_feed:
        print(h)