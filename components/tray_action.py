# Imports | kazuha046 creator
import pystray
import sys
import tools.manage_programm

from pystray import MenuItem
from PIL import Image
from components.assistant_window import destroy_assistant_window
from tools.best_logging import create_log


# Methods
def create_tray_icon():
    global icon

    image = Image.open('source/heart.ico')

    menu_items = [
        MenuItem('Настройки', None),
        MenuItem('Выход', exit_action)
    ]

    icon = pystray.Icon('example', image, 'Example')
    icon.menu = pystray.Menu(*menu_items)
    icon.run()


def exit_action():
    create_log('LOG: Exiting', 'info')
    tools.manage_programm.start = False
    destroy_assistant_window()
    icon.remove()

    sys.exit(-1)
