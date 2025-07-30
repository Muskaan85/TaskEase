class Task:
    def __init__(self, title, description, due_date, priority):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.priority = priority

    def display(self):
        print(f"\n\033[94mTitle:\033[0m {self.title}")
        print(f"\033[94mDescription:\033[0m {self.description}")
        print(f"\033[94mDue Date:\033[0m {self.due_date}")
        print(f"\033[94mPriority:\033[0m {self.priority}")


class WorkTask(Task):
    def display(self):
        print(f"\n\033[92m[Work Task]\033[0m")
        super().display()


class PersonalTask(Task):
    def display(self):
        print(f"\n\033[93m[Personal Task]\033[0m")
        super().display()
