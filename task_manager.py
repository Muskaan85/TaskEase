import json
from task import Task, WorkTask, PersonalTask

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, title):
        self.tasks = [task for task in self.tasks if task.title.lower() != title.lower()]

    def show_all_tasks(self):
        if not self.tasks:
            print("\033[91mNo tasks available.\033[0m")
        for task in self.tasks:
            task.display()

    def save_tasks(self, filename):
        data = []
        for task in self.tasks:
            data.append({
                'type': task.__class__.__name__,
                'title': task.title,
                'description': task.description,
                'due_date': task.due_date,
                'priority': task.priority
            })
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)

    def load_tasks(self, filename):
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
            self.tasks.clear()
            for item in data:
                task_type = item['type']
                if task_type == 'WorkTask':
                    task = WorkTask(item['title'], item['description'], item['due_date'], item['priority'])
                elif task_type == 'PersonalTask':
                    task = PersonalTask(item['title'], item['description'], item['due_date'], item['priority'])
                else:
                    task = Task(item['title'], item['description'], item['due_date'], item['priority'])
                self.tasks.append(task)
        except FileNotFoundError:
            print("\033[91mSave file not found. Starting with empty task list.\033[0m")
