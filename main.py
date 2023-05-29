from world import World
from czlowiek import Czlowiek

import tkinter as tk
import random


def on_button_click():
    print("Кнопка нажата!")


def on_mouse_click(event):
    if (event.x > world.width*20 or event.y > world.height*20):
        return
    print("Мышь нажата на координатах", event.x, event.y)
    print(event)
    create_random_square(event.x, event.y)


def create_random_square(x, y):
    colors = ["red", "green", "blue", "yellow", "orange", "purple"]
    color = random.choice(colors)
    size = 50
    x1 = x - size // 2
    y1 = y - size // 2
    x2 = x + size // 2
    y2 = y + size // 2
    canvas.create_rectangle(x1, y1, x2, y2, fill=color)


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
    world.next_turn()
    draw_world()


def add_hood(window):
    button = tk.Button(window, text="Нажми меня!", command=on_button_click)
    button.pack()

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


size = input("Input width and heighth: ").strip().split()
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

global canvas
canvas = tk.Canvas(window, width=size[0], height=size[1]-100)
canvas.pack()

add_hood(window)

window.mainloop()
