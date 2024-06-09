from pathlib import Path
from tkinter import Tk, Canvas, Button, PhotoImage, Frame

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH_FRAME0 = OUTPUT_PATH / Path(r"assets\frame0")
ASSETS_PATH_FRAME1 = OUTPUT_PATH / Path(r"assets\frame1")

def relative_to_assets(path: str, frame: int) -> Path:
    if frame == 0:
        return ASSETS_PATH_FRAME0 / Path(path)
    elif frame == 1:
        return ASSETS_PATH_FRAME1 / Path(path)

def show_frame(frame):
    frame.tkraise()

def switch_frame_and_color(target_frame, button_active, button_inactive):
    window.after(100, lambda: show_frame(target_frame))
    button_active.config(fg="black", activeforeground="black")
    button_inactive.config(fg="gray", activeforeground="gray")

window = Tk()
window.geometry("1920x1080")
window.configure(bg="#2F2F2F")  # Ustawienie tła okna na ciemny szary

frame0 = Frame(window, bg="#2F2F2F")  # Ustawienie tła ramki na ciemny szary
frame1 = Frame(window, bg="#2F2F2F")  # Ustawienie tła ramki na ciemny szary

for frame in (frame0, frame1):
    frame.place(x=0, y=0, width=1920, height=1080)

# Frame 0 content
canvas0 = Canvas(
    frame0,
    bg="#2F2F2F",  # Ustawienie tła canvas na ciemny szary
    height=1080,
    width=1920,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)
canvas0.place(x=0, y=0)

image_image_2 = PhotoImage(
    file=relative_to_assets("Signal_ON.png", 0))
image_2 = canvas0.create_image(
    1100.0,  # X-coordinate for the center of the window
    600.0,  # Y-coordinate for the center of the window
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("Text_C.png", 0))
image_3 = canvas0.create_image(
    960.0,
    290.0,
    image=image_image_3
)

image_image_4 = PhotoImage(
    file=relative_to_assets("Gryf_C.png", 0))
image_4 = canvas0.create_image(
    315.0,
    540.0,
    image=image_image_4
)

image_image_5 = PhotoImage(
    file=relative_to_assets("Mikrofon.png", 0))
image_5 = canvas0.create_image(
    960.0,
    870.0,
    image=image_image_5
)

button_image_1_frame0 = PhotoImage(
    file=relative_to_assets("Rozpoznaj_OFF.png", 0))
button_1_frame0 = Button(
    frame0,
    image=button_image_1_frame0,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: switch_frame_and_color(frame1, button_1_frame0, button_2_frame0),
    relief="flat",
    bg="#2F2F2F",  # Ustawienie tła przycisku na ciemny szary
    activebackground="#2F2F2F",
    fg="gray",
    activeforeground="gray"
)
button_1_frame0.place(
    x=0.0,
    y=0.0,
    width=960.0,
    height=78.0
)

button_image_2_frame0 = PhotoImage(
    file=relative_to_assets("Zagraj_ON.png", 0))
button_2_frame0 = Button(
    frame0,
    image=button_image_2_frame0,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: switch_frame_and_color(frame1, button_1_frame0, button_2_frame0),
    relief="flat",
    bg="#2F2F2F",  # Ustawienie tła przycisku na ciemny szary
    activebackground="#2F2F2F",
    fg="black",
    activeforeground="black"
)
button_2_frame0.place(
    x=960.0,
    y=0.0,
    width=960.0,
    height=78.0
)

# Frame 1 content
canvas1 = Canvas(
    frame1,
    bg="#2F2F2F",  # Ustawienie tła canvas na ciemny szary
    height=1080,
    width=1920,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)
canvas1.place(x=0, y=0)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png", 1))
button_3 = Button(
    frame1,
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    relief="flat",
    bg="#2F2F2F",  # Ustawienie tła przycisku na ciemny szary
    activebackground="#2F2F2F",
    fg="black",
    activeforeground="black"
)
button_3.place(
    x=372.0,
    y=114.0,
    width=1176.0,
    height=104.0
)

button_image_1_frame1 = PhotoImage(
    file=relative_to_assets("Rozpoznaj_ON.png", 1))
button_1_frame1 = Button(
    frame1,
    image=button_image_1_frame1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: switch_frame_and_color(frame0, button_1_frame1, button_2_frame1),
    relief="flat",
    bg="#2F2F2F",  # Ustawienie tła przycisku na ciemny szary
    activebackground="#2F2F2F",
    fg="gray",
    activeforeground="gray"
)
button_1_frame1.place(
    x=0.0,
    y=0.0,
    width=960.0,
    height=78.0
)

button_image_2_frame1 = PhotoImage(
    file=relative_to_assets("Zagraj_OFF.png", 1))
button_2_frame1 = Button(
    frame1,
    image=button_image_2_frame1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: switch_frame_and_color(frame0, button_1_frame1, button_2_frame1),
    relief="flat",
    bg="#2F2F2F",  # Ustawienie tła przycisku na ciemny szary
    activebackground="#2F2F2F",
    fg="black",
    activeforeground="black"
)
button_2_frame1.place(
    x=960.0,
    y=0.0,
    width=960.0,
    height=78.0
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png", 1))
button_4 = Button(
    frame1,
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_4 clicked"),
    relief="flat",
    bg="#2F2F2F",  # Ustawienie tła przycisku na ciemny szary
    activebackground="#2F2F2F",
    fg="black",
    activeforeground="black"
)
button_4.place(
    x=372.0,
    y=205.0,
    width=1176.0,
    height=126.0
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png", 1))
button_5 = Button(
    frame1,
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_5 clicked"),
    relief="flat",
    bg="#2F2F2F",  # Ustawienie tła przycisku na ciemny szary
    activebackground="#2F2F2F",
    fg="black",
    activeforeground="black"
)
button_5.place(
    x=372.0,
    y=331.0,
    width=1176.0,
    height=126.0
)

button_image_6 = PhotoImage(
    file=relative_to_assets("button_6.png", 1))
button_6 = Button(
    frame1,
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_6 clicked"),
    relief="flat",
    bg="#2F2F2F",  # Ustawienie tła przycisku na ciemny szary
    activebackground="#2F2F2F",
    fg="black",
    activeforeground="black"
)
button_6.place(
    x=372.0,
    y=457.0,
    width=1176.0,
    height=126.0
)

button_image_7 = PhotoImage(
    file=relative_to_assets("button_7.png", 1))
button_7 = Button(
    frame1,
    image=button_image_7,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_7 clicked"),
    relief="flat",
    bg="#2F2F2F",  # Ustawienie tła przycisku na ciemny szary
    activebackground="#2F2F2F",
    fg="black",
    activeforeground="black"
)
button_7.place(
    x=372.0,
    y=583.0,
    width=1176.0,
    height=126.0
)

button_image_8 = PhotoImage(
    file=relative_to_assets("button_8.png", 1))
button_8 = Button(
    frame1,
    image=button_image_8,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_8 clicked"),
    relief="flat",
    bg="#2F2F2F",  # Ustawienie tła przycisku na ciemny szary
    activebackground="#2F2F2F",
    fg="black",
    activeforeground="black"
)
button_8.place(
    x=372.0,
    y=709.0,
    width=1176.0,
    height=126.0
)

button_image_9 = PhotoImage(
    file=relative_to_assets("button_9.png", 1))
button_9 = Button(
    frame1,
    image=button_image_9,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_9 clicked"),
    relief="flat",
    bg="#2F2F2F",  # Ustawienie tła przycisku na ciemny szary
    activebackground="#2F2F2F",
    fg="black",
    activeforeground="black"
)
button_9.place(
    x=372.0,
    y=835.0,
    width=1176.0,
    height=126.0
)

show_frame(frame0)
window.resizable(False, False)
window.mainloop()
