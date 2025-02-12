
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import subprocess

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\Hudson Artur\Documents\Faculdade\Quinto_periodo\linhas\trabalho_da_disciplina\codigo\build\assets\frame5")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("1200x510")
window.configure(bg = "#F5F5F5")


canvas = Canvas(
    window,
    bg = "#F5F5F5",
    height = 510,
    width = 1200,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    467.5,
    227.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=384.0,
    y=199.0,
    width=167.0,
    height=54.0
)

canvas.create_text(
    220.0,
    30.0,
    anchor="nw",
    text="Linhas de Transmissão e Ondas",
    fill="#000000",
    font=("Inter Bold", 48 * -1)
)

def open_gui2():
    subprocess.Popen(["python", "build/gui2.py"])
    window.destroy()

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=open_gui2,
    relief="flat"
)
button_1.place(
    x=824.0,
    y=421.0,
    width=161.0,
    height=55.0
)

def open_gui7():
    subprocess.Popen(["python", "build/gui7.py"])
    window.destroy()

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=open_gui7,
    relief="flat"
)
button_2.place(
    x=195.0,
    y=421.0,
    width=161.0,
    height=55.0
)

canvas.create_text(
    498.0,
    118.0,
    anchor="nw",
    text="Eq. Telegráficas",
    fill="#000000",
    font=("RobotoRoman Regular", 28 * -1)
)

canvas.create_text(
    44.0,
    211.0,
    anchor="nw",
    text="Condutividade do dielétrico:",
    fill="#000000",
    font=("RobotoRoman Regular", 24 * -1)
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    467.5,
    315.0,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=384.0,
    y=287.0,
    width=167.0,
    height=54.0
)

canvas.create_text(
    51.0,
    299.0,
    anchor="nw",
    text="Espessura do dielétrico (d):",
    fill="#000000",
    font=("RobotoRoman Regular", 24 * -1)
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    1044.5,
    227.0,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_3.place(
    x=961.0,
    y=199.0,
    width=167.0,
    height=54.0
)

canvas.create_text(
    611.0,
    211.0,
    anchor="nw",
    text="Raio do condutor externo (a):",
    fill="#000000",
    font=("RobotoRoman Regular", 24 * -1)
)

entry_image_4 = PhotoImage(
    file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(
    1044.5,
    307.0,
    image=entry_image_4
)
entry_4 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_4.place(
    x=961.0,
    y=279.0,
    width=167.0,
    height=54.0
)

canvas.create_text(
    696.0,
    291.0,
    anchor="nw",
    text="Raio do condutor (b):",
    fill="#000000",
    font=("RobotoRoman Regular", 24 * -1)
)
window.resizable(False, False)
window.mainloop()
