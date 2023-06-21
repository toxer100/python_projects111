from tkinter import *

root = Tk()

# Создаем текстовое поле и кнопку "Добавить"
text_entry = Entry(root)
add_button = Button(root, text="Добавить")

# Функция для добавления нового текстового поля
def add_text_entry():
    new_entry = Entry(root)
    new_entry.pack()

# Устанавливаем функцию для кнопки "Добавить"
add_button.config(command=add_text_entry)

# Размещаем элементы на форме
text_entry.pack()
add_button.pack()

root.mainloop()