from bs4 import BeautifulSoup
import datetime
import requests


def fetch_headlines(url="https://news.ycombinator.com/", limit=10):
    """Fetches headlines from param URL with param limit. Defaults to ycombinator.com & limit of 10."""

    response = requests.get(url, headers={"User-Agent": "PythonPracticeScraper/1.0"})

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        title_spans = soup.find_all("span", class_="titleline", limit=limit)
        subline_spans = soup.find_all("span", class_="subline", limit=limit)
        zipped_spans = list(zip(title_spans, subline_spans))

        try:
            headlines = []
            for span in zipped_spans:
                title_tag = span[0].find("a")
                headlines.append({
                    'title': title_tag.text,
                    'link': title_tag['href'], 
                    'score': int(span[1].find("span", class_="score").text.split()[0]),
                    'author': span[1].find("a", class_="hnuser").text,
                    'date': datetime.datetime.fromisoformat(span[1].find("span", class_="age")['title'].split()[0])})
        except:
            print("There was an error processing headlines. Please try again later.")
            return []

        return headlines
    else:
        print("Webpage didn't return correctly!")