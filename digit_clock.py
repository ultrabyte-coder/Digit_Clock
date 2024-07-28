import tkinter as tk
from datetime import datetime

root = tk.Tk()

# Убираем рамку окна
root.overrideredirect(True)

# Задаем расположение окна в правом нижнем углу экрана
root.geometry("+1700+1000")


def time():
    """
    Функция для отображения текущего времени.

    Описание:
        Функция получает текущее время и обновляет текст метки label соответствующим значением.
        Затем функция вызывает саму себя через 1 секунду, чтобы обновить время.

    Пример использования:
        >>> time()
    """
    string = datetime.now().strftime('%H:%M:%S')
    label.config(text=string)
    label.after(1000, time)


label = tk.Label(root, font=('calibri', 12, 'bold'), background='black', foreground='white')
label.pack(anchor='se')

# Запускаем функцию time для отображения времени
time()

# Окно поверх всех окон
root.attributes("-topmost", True)

# Запускаем приложение
root.mainloop()