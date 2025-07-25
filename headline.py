class Headline:
    """Represents a headline from Hacker News (ycombinator.com)."""

    def __init__(self, data):
        self._title = data['title']
        self._link = data['link']
        self._score = data['score']
        self._author = data['author']
        self._date = data['date']

    def __str__(self):
        return f"Title: {self._title} | Link: {self._link} | {self._score} Points\nAuthor: {self._author} | Date: {self._date}\n"

    def get_title(self):
        return self._title

    def get_link(self):
        return self._link
    
    def get_score(self):
        return self._score
    
    def get_author(self):
        return self._author
    
    def get_date(self):
        return self._date
    
    def match_keyword(self, keyword):
        return keyword.lower() in self._title.lower()