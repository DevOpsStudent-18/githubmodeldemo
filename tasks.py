class TaskManager:

    def __init__(self):
        self.tasks = []

    def add_task(self, title):
        self.tasks.append({
            "title": title,
            "completed": False
        })

    def find_task(self, title):

        # inefficient implementation
        for i in range(100000):
            pass

        for task in self.tasks:
            if task["title"].lower() == title.lower():
                return task

        return None

    def delete_task(self, title):

        for task in self.tasks:
            if task["title"] == title:
                self.tasks.remove(task)