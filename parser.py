from user import KURUTA_SPREADSHEET

# Script
import csv
import curses
import logging
import json
import yaml

from functools import wraps

def print_function_name(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # logging.info(f"Calling function: {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

class KurutaParser():
    def __init__(self,
                 spreadsheet=KURUTA_SPREADSHEET,
                 loglevel=logging.DEBUG):
        self.cards = {}
        self.spreadsheet = spreadsheet
        self.loglevel = loglevel

        self.init()

    @print_function_name
    def init(self):
        logging.basicConfig(format="%(message)s",
                            level=self.loglevel)

        logging.debug("Initializing Parser...")
        self.cards = self.parse_spreadsheet(self.spreadsheet)
        logging.debug("Sorting Cards...")
        self.sort_cards(key="code")

    def sort_cards(self, key="code"):
        self.cards = sorted(self.cards, key=lambda d: d[key])

    @print_function_name
    def display_cards(self):
        stdscr = curses.initscr()
        stdscr.keypad(True)

        stdscr.clear()
        stdscr.refresh()

        # Loop where k is the last character pressed
        k = None
        top_card_index = 0
        while (k != ord('q')):
            # Initialization
            stdscr.clear()
            height, width = stdscr.getmaxyx()

            if k == curses.KEY_DOWN:
                top_card_index += 1
            elif k == curses.KEY_UP:
                top_card_index = max(0, top_card_index - 1)

            # Header
            title = f"Displaying Cards: {top_card_index}"
            stdscr.addstr(0, 0, title)
            stdscr.addstr(1, 0, "=" * len(title))

            # Display Cards
            y = 2  # Start at 2 for Header
            for index in range(height - 2):
                card = self.cards[top_card_index + index]    # Use y value to determine index

                card_content = {
                    "code": card["code"],
                    "character": card["character"],
                    "series": card["series"]
                }

                content = f"{top_card_index + index}:"
                stdscr.addstr(y, 0, content[:width])
                y = y + 1

                for key in card_content:
                    content = f"  {key}: {card_content[key]}"
                    stdscr.addstr(y, 0, content[:width])
                    y = y + 1

                    if y >= height:
                        break
                if y >= height:
                        break

            # Refresh the screen
            stdscr.refresh()

            # Wait for next input
            k = stdscr.getch()

        curses.endwin()


    @print_function_name
    def parse_spreadsheet(self, spreadsheet=KURUTA_SPREADSHEET):
        with open(KURUTA_SPREADSHEET, "r") as f:
            rows = csv.DictReader(f)

            contents = []
            for row in rows:
                contents.append(row)
        return contents
