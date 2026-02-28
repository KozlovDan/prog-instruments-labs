from logger_config import setup_logging
from demo import demo_task_manager
import logging

def main():
    setup_logging()
    logging.info("Программа запущена")
    demo_task_manager()
    logging.info("Программа завершена")

if __name__ == "__main__":
    main()
