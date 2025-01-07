
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import subprocess

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\Hudson Artur\Documents\Faculdade\Quinto_periodo\linhas\trabalho_da_disciplina\codigo\build\assets\frame2")


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
canvas.create_text(
    220.0,
    30.0,
    anchor="nw",
    text="Linhas de Transmissão e Ondas",
    fill="#000000",
    font=("Inter Bold", 48 * -1)
)

def open_gui1():
    subprocess.Popen(["python", "build/gui1.py"])
    window.destroy()

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=open_gui1,
    relief="flat"
)
button_1.place(
    x=824.0,
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

def open_gui3():
    subprocess.Popen(["python", "build/gui3.py"])
    window.destroy()

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=open_gui3,
    relief="flat"
)
button_2.place(
    x=355.0,
    y=310.0,
    width=70.0,
    height=50.0
)

def open_gui4():
    subprocess.Popen(["python", "build/gui4.py"])
    window.destroy()

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=open_gui4,
    relief="flat"
)
button_3.place(
    x=497.0,
    y=310.0,
    width=70.0,
    height=50.0
)

def open_gui5():
    subprocess.Popen(["python", "build/gui5.py"])
    window.destroy()

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=open_gui5,
    relief="flat"
)
button_4.place(
    x=639.0,
    y=310.0,
    width=70.0,
    height=50.0
)

def open_gui6():
    subprocess.Popen(["python", "build/gui6.py"])
    window.destroy()

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=open_gui6,
    relief="flat"
)
button_5.place(
    x=774.0,
    y=310.0,
    width=70.0,
    height=50.0
)

canvas.create_text(
    417.0,
    205.0,
    anchor="nw",
    text="Selecione um para o cálculo:",
    fill="#000000",
    font=("RobotoRoman Regular", 28 * -1)
)
window.resizable(False, False)
window.mainloop()