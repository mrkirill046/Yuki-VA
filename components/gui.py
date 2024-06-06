# Imports | kazuha046 creator
import tkinter as tk

from tkinter import font
from PIL import ImageTk, Image
from components.start import start_assistant

# Variable
root = tk.Tk()

screen_width = root.winfo_screenwidth() / 2
screen_height = root.winfo_screenheight() / 2
window_width = root.winfo_reqwidth()
window_height = root.winfo_reqheight()

title = font.Font(family='Impact', size=26)
text = font.Font(family='Constantia', size=18)


# Methods
def starting_assistant():
    root.destroy()
    start_assistant()


def show_launcher():
    root.title('Yuki - Launcher')
    root.iconbitmap('source/heart.ico')
    root.resizable(width=False, height=False)

    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2

    img = Image.open('source/assistant.png')
    img = img.resize((250, 350))
    img = ImageTk.PhotoImage(img)

    label = tk.Label(root, text='Yuki Launcher работает в фоновом режиме', font=title)
    label.pack()

    image = tk.Label(root, image=img)
    image.pack(pady=100)

    button = tk.Button(root, text='Запустить виртуального ассистента', font=text, bg='grey', command=starting_assistant)
    button.pack()

    root.geometry(f'{int(screen_width)}x{int(screen_height)}+{int(x)}+{int(y)}')
    root.mainloop()
