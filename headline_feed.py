from headline import Headline
import json
import os.path

class HeadlineFeed:
    """Represents a timeline of class Headline headlines from Hacker News."""

    def __init__(self, raw_list):
        headline_list = []
        for item in raw_list:
            headline_list.append(Headline(item))

        self._origin = headline_list
        self._feed = headline_list.copy()

    def keyword_filter(self, keywords):
        """Filters collected headlines based on if passed keyword is in title."""

        self._feed.clear()

        for headline in self._origin:
            if headline.match_keywords(keywords):
                self._feed.append(headline)

    def load_from_file(self):
        """Loads file and adds saved headlines to current feed. Does not change origin."""
        
        filename = str(input("Enter name of file to load: ")) + ".json"
        if os.path.isfile(filename):
            with open(filename, 'r', encoding='utf-8') as f:
                data = json.load(f)
                for d in data:
                    self._feed.append(Headline(d))
        else:
            print("That file does not exist. Check your spelling and try again.")

    def print_feed(self):
        """Outputs sorted/filtered headline list to command line."""

        if len(self._feed) > 0:
            for headline in self._feed:
                print(headline)
        else:
            print("No posts match your criteria.")
    
    def save_to_file(self):
        """Saves current feed to JSON file. Uses Headline to_dict method to convert."""

        filename = str(input("Please enter filename: ")) + ".json"
        if os.path.isfile(filename):
            if not str(input("Would you like to overwrite this file? y/n: ") == 'y'):
                return
        
        with open(filename, 'w', encoding='utf-8') as f:
            json_list = []
            for headline in self._feed:
                json_list.append(headline.to_dict())
            json.dump(json_list, f, indent=4)


    def sort_feed(self, sort_on="score", desc=True):
        """Sorts based on passed criteria. sort_on = ('date', 'score', 'title')."""

        match sort_on:
            case "date":
                self._feed.sort(key=lambda x: x.get_date(), reverse=desc)
            case "score":
                self._feed.sort(key=lambda x: x.get_score(), reverse=desc)
            case "title":
                self._feed.sort(key=lambda x: x.get_title(), reverse=desc)

    