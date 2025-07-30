from task_manager import TaskManager
from task import Task, WorkTask, PersonalTask
from utils import welcome_message, menu, task_type_menu

def main():
    manager = TaskManager()
    filename = 'tasks.json'

    welcome_message()

    while True:
        menu()
        choice = input("\nEnter your choice (1-6): ")

        if choice == '1':
            task_type_menu()
            type_choice = input("Select task type (1-3): ")

            title = input("Enter Title: ")
            description = input("Enter Description: ")
            due_date = input("Enter Due Date (YYYY-MM-DD): ")
            priority = input("Enter Priority (Low/Medium/High): ")

            if type_choice == '1':
                task = WorkTask(title, description, due_date, priority)
            elif type_choice == '2':
                task = PersonalTask(title, description, due_date, priority)
            else:
                task = Task(title, description, due_date, priority)

            manager.add_task(task)
            print("\033[92mTask added successfully!\033[0m")

        elif choice == '2':
            title = input("Enter the title of the task to remove: ")
            manager.remove_task(title)
            print("\033[91mTask removed (if existed).\033[0m")

        elif choice == '3':
            manager.show_all_tasks()

        elif choice == '4':
            manager.save_tasks(filename)
            print("\033[92mTasks saved successfully!\033[0m")

        elif choice == '5':
            manager.load_tasks(filename)
            print("\033[92mTasks loaded successfully!\033[0m")

        elif choice == '6':
            print("\033[94mGoodbye!\033[0m")
            break

        else:
            print("\033[91mInvalid choice. Try again.\033[0m")


if __name__ == "__main__":
    main()
