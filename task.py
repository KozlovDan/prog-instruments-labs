import logging
from datetime import datetime

class Task:
    def __init__(self, title, description="", priority=1):
        self.title = title
        self.description = description
        self.priority = priority
        self.created_at = datetime.now()
        self.completed = False
        logging.debug(f"Создана задача: {self}")

    def complete(self):
        if self.completed:
            logging.warning(f"Задача уже выполнена: {self.title}")
        else:
            self.completed = True
            logging.info(f"Задача выполнена: {self.title}")

    def __str__(self):
        status = "Выполнена" if self.completed else "В процессе"
        return f"[{status}] {self.title} (Приоритет: {self.priority})"
