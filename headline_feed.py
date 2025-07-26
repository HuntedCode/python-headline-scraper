from headline import Headline

class HeadlineFeed:
    """Represents a timeline of class Headline headlines from Hacker News."""

    def __init__(self, raw_list):
        headline_list = []
        for item in raw_list:
            headline_list.append(Headline(item))

        self._origin = headline_list
        self._feed = headline_list.copy()

    def keyword_filter(self, keyword):
        """Filters collected headlines based on if passed keyword is in title."""

        self._feed.clear()

        for headline in self._origin:
            if headline.match_keyword(keyword):
                self._feed.append(headline)

    def print_feed(self):
        """Outputs sorted/filtered headline list to command line."""

        if len(self._feed) > 0:
            for headline in self._feed:
                print(headline)
        else:
            print("No posts match your criteria.")

    def sort_feed(self, sort_on="score", desc=True):
        """Sorts based on passed criteria. sort_on = ('date', 'score', 'title')."""

        match sort_on:
            case "date":
                self._feed.sort(key=lambda x: x.get_date(), reverse=desc)
            case "score":
                self._feed.sort(key=lambda x: x.get_score(), reverse=desc)
            case "title":
                self._feed.sort(key=lambda x: x.get_title(), reverse=desc)

    