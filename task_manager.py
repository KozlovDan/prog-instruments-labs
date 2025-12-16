import logging
import random
from task import Task

class TaskManager:
    def __init__(self):
        self.tasks = []
        logging.info("Менеджер задач инициализирован")

    def add_task(self, title, description="", priority=1):
        if not title:
            logging.error("Попытка добавить задачу без названия")
            return
        task = Task(title, description, priority)
        self.tasks.append(task)
        logging.info(f"Задача добавлена: {title}")

    def remove_task(self, title):
        found = False
        for task in self.tasks:
            if task.title == title:
                self.tasks.remove(task)
                logging.info(f"Задача удалена: {title}")
                found = True
                break
        if not found:
            logging.warning(f"Попытка удалить несуществующую задачу: {title}")

    def list_tasks(self, show_completed=True):
        logging.info("Список задач:")
        for task in self.tasks:
            if not show_completed and task.completed:
                continue
            logging.info(str(task))

    def search_task(self, keyword):
        results = [task for task in self.tasks if keyword.lower() in task.title.lower()]
        logging.info(f"Результаты поиска по ключевому слову '{keyword}':")
        for task in results:
            logging.info(str(task))
        if not results:
            logging.warning("Задачи не найдены")

    def complete_task(self, title):
        for task in self.tasks:
            if task.title == title:
                task.complete()
                return
        logging.warning(f"Попытка выполнить несуществующую задачу: {title}")

    def random_task_action(self):
        if not self.tasks:
            logging.warning("Нет задач для случайного действия")
            return
        task = random.choice(self.tasks)
        action = random.choice(["complete", "remove", "update"])
        if action == "complete":
            logging.info(f"Случайное действие: выполнение задачи '{task.title}'")
            task.complete()
        elif action == "remove":
            logging.info(f"Случайное действие: удаление задачи '{task.title}'")
            self.tasks.remove(task)
        elif action == "update":
            old_title = task.title
            task.title += "_обновлено"
            logging.info(f"Случайное действие: обновление задачи '{old_title}' -> '{task.title}'")
