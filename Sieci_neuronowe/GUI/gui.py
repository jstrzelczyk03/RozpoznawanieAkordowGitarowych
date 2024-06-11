from pathlib import Path
from tkinter import Tk, Canvas, Button, PhotoImage, Frame

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH_FRAME0 = OUTPUT_PATH / Path(r"assets/frame0")
ASSETS_PATH_FRAME1 = OUTPUT_PATH / Path(r"assets/frame1")
ASSETS_PATH_FRAME2 = OUTPUT_PATH / Path(r"assets/frame2")
ASSETS_PATH_FRAME3 = OUTPUT_PATH / Path(r"assets/frame3")
ASSETS_PATH_FRAME4 = OUTPUT_PATH / Path(r"assets/frame4")
ASSETS_PATH_FRAME5 = OUTPUT_PATH / Path(r"assets/frame5")
ASSETS_PATH_FRAME6 = OUTPUT_PATH / Path(r"assets/frame6")
ASSETS_PATH_FRAME7 = OUTPUT_PATH / Path(r"assets/frame7")
ASSETS_PATH_FRAME8 = OUTPUT_PATH / Path(r"assets/frame8")
def relative_to_assets(path: str, frame: int) -> Path:
    if frame == 0:
        return ASSETS_PATH_FRAME0 / Path(path)
    elif frame == 1:
        return ASSETS_PATH_FRAME1 / Path(path)
    elif frame == 2:
        return ASSETS_PATH_FRAME2 / Path(path)
    elif frame == 3:
        return ASSETS_PATH_FRAME3 / Path(path)
    elif frame == 4:
        return ASSETS_PATH_FRAME4 / Path(path)
    elif frame == 5:
        return ASSETS_PATH_FRAME5 / Path(path)
    elif frame == 6:
        return ASSETS_PATH_FRAME6 / Path(path)
    elif frame == 7:
        return ASSETS_PATH_FRAME7 / Path(path)
    elif frame == 8:
        return ASSETS_PATH_FRAME8 / Path(path)

def show_frame(frame):
    frame.tkraise()

def update_chord_image(chord):
    chord_images = {
        "A": "Text_A.png",
        "am": "Text_am.png",
        "C": "Text_C.png",
        "D": "Text_D.png",
        "dm": "Text_dm.png",
        "E": "Text_E.png",
        "em": "Text_em.png",
        "F": "Text_F.png",
        "fm": "Text_fm.png",
        "G": "Text_G.png",
        "H": "Text_H.png",
        "hm": "Text_hm.png",
    }
    gryf_images = {
        "A": "Gryf_A.png",
        "am": "Gryf_am.png",
        "C": "Gryf_C.png",
        "D": "Gryf_D.png",
        "dm": "Gryf_dm.png",
        "E": "Gryf_E.png",
        "em": "Gryf_em.png",
        "F": "Gryf_F.png",
        "fm": "Gryf_fm.png",
        "G": "Gryf_G.png",
        "H": "Gryf_H.png",
        "hm": "Gryf_hm.png",
    }

    text_image_file = chord_images.get(chord, "Text.png")
    text_image_path = relative_to_assets(text_image_file, 0)
    new_text_image = PhotoImage(file=text_image_path)
    canvas0.itemconfig(image_3_id, image=new_text_image)
    canvas0.image = new_text_image  # Aktualizacja odniesienia do obrazu, aby zapobiec usunięciu przez garbage collector

    gryf_image_file = gryf_images.get(chord, "Gryf.png")
    gryf_image_path = relative_to_assets(gryf_image_file, 0)
    new_gryf_image = PhotoImage(file=gryf_image_path)
    canvas0.itemconfig(image_gryf_id, image=new_gryf_image)
    canvas0.gryf_image = new_gryf_image  # Aktualizacja odniesienia do obrazu, aby zapobiec usunięciu przez garbage collector

def switch_frame_and_color(target_frame, button_active, button_inactive):
    window.after(100, lambda: show_frame(target_frame))
    button_active.config(fg="black", activeforeground="black")
    button_inactive.config(fg="gray", activeforeground="gray")

def start_gui():
    global window, canvas0, image_2, image_3_id, image_gryf_id, image_image_2, image_image_3, image_image_gryf, image_image_5
    window = Tk()
    window.geometry("1920x1080")
    window.configure(bg="#2F2F2F")  # Ustawienie tła okna na ciemny szary

    frame0 = Frame(window, bg="#2F2F2F")  # Ustawienie tła ramki na ciemny szary
    frame1 = Frame(window, bg="#2F2F2F")
    frame2 = Frame(window, bg="#2F2F2F")
    frame3 = Frame(window, bg="#2F2F2F")
    frame4 = Frame(window, bg="#2F2F2F")
    frame5 = Frame(window, bg="#2F2F2F")
    frame6 = Frame(window, bg="#2F2F2F")
    frame7 = Frame(window, bg="#2F2F2F")
    frame8 = Frame(window, bg="#2F2F2F")

    for frame in (frame0, frame1, frame2, frame3, frame4, frame5, frame6, frame7, frame8):
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

    image_image_2 = PhotoImage(file=relative_to_assets("Signal_ON.png", 0))
    image_2 = canvas0.create_image(
        1100.0,
        600.0,
        image=image_image_2
    )

    # Tworzenie globalnego image_3_id
    image_image_3 = PhotoImage(file=relative_to_assets("Text.png", 0))
    image_3_id = canvas0.create_image(
        960.0,
        290.0,
        image=image_image_3
    )

    # Tworzenie globalnego image_gryf_id
    image_image_gryf = PhotoImage(file=relative_to_assets("Gryf.png", 0))
    image_gryf_id = canvas0.create_image(
        315.0,
        540.0,
        image=image_image_gryf
    )

    image_image_5 = PhotoImage(file=relative_to_assets("Mikrofon.png", 0))
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
        command=lambda: switch_frame_and_color(frame0, button_1_frame0, button_2_frame0),
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
        command=lambda: switch_frame_and_color(frame1, button_1_frame1, button_2_frame1),
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

    button_image_3 = PhotoImage(
        file=relative_to_assets("Spis_1.png", 1))
    button_3 = Button(
        frame1,
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: show_frame(frame2),
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

    button_image_4 = PhotoImage(
        file=relative_to_assets("Spis_2.png", 1))
    button_4 = Button(
        frame1,
        image=button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: show_frame(frame3),
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
        file=relative_to_assets("Spis_3.png", 1))
    button_5 = Button(
        frame1,
        image=button_image_5,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: show_frame(frame4),
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
        file=relative_to_assets("Spis_4.png", 1))
    button_6 = Button(
        frame1,
        image=button_image_6,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: show_frame(frame5),
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
        file=relative_to_assets("Spis_5.png", 1))
    button_7 = Button(
        frame1,
        image=button_image_7,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: show_frame(frame6),
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
        file=relative_to_assets("Spis_6.png", 1))
    button_8 = Button(
        frame1,
        image=button_image_8,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: show_frame(frame7),
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
        file=relative_to_assets("Spis_7.png", 1))
    button_9 = Button(
        frame1,
        image=button_image_9,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: show_frame(frame8),
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

    # Frame 2 content
    canvas2 = Canvas(
        frame2,
        bg="#2F2F2F",  # Ustawienie tła canvas na ciemny szary
        height=1080,
        width=1920,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )
    canvas2.place(x=0, y=0)

    button_image_1_frame2 = PhotoImage(
        file=relative_to_assets("Rozpoznaj_ON.png", 2))
    button_1_frame2 = Button(
        frame2,
        image=button_image_1_frame2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: switch_frame_and_color(frame0, button_1_frame2, button_2_frame2),
        relief="flat",
        bg="#2F2F2F",  # Ustawienie tła przycisku na ciemny szary
        activebackground="#2F2F2F",
        fg="gray",
        activeforeground="gray"
    )
    button_1_frame2.place(
        x=0.0,
        y=0.0,
        width=960.0,
        height=78.0
    )

    button_image_2_frame2 = PhotoImage(
        file=relative_to_assets("Zagraj_OFF.png", 2))
    button_2_frame2 = Button(
        frame2,
        image=button_image_2_frame2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: switch_frame_and_color(frame1, button_1_frame2, button_2_frame2),
        relief="flat",
        bg="#2F2F2F",  # Ustawienie tła przycisku na ciemny szary
        activebackground="#2F2F2F",
        fg="black",
        activeforeground="black"
    )
    button_2_frame2.place(
        x=960.0,
        y=0.0,
        width=960.0,
        height=78.0
    )

    image_image_6 = PhotoImage(
        file=relative_to_assets("Utwor_1.png", 2))
    image_6 = canvas2.create_image(
        960.0,  # X-coordinate for the center of the window
        540.0,  # Y-coordinate for the center of the window
        image=image_image_6
    )

    # Frame 3 content
    canvas3 = Canvas(
        frame3,
        bg="#2F2F2F",  # Ustawienie tła canvas na ciemny szary
        height=1080,
        width=1920,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )
    canvas3.place(x=0, y=0)

    button_image_1_frame3 = PhotoImage(
        file=relative_to_assets("Rozpoznaj_ON.png", 3))
    button_1_frame3 = Button(
        frame3,
        image=button_image_1_frame3,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: switch_frame_and_color(frame0, button_1_frame3, button_2_frame3),
        relief="flat",
        bg="#2F2F2F",  # Ustawienie tła przycisku na ciemny szary
        activebackground="#2F2F2F",
        fg="gray",
        activeforeground="gray"
    )
    button_1_frame3.place(
        x=0.0,
        y=0.0,
        width=960.0,
        height=78.0
    )

    button_image_2_frame3 = PhotoImage(
        file=relative_to_assets("Zagraj_OFF.png", 3))
    button_2_frame3 = Button(
        frame3,
        image=button_image_2_frame3,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: switch_frame_and_color(frame1, button_1_frame3, button_2_frame3),
        relief="flat",
        bg="#2F2F2F",  # Ustawienie tła przycisku na ciemny szary
        activebackground="#2F2F2F",
        fg="black",
        activeforeground="black"
    )
    button_2_frame3.place(
        x=960.0,
        y=0.0,
        width=960.0,
        height=78.0
    )

    image_image_7 = PhotoImage(
        file=relative_to_assets("Utwor_2.png", 3))
    image_7 = canvas3.create_image(
        960.0,  # X-coordinate for the center of the window
        540.0,  # Y-coordinate for the center of the window
        image=image_image_7
    )

    # Frame 4 content
    canvas4 = Canvas(
        frame4,
        bg="#2F2F2F",  # Ustawienie tła canvas na ciemny szary
        height=1080,
        width=1920,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )
    canvas4.place(x=0, y=0)

    button_image_1_frame4 = PhotoImage(
        file=relative_to_assets("Rozpoznaj_ON.png", 4))
    button_1_frame4 = Button(
        frame4,
        image=button_image_1_frame4,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: switch_frame_and_color(frame0, button_1_frame4, button_2_frame4),
        relief="flat",
        bg="#2F2F2F",  # Ustawienie tła przycisku na ciemny szary
        activebackground="#2F2F2F",
        fg="gray",
        activeforeground="gray"
    )
    button_1_frame4.place(
        x=0.0,
        y=0.0,
        width=960.0,
        height=78.0
    )

    button_image_2_frame4 = PhotoImage(
        file=relative_to_assets("Zagraj_OFF.png", 4))
    button_2_frame4 = Button(
        frame4,
        image=button_image_2_frame4,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: switch_frame_and_color(frame1, button_1_frame4, button_2_frame4),
        relief="flat",
        bg="#2F2F2F",  # Ustawienie tła przycisku na ciemny szary
        activebackground="#2F2F2F",
        fg="black",
        activeforeground="black"
    )
    button_2_frame4.place(
        x=960.0,
        y=0.0,
        width=960.0,
        height=78.0
    )

    image_image_8 = PhotoImage(
        file=relative_to_assets("Utwor_3.png", 4))
    image_8 = canvas4.create_image(
        960.0,  # X-coordinate for the center of the window
        540.0,  # Y-coordinate for the center of the window
        image=image_image_8
    )

    # Frame 5 content
    canvas5 = Canvas(
        frame5,
        bg="#2F2F2F",  # Ustawienie tła canvas na ciemny szary
        height=1080,
        width=1920,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )
    canvas5.place(x=0, y=0)

    button_image_1_frame5 = PhotoImage(
        file=relative_to_assets("Rozpoznaj_ON.png", 5))
    button_1_frame5 = Button(
        frame5,
        image=button_image_1_frame5,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: switch_frame_and_color(frame0, button_1_frame5, button_2_frame5),
        relief="flat",
        bg="#2F2F2F",  # Ustawienie tła przycisku na ciemny szary
        activebackground="#2F2F2F",
        fg="gray",
        activeforeground="gray"
    )
    button_1_frame5.place(
        x=0.0,
        y=0.0,
        width=960.0,
        height=78.0
    )

    button_image_2_frame5 = PhotoImage(
        file=relative_to_assets("Zagraj_OFF.png", 5))
    button_2_frame5 = Button(
        frame5,
        image=button_image_2_frame5,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: switch_frame_and_color(frame1, button_1_frame5, button_2_frame5),
        relief="flat",
        bg="#2F2F2F",  # Ustawienie tła przycisku na ciemny szary
        activebackground="#2F2F2F",
        fg="black",
        activeforeground="black"
    )
    button_2_frame5.place(
        x=960.0,
        y=0.0,
        width=960.0,
        height=78.0
    )

    image_image_9 = PhotoImage(
        file=relative_to_assets("Utwor_4.png", 5))
    image_9 = canvas5.create_image(
        960.0,  # X-coordinate for the center of the window
        540.0,  # Y-coordinate for the center of the window
        image=image_image_9
    )

    # Frame 6 content
    canvas6 = Canvas(
        frame6,
        bg="#2F2F2F",  # Ustawienie tła canvas na ciemny szary
        height=1080,
        width=1920,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )
    canvas6.place(x=0, y=0)

    button_image_1_frame6 = PhotoImage(
        file=relative_to_assets("Rozpoznaj_ON.png", 6))
    button_1_frame6 = Button(
        frame6,
        image=button_image_1_frame6,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: switch_frame_and_color(frame0, button_1_frame6, button_2_frame6),
        relief="flat",
        bg="#2F2F2F",  # Ustawienie tła przycisku na ciemny szary
        activebackground="#2F2F2F",
        fg="gray",
        activeforeground="gray"
    )
    button_1_frame6.place(
        x=0.0,
        y=0.0,
        width=960.0,
        height=78.0
    )

    button_image_2_frame6 = PhotoImage(
        file=relative_to_assets("Zagraj_OFF.png", 6))
    button_2_frame6 = Button(
        frame6,
        image=button_image_2_frame6,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: switch_frame_and_color(frame1, button_1_frame6, button_2_frame6),
        relief="flat",
        bg="#2F2F2F",  # Ustawienie tła przycisku na ciemny szary
        activebackground="#2F2F2F",
        fg="black",
        activeforeground="black"
    )
    button_2_frame6.place(
        x=960.0,
        y=0.0,
        width=960.0,
        height=78.0
    )

    image_image_10 = PhotoImage(
        file=relative_to_assets("Utwor_5.png", 6))
    image_10 = canvas6.create_image(
        960.0,  # X-coordinate for the center of the window
        540.0,  # Y-coordinate for the center of the window
        image=image_image_10
    )

    # Frame 7 content
    canvas7 = Canvas(
        frame7,
        bg="#2F2F2F",  # Ustawienie tła canvas na ciemny szary
        height=1080,
        width=1920,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )
    canvas7.place(x=0, y=0)

    button_image_1_frame7 = PhotoImage(
        file=relative_to_assets("Rozpoznaj_ON.png", 7))
    button_1_frame7 = Button(
        frame7,
        image=button_image_1_frame7,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: switch_frame_and_color(frame0, button_1_frame7, button_2_frame7),
        relief="flat",
        bg="#2F2F2F",  # Ustawienie tła przycisku na ciemny szary
        activebackground="#2F2F2F",
        fg="gray",
        activeforeground="gray"
    )
    button_1_frame7.place(
        x=0.0,
        y=0.0,
        width=960.0,
        height=78.0
    )

    button_image_2_frame7 = PhotoImage(
        file=relative_to_assets("Zagraj_OFF.png", 7))
    button_2_frame7 = Button(
        frame7,
        image=button_image_2_frame7,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: switch_frame_and_color(frame1, button_1_frame7, button_2_frame7),
        relief="flat",
        bg="#2F2F2F",  # Ustawienie tła przycisku na ciemny szary
        activebackground="#2F2F2F",
        fg="black",
        activeforeground="black"
    )
    button_2_frame7.place(
        x=960.0,
        y=0.0,
        width=960.0,
        height=78.0
    )

    image_image_11 = PhotoImage(
        file=relative_to_assets("Utwor_6.png", 7))
    image_11 = canvas7.create_image(
        960.0,  # X-coordinate for the center of the window
        540.0,  # Y-coordinate for the center of the window
        image=image_image_11
    )

    # Frame 8 content
    canvas8 = Canvas(
        frame8,
        bg="#2F2F2F",  # Ustawienie tła canvas na ciemny szary
        height=1080,
        width=1920,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )
    canvas8.place(x=0, y=0)

    button_image_1_frame8 = PhotoImage(
        file=relative_to_assets("Rozpoznaj_ON.png", 8))
    button_1_frame8 = Button(
        frame8,
        image=button_image_1_frame8,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: switch_frame_and_color(frame0, button_1_frame8, button_2_frame8),
        relief="flat",
        bg="#2F2F2F",  # Ustawienie tła przycisku na ciemny szary
        activebackground="#2F2F2F",
        fg="gray",
        activeforeground="gray"
    )
    button_1_frame8.place(
        x=0.0,
        y=0.0,
        width=960.0,
        height=78.0
    )

    button_image_2_frame8 = PhotoImage(
        file=relative_to_assets("Zagraj_OFF.png", 8))
    button_2_frame8 = Button(
        frame8,
        image=button_image_2_frame8,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: switch_frame_and_color(frame1, button_1_frame8, button_2_frame8),
        relief="flat",
        bg="#2F2F2F",  # Ustawienie tła przycisku na ciemny szary
        activebackground="#2F2F2F",
        fg="black",
        activeforeground="black"
    )
    button_2_frame8.place(
        x=960.0,
        y=0.0,
        width=960.0,
        height=78.0
    )

    image_image_12 = PhotoImage(
        file=relative_to_assets("Utwor_7.png", 8))
    image_12 = canvas8.create_image(
        960.0,  # X-coordinate for the center of the window
        540.0,  # Y-coordinate for the center of the window
        image=image_image_12
    )


    show_frame(frame0)
    window.resizable(False, False)
    window.mainloop()