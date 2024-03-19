import tkinter
import customtkinter as ctk
from win32api import GetSystemMetrics

WIDTH = int(GetSystemMetrics(0)/2)
HEIGHT = int(GetSystemMetrics(1)/2)

ctk.set_default_color_theme("dark-blue")
app = ctk.CTk()
app.grid_columnconfigure(0, weight=1)
app.grid_columnconfigure(1, weight=1)
app.title("Recognizing the guitar chords")
app.geometry(f"{WIDTH}x{HEIGHT}")
app.minsize(WIDTH, HEIGHT)

micro = tkinter.PhotoImage(file="micro3.png")
button = ctk.CTkButton(master=app, fg_color="blue", text="Rozpoznaj akord")
button2 = ctk.CTkButton(master=app, fg_color="blue", text="Zagraj utwór")


button.grid(row=0, column=0, padx=5, pady=20, sticky="ew")
button2.grid(row=0, column=1, padx=5, pady=20, sticky="ew")

app.mainloop()
