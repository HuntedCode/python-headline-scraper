from headline import Headline

class HeadlineFeed:
    """Represents a timeline of class Headline headlines from Hacker News."""

    def __init__(self, raw_list):
        headline_list = []
        for item in raw_list:
            headline_list.append(Headline(item))

        self._origin = headline_list
        self._feed = headline_list.copy()

    def print_feed(self):
        for headline in self._feed:
            print(headline)

    def keyword_filter(self, keyword):
        self._feed.clear()

        for headline in self._origin:
            if headline.match_keyword(keyword):
                self._feed.append(headline)

    def date_sort(self):
        self._feed.sort(key=lambda x: x.get_date(), reverse=True)

    def title_sort(self):
        self._feed.sort(key=lambda x: x.get_title(), reverse=True)

    def score_sort(self):
        self._feed.sort(key=lambda x: x.get_score(), reverse=True)

    