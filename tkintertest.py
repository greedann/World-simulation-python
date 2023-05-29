import tkinter as tk
import random
mouse_click_flag = False

def on_button_click():
    if not mouse_click_flag:
        print("Кнопка нажата!")

def on_mouse_click(event):
    print("Мышь нажата на координатах", event.x, event.y)
    if not mouse_click_flag:
        mouse_click_flag = True
        create_random_square(event.x, event.y)
        mouse_click_flag = False

def on_key_press(event):
    print("Клавиша", event.keysym, "нажата")

def create_random_square(x, y):
    colors = ["red", "green", "blue", "yellow", "orange", "purple"]
    color = random.choice(colors)
    size = 50
    x1 = x - size // 2
    y1 = y - size // 2
    x2 = x + size // 2
    y2 = y + size // 2
    canvas.create_rectangle(x1, y1, x2, y2, fill=color)

# Создание графического окна
window = tk.Tk()
window.title("Пример приложения")
window.geometry("300x200")

# Создание кнопки
button = tk.Button(window, text="Нажми меня!", command=on_button_click)
button.pack(pady=20)

# Создание холста
canvas = tk.Canvas(window, width=300, height=200)
canvas.pack()

# Привязка обработчиков событий
window.bind("<Button-1>", on_mouse_click)
window.bind("<Key>", on_key_press)

# Запуск цикла обработки событий
window.mainloop()
