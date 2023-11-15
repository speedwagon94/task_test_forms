import logging
from logging.handlers import RotatingFileHandler
import os

# Настройка логгирования
def configure_logging():
    logs_folder = 'logs'

    if not os.path.exists(logs_folder):
        os.makedirs(logs_folder)

    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

    error_handler = RotatingFileHandler(os.path.join(logs_folder, 'error.log'), maxBytes=100000, backupCount=1)
    error_handler.setLevel(logging.ERROR)
    error_handler.setFormatter(formatter)

    info_handler = RotatingFileHandler(os.path.join(logs_folder, 'info.log'), maxBytes=100000, backupCount=1)
    info_handler.setLevel(logging.INFO)
    info_handler.setFormatter(formatter)

    debug_handler = RotatingFileHandler(os.path.join(logs_folder, 'debug.log'), maxBytes=100000, backupCount=1)
    debug_handler.setLevel(logging.DEBUG)
    debug_handler.setFormatter(formatter)

    logger.addHandler(error_handler)
    logger.addHandler(info_handler)
    logger.addHandler(debug_handler)
