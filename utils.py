from colorama import Fore, Style

def welcome_message():
    print(Fore.CYAN + "\nWelcome to TaskEase - Smart To-Do Manager!" + Style.RESET_ALL)


def menu():
    print(Fore.GREEN + "\nSelect an Option:" + Style.RESET_ALL)
    print("1. Add Task")
    print("2. Remove Task")
    print("3. View All Tasks")
    print("4. Save Tasks")
    print("5. Load Tasks")
    print("6. Exit")


def task_type_menu():
    print("\nSelect Task Type:")
    print("1. Work Task")
    print("2. Personal Task")
    print("3. General Task")
