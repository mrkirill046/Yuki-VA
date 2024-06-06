# Imports | kazuha046 creator
import subprocess
import pystray
import os
import sys
import tools.manage_programm
import tkinter as tk

from tkinter import font
from PIL import ImageTk
from pystray import MenuItem
from PIL import Image
from components.assistant_window import destroy_assistant_window
from tools.manage_programm import resource_path
from tools.best_logging import create_log


# Methods
def create_tray_icon():
    global icon

    image = Image.open(resource_path('source/heart.ico'))

    menu_items = [
        MenuItem('Настройки', show_settings_action),
        MenuItem('Выход', exit_action)
    ]

    icon = pystray.Icon('example', image, 'Юки - Виртуальный ассистент')
    icon.menu = pystray.Menu(*menu_items)
    icon.run()


def exit_action():
    create_log('LOG: Exiting', 'info')
    tools.manage_programm.start = False
    destroy_assistant_window()
    icon.remove()

    sys.exit(-1)


def show_settings_action():
    show_launcher()


def start_console():
    root = tk.Toplevel()
    root.title('Mini Console')
    root.iconbitmap(resource_path('source/heart.ico'))

    console_text = tk.Text(root, height=10, width=50)
    console_text.pack(padx=10, pady=10)

    input_entry = tk.Entry(root, width=50)
    input_entry.pack(padx=10, pady=5)

    def handle_input(event=None):
        command = input_entry.get()
        console_text.insert(tk.END, f'>>> {command}\n')
        input_entry.delete(0, tk.END)

        if command == 'start':
            subprocess.Popen(['cmd.exe', '/k', 'debug.exe'])
            root.after(1000, exit_action)

    input_entry.bind('<Return>', handle_input)

    root.mainloop()


def show_launcher():
    title = font.Font(family='Impact', size=26)
    text = font.Font(family='Constantia', size=18)

    settings_window = tk.Toplevel()

    settings_window.resizable(width=False, height=False)
    settings_window.title('Yuki - Launcher Settings')
    settings_window.iconbitmap(resource_path('source/heart.ico'))

    screen_width = settings_window.winfo_screenwidth() / 2
    screen_height = settings_window.winfo_screenheight() / 2

    img = Image.open(resource_path('source/assistant.png'))
    img = img.resize((250, 350))
    img = ImageTk.PhotoImage(img)

    label = tk.Label(settings_window, text='Yuki Launcher работает в фоновом режиме', font=title)
    label.pack()

    label2 = tk.Label(settings_window, text='Yuki Launcher - Настройки', font=title)
    label2.pack()

    image = tk.Label(settings_window, image=img)
    image.pack(pady=100)

    button = tk.Button(settings_window, text='Запустить режим отладки', font=text, bg='grey', command=start_console)
    button.pack()

    settings_window.geometry(f'{int(screen_width)}x{int(screen_height)}')
    settings_window.mainloop()
