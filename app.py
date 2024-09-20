from menu import Menu
from parser import KurutaParser

class JoeKuruta():
    def __init__(self):
        self.parser = KurutaParser()
        self.menu = self.create_menu()

    def run(self):
        self.menu.run()

    def create_menu(self):
        menu = Menu("Main Menu")

        # Display Cards Sub-Menu
        display_menu = Menu("Display Cards")

        def sort_and_display_by_key(key):
            self.parser.sort_cards(key=key)
            self.parser.display_cards()

        def sort_and_display_by_code():
            sort_and_display_by_key("code")

        def sort_and_display_by_character():
            sort_and_display_by_key("character")

        display_menu.add_option("1", "By Code", sort_and_display_by_code)
        display_menu.add_option("2", "By Character", sort_and_display_by_character)

        # Main Menu
        menu.add_option("1", "Display Cards", display_menu)

        return menu
