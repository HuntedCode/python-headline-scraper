# Headline Scraper CLI

A command-line tool that scrapes top headlines from Hacker News (news.ycombinator.com), allowing users to filter, sort, save/load feeds, and view details. Built in Python as part of a self-taught career transition project.

## Features
- Fetch live headlines with details like title, link, score, author, and date.
- Filter by keywords (multi-word support with OR logic).
- Sort by date, score, or title (ascending/descending).
- Save filtered/sorted feeds to JSON files and load them back.
- Ethical scraping: Includes User-Agent header and respects site structure.

## Installation
1. Clone the repository:

```
git clone https://github.com/HuntedCode/python-headline-scraper.git
cd python-headline-scraper
```

2. Install dependencies (Python 3.8+ required):

```
pip install requests beautifulsoup4
```

(No other external libraries needed.)

## Usage
Run the app from the command line:

```
python main.py
```

Once running, you'll see the initial feed. Use these commands:
- `view`: Display the current feed.
- `filter`: Enter keywords to filter titles.
- `sort`: Choose criteria (date, score, title) and direction (asc/desc).
- `save`: Export the current feed to a JSON file.
- `load`: Import a saved JSON file and append to the feed.
- `refresh`: Fetch fresh headlines from Hacker News.
- `help`: List all commands.
- `exit`: Quit the app.

Example session:
1. Type `refresh` to get latest headlines.
2. `filter` with "AI data" to search titles.
3. `sort` by "score" descending.
4. `save` to "my_feed.json".
5. `view` to see results.

**Note**: This is for educational purposes. Respect Hacker News' terms—avoid excessive requests (e.g., add delays if automating). No API key needed.

## Project Structure
- `main.py`: Entry point.
- `cli.py`: Handles user interface and commands.
- `scraper.py`: Fetches and parses web data using Requests and BeautifulSoup.
- `headline.py`: Data model for individual headlines.
- `headline_feed.py`: Manages feed operations (filter, sort, save/load).

## Contributing
Feedback welcome! Fork the repo, make changes, and submit a pull request. Issues can be reported on GitHub.

## License
MIT License—feel free to use and modify.

Built by Jeffrey Lowe as part of a 6-month Python learning plan for remote coding jobs. Last updated: July 27, 2025.