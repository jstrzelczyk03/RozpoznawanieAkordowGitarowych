from tkinter import *
from PIL import Image, ImageTk
from win32api import GetSystemMetrics

# Funkcja do aktualizacji rozmiaru obrazu
def resize_image(event):
    new_width = event.width
    new_height = event.height
    image = original_image.resize((new_width, new_height))
    photo = ImageTk.PhotoImage(image)
    canvas.itemconfig(image_on_canvas, image=photo)
    # Musimy zaktualizować referencję do obrazu, aby nie został usunięty przez garbage collector
    canvas.image = photo

# Pobieranie wymiarów ekranu
WIDTH = GetSystemMetrics(0)
HEIGHT = GetSystemMetrics(1)

window = Tk()
window.title("Dzejsomat - chords recognition")
window.minsize(int(WIDTH/2), int(HEIGHT/2))

canvas = Canvas(window)
canvas.grid(row=0, column=0, sticky='nsew')

window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)

# Załadowanie obrazu przy użyciu PIL
original_image = Image.open("GuitarTloA.png")
photo = ImageTk.PhotoImage(original_image)

image_on_canvas = canvas.create_image(0, 0, anchor="nw", image=photo)

# Powiązanie zdarzenia zmiany rozmiaru okna z funkcją resize_image
window.bind('<Configure>', resize_image)

window.mainloop()
