import time
import logging
import random
from task_manager import TaskManager

def generate_random_tasks(manager, count=10):
    logging.info(f"Генерация {count} случайных задач")
    for i in range(count):
        title = f"Задача_{i+1}"
        description = f"Описание для {title}"
        priority = random.randint(1, 5)
        manager.add_task(title, description, priority)
        time.sleep(0.01)  # чтобы время создания различалось

def demo_task_manager():
    logging.info("=== Демонстрация работы менеджера задач ===")
    manager = TaskManager()

    generate_random_tasks(manager, count=15)
    manager.list_tasks()

    for _ in range(10):
        manager.random_task_action()
        time.sleep(0.05)

    manager.search_task("3")
    manager.search_task("Не существует")

    manager.add_task("Ключевая задача", "Очень важная", priority=5)
    manager.complete_task("Ключевая задача")
    manager.remove_task("Ключевая задача")
    manager.remove_task("Ключевая задача")

    manager.list_tasks(show_completed=False)
    logging.info("=== Демонстрация завершена ===")
