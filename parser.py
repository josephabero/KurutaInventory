from user import KURUTA_SPREADSHEET

# Script
import csv
import logging
import json
import yaml

from functools import wraps

def print_function_name(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # print(f"Calling function: {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

class KurutaParser():
    def __init__(self,
                 spreadsheet=KURUTA_SPREADSHEET,
                 loglevel=logging.INFO):
        self.cards = {}
        self.spreadsheet = spreadsheet
        self.loglevel = loglevel

        self.init()

    @print_function_name
    def init(self):
        logging.basicConfig(format="%(message)s",
                            level=self.loglevel)
        self.cards = self.parse_spreadsheet(self.spreadsheet)

    @print_function_name
    def display_cards(self):
        title = "Displaying Cards"
        print(title)
        print("=" * len(title))
        for card in self.cards:
            card_content = {
                self.cards[card]["code"]: {
                    "character": self.cards[card]["character"],
                    "series": self.cards[card]["series"]
                }
            }
            logging.info(yaml.dump(card_content,
                                   indent=4,
                                   allow_unicode=True))

    @print_function_name
    def parse_spreadsheet(self, spreadsheet=KURUTA_SPREADSHEET):
        with open(KURUTA_SPREADSHEET, "r") as f:
            rows = csv.DictReader(f)

            contents = {}
            for row in rows:
                contents[row["code"]] = row
        return contents
