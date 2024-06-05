# Imports | kazuha046 creator
import tkinter as tk
from PIL import Image, ImageTk

# Variables
drag_start_x = 0
drag_start_y = 0


# Methods
def on_drag_start(event):
    global drag_start_x, drag_start_y
    drag_start_x = event.x
    drag_start_y = event.y


def on_drag_motion(event):
    x = root.winfo_pointerx() - drag_start_x
    y = root.winfo_pointery() - drag_start_y
    root.geometry(f'+{x}+{y}')


def show_assistant_window():
    global root

    root = tk.Tk()
    root.title('Assistant')
    root.overrideredirect(True)
    root.attributes('-topmost', True)

    img = Image.open('assistant.png')
    photo = ImageTk.PhotoImage(img)

    label = tk.Label(root, image=photo, bg='white')
    label.image = photo
    label.pack()

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    window_width = img.width
    window_height = img.height

    x = screen_width - window_width
    y = screen_height - window_height - 70
    root.geometry(f'{window_width}x{window_height}+{x}+{y}')

    root.wm_attributes('-transparentcolor', 'white')

    label.bind('<Button-1>', on_drag_start)
    label.bind('<B1-Motion>', on_drag_motion)

    root.mainloop()
