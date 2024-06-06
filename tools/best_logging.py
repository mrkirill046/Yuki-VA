# Imports | kazuha046 creator
import logging
import os

from datetime import datetime
from colorama import init, Fore

# Variables
if not os.path.exists('logs'):
    os.makedirs('logs')

log_filename = os.path.join('logs', datetime.now().strftime('%d.%m.%Y--%H.%M.%S.log'))
logging.basicConfig(
    filename=log_filename,
    level=logging.DEBUG,
    format='%(asctime)s:%(levelname)s:%(message)s',
    encoding='utf-8'
)


# Method
def create_log(text: str, level: str):
    init(autoreset=False)

    if level.lower() == 'debug':
        logging.debug(text)
        print(Fore.GREEN, text)
    elif level.lower() == 'info':
        logging.info(text)
        print(Fore.BLUE, text)
    elif level.lower() == 'warning':
        logging.warning(text)
        print(Fore.YELLOW, text)
    elif level.lower() == 'error':
        logging.error(text)
        print(Fore.RED, text)
    elif level.lower() == 'critical':
        logging.critical(text)
        print(Fore.MAGENTA, text)
    else:
        print(Fore.WHITE, f'Unknown logging level: {level}. Message: {text}')
