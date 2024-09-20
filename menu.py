import os
import platform

class Menu:
    def __init__(self, title):
        self.title = title
        self.options = {}

    def add_option(self, key, description, func):
        self.options[key] = (description, func)

    def display(self):
        print(self.title)
        print("=" * len(self.title))
        for key, (description, _) in self.options.items():
            print(f"{key}: {description}")
        print(f"b: Back")
        print(f"q: Quit")

    def get_user_choice(self):
        choice = input("Please enter your choice: ").strip()
        return choice

    def run(self):
        self.clear_screen()
        while True:
            self.display()
            choice = self.get_user_choice()
            if choice in self.options:
                description, action = self.options[choice]
                self.clear_screen()
                print(f"You selected: {description}")
                if callable(action):  # If it's a function, call it
                    action()
                if isinstance(action, Menu):  # If it's a function, call it
                    action.run()
            elif choice == "b":
                self.clear_screen()
                print("Going Back...")
                break
            elif choice == "q":
                self.clear_screen()
                print("Quitting the application.")
                exit(1)
            else:
                self.clear_screen()
                print("Invalid choice. Please try again.")

    def clear_screen(self):
        # Check the current operating system
        if platform.system() == "Windows":
            os.system("cls")  # Clear screen for Windows
        else:
            os.system("clear")  # Clear screen for macOS and Linux
