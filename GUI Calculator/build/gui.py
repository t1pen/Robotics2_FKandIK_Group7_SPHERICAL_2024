from pathlib import Path

from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\saloj\Documents\3rd Year 2nd Sem\Rob2\Final Project\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("900x600")
window.configure(bg = "#FFFFFF")

def reset():
    a1_E.delete(0, END)
    a2_E.delete(0, END)
    a3_E.delete(0, END)

    t1_E.delete(0, END)
    t2_E.delete(0, END)
    d3_E.delete(0, END)
    
    x_E.delete(0, END)
    y_E.delete(0, END)
    z_E.delete(0, END)


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 600,
    width = 900,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    0.0,
    0.0,
    900.0,
    600.0,
    fill="#262626",
    outline="")

canvas.create_text(
    130.0,
    49.0,
    anchor="nw",
    text="SPHERICAL",
    fill="#51FF00",
    font=("Metropolis Black", 48 * -1)
)

canvas.create_text(
    407.0,
    49.0,
    anchor="nw",
    text="MANIPULATOR",
    fill="#FFFFFF",
    font=("Metropolis Black", 48 * -1)
)

canvas.create_text(
    253.0,
    92.0,
    anchor="nw",
    text="FORWARD AND INVERSE KINEMATICS CALCULATOR",
    fill="#FFFFFF",
    font=("Metropolis Black", 15 * -1)
)

canvas.create_text(
    238.0,
    147.0,
    anchor="nw",
    text="Link Lengths",
    fill="#FFFFFF",
    font=("Calibri Italic", 20 * -1)
)

canvas.create_text(
    110.0,
    367.0,
    anchor="nw",
    text="Joint Variables",
    fill="#FFFFFF",
    font=("Calibri Italic", 20 * -1)
)

canvas.create_text(
    335.0,
    367.0,
    anchor="nw",
    text="Position Vector",
    fill="#FFFFFF",
    font=("Calibri Italic", 20 * -1)
)

canvas.create_text(
    190.0,
    184.0,
    anchor="nw",
    text="a₁:",
    fill="#FFFFFF",
    font=("Calibri", 16 * -1)
)

canvas.create_text(
    359.0,
    184.0,
    anchor="nw",
    text="cm",
    fill="#FFFFFF",
    font=("Calibri", 16 * -1)
)

canvas.create_text(
    73.0,
    403.0,
    anchor="nw",
    text="θ₁:",
    fill="#FFFFFF",
    font=("Calibri", 16 * -1)
)

canvas.create_text(
    242.0,
    403.0,
    anchor="nw",
    text="°",
    fill="#FFFFFF",
    font=("Calibri", 16 * -1)
)

canvas.create_text(
    73.0,
    443.0,
    anchor="nw",
    text="θ₂:",
    fill="#FFFFFF",
    font=("Calibri", 16 * -1)
)

canvas.create_text(
    242.0,
    443.0,
    anchor="nw",
    text="°",
    fill="#FFFFFF",
    font=("Calibri", 16 * -1)
)

canvas.create_text(
    73.0,
    483.0,
    anchor="nw",
    text="d₃:",
    fill="#FFFFFF",
    font=("Calibri", 16 * -1)
)

canvas.create_text(
    242.0,
    483.0,
    anchor="nw",
    text="cm",
    fill="#FFFFFF",
    font=("Calibri", 16 * -1)
)

canvas.create_text(
    307.0,
    403.0,
    anchor="nw",
    text="x:",
    fill="#FFFFFF",
    font=("Calibri", 16 * -1)
)

canvas.create_text(
    469.0,
    403.0,
    anchor="nw",
    text="cm",
    fill="#FFFFFF",
    font=("Calibri", 16 * -1)
)

canvas.create_text(
    307.0,
    443.0,
    anchor="nw",
    text="y:",
    fill="#FFFFFF",
    font=("Calibri", 16 * -1)
)

canvas.create_text(
    307.0,
    483.0,
    anchor="nw",
    text="z:",
    fill="#FFFFFF",
    font=("Calibri", 16 * -1)
)

canvas.create_text(
    471.0,
    443.0,
    anchor="nw",
    text="cm",
    fill="#FFFFFF",
    font=("Calibri", 16 * -1)
)

canvas.create_text(
    471.0,
    483.0,
    anchor="nw",
    text="cm",
    fill="#FFFFFF",
    font=("Calibri", 16 * -1)
)

canvas.create_text(
    190.0,
    224.0,
    anchor="nw",
    text="a₂:",
    fill="#FFFFFF",
    font=("Calibri", 16 * -1)
)

canvas.create_text(
    359.0,
    224.0,
    anchor="nw",
    text="cm",
    fill="#FFFFFF",
    font=("Calibri", 16 * -1)
)

canvas.create_text(
    190.0,
    264.0,
    anchor="nw",
    text="a₃:",
    fill="#FFFFFF",
    font=("Calibri", 16 * -1)
)

canvas.create_text(
    359.0,
    264.0,
    anchor="nw",
    text="cm",
    fill="#FFFFFF",
    font=("Calibri", 16 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    284.5,
    274.5,
    image=entry_image_1
)
a3_E = Entry(
    font=('Calibri', 13),
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
a3_E.place(
    x=218.0,
    y=260.0,
    width=133.0,
    height=29.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    284.5,
    234.5,
    image=entry_image_2
)
a2_E = Entry(
    font=('Calibri', 13),
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
a2_E.place(
    x=218.0,
    y=222.0,
    width=133.0,
    height=29.0
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    284.5,
    194.5,
    image=entry_image_3
)
a1_E = Entry(
    font=('Calibri', 13),
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
a1_E.place(
    x=218.0,
    y=182.0,
    width=133.0,
    height=29.0
)

entry_image_4 = PhotoImage(
    file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(
    168.0,
    414.0,
    image=entry_image_4
)
t1_E = Entry(
    font=('Calibri', 13),
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
t1_E.place(
    x=102.0,
    y=398.0,
    width=132.0,
    height=30.0
)

entry_image_5 = PhotoImage(
    file=relative_to_assets("entry_5.png"))
entry_bg_5 = canvas.create_image(
    168.0,
    453.5,
    image=entry_image_5
)
t2_E = Entry(
    font=('Calibri', 13),
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
t2_E.place(
    x=102.0,
    y=438.5,
    width=132.0,
    height=29.0
)

entry_image_6 = PhotoImage(
    file=relative_to_assets("entry_6.png"))
entry_bg_6 = canvas.create_image(
    168.0,
    493.5,
    image=entry_image_6
)
d3_E = Entry(
    font=('Calibri', 13),
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
d3_E.place(
    x=102.0,
    y=478.5,
    width=132.0,
    height=29.0
)

entry_image_7 = PhotoImage(
    file=relative_to_assets("entry_7.png"))
entry_bg_7 = canvas.create_image(
    395.0,
    414.0,
    image=entry_image_7
)
x_E = Entry(
    font=('Calibri', 13),
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
x_E.place(
    x=329.0,
    y=398.0,
    width=132.0,
    height=30.0
)

entry_image_8 = PhotoImage(
    file=relative_to_assets("entry_8.png"))
entry_bg_8 = canvas.create_image(
    395.0,
    453.5,
    image=entry_image_8
)
y_E = Entry(
    font=('Calibri', 13),
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
y_E.place(
    x=329.0,
    y=438.5,
    width=132.0,
    height=29.0
)

entry_image_9 = PhotoImage(
    file=relative_to_assets("entry_9.png"))
entry_bg_9 = canvas.create_image(
    395.0,
    495.0,
    image=entry_image_9
)
z_E = Entry(
    font=('Calibri', 13),
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
z_E.place(
    x=329.0,
    y=479.0,
    width=132.0,
    height=30.0
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=108.0,
    y=522.73291015625,
    width=118.0,
    height=30.26708984375
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
button_2.place(
    x=335.9855041503906,
    y=522.73291015625,
    width=117.42608642578125,
    height=30.26706314086914
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=reset,
    relief="flat"
)
button_3.place(
    x=235.0,
    y=301.0,
    width=99.0,
    height=30.44510269165039
)

canvas.create_rectangle(
    530.0,
    131.0,
    828.0,
    347.0,
    fill="#262626",
    outline="")

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    679.0,
    239.0,
    image=image_image_1
)

canvas.create_rectangle(
    530.0,
    359.0,
    828.0,
    560.0,
    fill="#262626",
    outline="")

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    679.0,
    459.0,
    image=image_image_2
)
window.resizable(False, False)
window.mainloop()
