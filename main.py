import os
import tkinter as tk
from tkinter import messagebox

from czlowiek import Czlowiek
from world import World


def add_new_organizm(x, y):
    czoise_window = tk.Toplevel(window)
    czoise_window.title("Add new organism")
    czoise_window.geometry("300x300")
    czoise_window.resizable(False, False)

    user_choice = tk.StringVar()

    def select_choice():
        selected_organizm = user_choice.get()
        czoise_window.destroy()
        messagebox.showinfo("Choise", f"Added {selected_organizm}")
        world.add_organism(selected_organizm, x, y)
        draw_world()
        window.focus_set()

    organizms = ["Antylopa", "Lis", "Owca", "Wilk", "Zolw", "Trawa",
                 "Mlecz", "Guarana", "Wilcze jagody", "Barszcz sosnowskiego"]

    for option in organizms:
        rb = tk.Radiobutton(czoise_window, text=option,
                            variable=user_choice, value=option)
        rb.pack()

    select_button = tk.Button(
        czoise_window, text="Choose", command=select_choice)
    select_button.pack()


def show_hint_window():
    hint_text = '''Controls:
SPACE to next turn
U to use special ability
Arrows to move
S to save to file
L to load from file

Types of organisms and colors:
Antylopa - cyan
Lis - orange
Wilk - dark gray
Owca - white
Zolw - grey
Barszcz - magenta
Guarana - pink
Mlecz - yellow
Trawa - green
Wilcze jagody - blue'''

    hint_window = tk.Toplevel()
    hint_window.title("Hint")

    hint_label = tk.Label(hint_window, text=hint_text,
                          justify=tk.LEFT, padx=10, pady=10)
    hint_label.pack()


def on_mouse_click(event):
    if (event.x > world.width*20 or event.y > world.height*20):
        return
    add_new_organizm(event.x // 20, event.y // 20)


def file_manager_func(function):
    def save_text():
        entered_text = text_entry.get()
        function(entered_text)
        text_entry_window.destroy()

    text_entry_window = tk.Toplevel()
    text_entry_window.title("Enter file name")

    text_entry = tk.Entry(text_entry_window, width=30)
    text_entry.pack()

    save_button = tk.Button(
        text_entry_window, text="Confirm", command=save_text)
    save_button.pack()

    text_entry_window.wait_window()


def on_key_press(event):
    # print("Клавиша", event.keysym, "нажата")
    if (event.keysym == "Up"):
        world.human.akcja(0, -1)
    elif (event.keysym == "Down"):
        world.human.akcja(0, 1)
    elif (event.keysym == "Left"):
        world.human.akcja(-1, 0)
    elif (event.keysym == "Right"):
        world.human.akcja(1, 0)
    elif (event.keysym == "space"):
        pass
    elif (event.keysym.lower() == "u"):
        world.human.set_umiejetnosc()
        os.system('clear')
        print("Umiejetnosc aktywowana")
        return
    elif (event.keysym.lower() == "s"):
        save_to_file()
        return
    elif (event.keysym.lower() == "l"):
        load_from_file()
        return
    next_turn()


def next_turn():
    os.system('clear')
    world.next_turn()
    draw_world()


def save_to_file():
    file_manager_func(world.save_to_file)


def load_from_file():
    file_manager_func(world.load_from_file)
    draw_world()


def add_hood(window):
    # pack buttons in 2 rows and 2
    button_container = tk.Frame(window)
    button_container.pack(pady=10, fill=tk.BOTH)

    button1 = tk.Button(button_container, text="New turn", command=next_turn)
    button1.pack(side=tk.LEFT, padx=10, fill=tk.BOTH, expand=True)

    button2 = tk.Button(button_container, text="Show hint",
                        command=show_hint_window)
    button2.pack(side=tk.LEFT, padx=10, fill=tk.BOTH, expand=True)

    button_container2 = tk.Frame(window)
    button_container2.pack(pady=10, fill=tk.BOTH)

    button3 = tk.Button(button_container2, text="Save to file",
                        command=save_to_file)
    button3.pack(side=tk.LEFT, padx=10, fill=tk.BOTH, expand=True)

    button4 = tk.Button(button_container2, text="Load from file",
                        command=load_from_file)
    button4.pack(side=tk.LEFT, padx=10, fill=tk.BOTH, expand=True)

    window.bind()
    window.bind("<Button-3>", on_mouse_click)
    window.bind("<Key>", on_key_press)


def draw_world():
    canvas.delete("all")
    for organism in world.organisms:
        draw_organism(organism)

    draw_organism(world.human)


def draw_organism(organism):
    x = organism.x * 20
    y = organism.y * 20
    size = 20
    canvas.create_rectangle(x, y, x+size, y+size,
                            fill=organism.color, outline='')


# size = input("Input width and heighth: ").strip().split()
size = "25 25".strip().split()
size = [int(x) for x in size]
world = World(size[0], size[1])
czlowiek = Czlowiek(0, 0, world)
world.human = czlowiek

size[0] *= 20
size[1] = size[1] * 20 + 100
str_size = [str(x) for x in size]

window = tk.Tk()
window.title("Pavel Harelik 196766")
window.geometry("x".join(str_size))

canvas = tk.Canvas(window, width=size[0], height=size[1]-100)
canvas.pack()

add_hood(window)
draw_world()
window.mainloop()
