from headline_feed import HeadlineFeed
from scraper import fetch_headlines

accepted_commands = {"exit", "filter", "help", "refresh", "sort", "view"}

def cli_run():
    """Controls basic interface loop for user."""

    feed = refresh_feed()
    view_command(feed)

    while True:
        command = input("What would you like to do?: ").lower()
        if command == "exit":
            break
        elif command == "refresh":
            feed = refresh_feed()
            view_command(feed)
            
        process_command(str(command), feed)

def refresh_feed():
    response = fetch_headlines(limit=5)
    return HeadlineFeed(response)

def process_command(command: str, feed: HeadlineFeed):
    """Processes command input and executes desired command."""

    if command in accepted_commands:
        match command:
            case "filter":
                filter_command(feed)
            case "help":
                help_command()
            case "sort":
                sort_command(feed)
            case "view":
                view_command(feed)
    else:
        print("That is not a valid command, type 'help' for a list of commands.")

def filter_command(feed: HeadlineFeed):
    keyword = str(input("\nPlease enter keyword: "))
    print(f"\nFiltering for: {keyword}")
    feed.keyword_filter(keyword)
    view_command(feed)

def help_command():
    string = "Use any of the following commands: "
    for index, command in enumerate(sorted(accepted_commands)):
        string += command
        if not index == len(accepted_commands) - 1:
            string += ", "
    print(string)

def sort_command(feed: HeadlineFeed):
    sort_on = str(input("\nWhat would you like to sort on (date, score or title)?: "))
    if sort_on.lower() in ('date', 'score', 'title'):
        feed.sort_feed(sort_on=sort_on)
    else:
        print("That is not a valid option. Defaulting to score sort:")
        feed.sort_feed()
    view_command(feed)

def view_command(feed: HeadlineFeed):
    print()
    feed.print_feed()