import random
import winsound
import tkinter as tk
from tkinter import messagebox 
from PIL import Image, ImageTk

LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
COLORS = ["green", "yellow", "orange", "red", "cyan", "white", "blue", "pink"]

def make_block(digits):
    block = list(digits)
    block.append(random.choice(LETTERS))
    block.append(random.choice(LETTERS))
    random.shuffle(block)
    return "".join(block)


def get_digits(block):
    digits = ""
    for symbol in block:
        if symbol.isdigit():
            digits += symbol
    return digits


def show_key(key, i=0):
    result.set(key[:i])
    if i < len(key):
        button.config(state="disabled")
        window.after(60, show_key, key, i + 1)
    else:
        button.config(state="normal")


def change_title_color(color_number=0):

    title.config(fg=COLORS[color_number])
    next_color_number = (color_number + 1) % len(COLORS)
    window.after(400, change_title_color, next_color_number)


def generate():
    number = entry.get()
    if len(number) != 6 or not number.isdigit():
        messagebox.showerror("Ошибка", "Введите 6 цифр")
        return

    block1 = make_block(number[3:])
    block2 = make_block(number[:3])

    total = int(get_digits(block1)) + int(get_digits(block2))
    block3 = str(total).zfill(4)      

    show_key(block1 + "-" + block2 + " " + block3)


window = tk.Tk()
window.title("Keygen")
window.geometry("800x450")
window.resizable(False, False)

# фон
image = Image.open("background.jpg")
image = image.resize((800, 450))
photo = ImageTk.PhotoImage(image)
background = tk.Label(window, image=photo)
background.place(x=0, y=0)

title = tk.Label(window, text="KEYGEN", font=("Courier", 30, "bold"), bg="black")
title.place(relx=0.5, y=50, anchor="center")

label = tk.Label(window, text="Введите 6 цифр", font=("Arial", 13), bg="black", fg="white")
label.place(relx=0.5, y=110, anchor="center")

entry = tk.Entry(window, font=("Courier", 16), justify="center", width=12)
entry.place(relx=0.5, y=145, anchor="center")

button = tk.Button(window, text="Сгенерировать ключ", font=("Arial", 12), bg="black", fg="white", command=generate)
button.place(relx=0.5, y=200, anchor="center")

result = tk.StringVar()
key_entry = tk.Entry(window, textvariable=result, font=("Courier", 18, "bold"), justify="center", width=18, state="readonly")
key_entry.place(relx=0.5, y=270, anchor="center")


winsound.PlaySound("music.wav", winsound.SND_FILENAME | winsound.SND_ASYNC | winsound.SND_LOOP)

change_title_color()

window.mainloop()