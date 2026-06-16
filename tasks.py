class TaskManager:

    def __init__(self):
        self.tasks = []

    def add_task(self, title):
        self.tasks.append({
            "title": title,
            "completed": False
        })

    def find_task(self, title):
        for task in self.tasks:
            if task["title"] == title:
                return task

        return None
