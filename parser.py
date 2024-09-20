from user import KURUTA_SPREADSHEET

# Script
import csv
import logging
import json
import yaml

from functools import wraps

import logging

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
        # Header
        title = "Displaying Cards"
        logging.info(title)
        logging.info("=" * len(title))

        # Display Cards
        for card in self.cards:
            card_content = {
                "code": card["code"],
                "character": card["character"],
                "series": card["series"]
            }
            logging.info(yaml.dump(card_content,
                                   indent=4,
                                   allow_unicode=True))

    @print_function_name
    def parse_spreadsheet(self, spreadsheet=KURUTA_SPREADSHEET):
        with open(KURUTA_SPREADSHEET, "r") as f:
            rows = csv.DictReader(f)

            contents = []
            for row in rows:
                contents.append(row)
        return contents
