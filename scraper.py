import datetime
import requests
from bs4 import BeautifulSoup

def fetch_headlines(url="https://news.ycombinator.com/", limit=10):
    """Fetches headlines from param URL with param limit. Defaults to ycombinator.com & limit of 10."""

    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        title_spans = soup.find_all("span", class_="titleline", limit=limit)
        subline_spans = soup.find_all("span", class_="subline", limit=limit)

        headlines = []
        for span in title_spans:
            tag = span.find("a")
            headlines.append({'title': tag.text, 'link': tag['href']})
        
        index = 0
        for span in subline_spans:
            headlines[index]['score'] = int(span.find("span", class_="score").text.split()[0])
            headlines[index]['author'] = span.find("a", class_="hnuser").text
            headlines[index]['date'] = datetime.datetime.fromisoformat(span.find("span", class_="age")['title'].split()[0])
            index += 1

        return headlines
    else:
        print("Webpage didn't return correctly!")