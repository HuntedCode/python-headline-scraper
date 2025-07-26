from headline_feed import HeadlineFeed
from scraper import fetch_headlines

accepted_commands = {"exit", "filter", "help", "load", "refresh", "save", "sort", "view"}

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
            case "load":
                load_command(feed)
            case "save":
                save_command(feed)
            case "sort":
                sort_command(feed)
            case "view":
                view_command(feed)
    else:
        print("That is not a valid command, type 'help' for a list of commands.")

def filter_command(feed: HeadlineFeed):
    str_input = str(input("\nPlease enter keyword(s): "))
    keywords = str_input.split()
    print_string = "\nFiltering for: "
    for k in keywords:
        print_string += k + " "
    print(print_string)

    feed.keyword_filter(keywords)
    view_command(feed)

def help_command():
    string = "Use any of the following commands: "
    for index, command in enumerate(sorted(accepted_commands)):
        string += command
        if not index == len(accepted_commands) - 1:
            string += ", "
    print(string)

def load_command(feed: HeadlineFeed):
    feed.load_from_file()

def save_command(feed: HeadlineFeed):
    feed.save_to_file()

def sort_command(feed: HeadlineFeed):
    sort_on = str(input("\nWhat would you like to sort on (date, score or title)?: "))
    direction = not (str(input("\n('a')scending or ('d')escending? (Default: 'd'): ")).lower() == 'a')
    
    if sort_on.lower() in ('date', 'score', 'title'):
        feed.sort_feed(sort_on=sort_on, desc=direction)
    else:
        print("That is not a valid option. Defaulting to score sort:")
        feed.sort_feed()
    view_command(feed)

def view_command(feed: HeadlineFeed):
    print()
    feed.print_feed()