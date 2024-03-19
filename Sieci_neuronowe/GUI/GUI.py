from tkinter import *
from PIL import Image,ImageTk
from win32api import GetSystemMetrics

WIDTH = GetSystemMetrics(0)
HEIGHT = GetSystemMetrics(1)

print("Width =", GetSystemMetrics(0))
print("Height =", GetSystemMetrics(1))

window = Tk()


# window.attributes('-fullscreen',True)
window.title("Dzejsomat - chords recognition")
window.minsize(int(WIDTH/2), int(HEIGHT/2))
# window.geometry("1280x720")
# window.config(padx=200, pady=50)

def function():
    canvas.create_text(100, 200, text="Pupupupu", font=("Arial", 45, "bold"))


canvas = Canvas(width=WIDTH, height=HEIGHT)
canvas.grid(row=0, column=0)
image = PhotoImage(file="GuitarTloA.png")
button1_image = (Image.open("micro3.png"))
button1_image = button1_image.resize((100, 100))
button1_image = ImageTk.PhotoImage(button1_image)
canvas.create_image(500, 250, image=image)

button1 = Button(window, image=button1_image, height=100, width=100, background="grey")
button1_canvas = canvas.create_window(500, 390,
                                       anchor="nw",
                                       window=button1
                                      )


window.mainloop()
