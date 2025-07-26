#!/usr/bin/env python3
from cli import cli_run

if __name__ == "__main__":

    try:
        cli_run()
    except:
        print("There was an error. Please try again later.")