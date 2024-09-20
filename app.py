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
        display_menu.add_option("1", "By Code", self.parser.display_cards)

        # Main Menu
        menu.add_option("1", "Display Cards", display_menu)

        return menu

