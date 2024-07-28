import tkinter as tk
from datetime import datetime
import unittest


class TestTimeApp(unittest.TestCase):
    """
    Класс для тестирования приложения Tkinter, которое отображает текущее время.
    """

    def setUp(self):
        """
        Инициализирует окно Tkinter и метку, которая будет отображать текущее время.
        """
        self.root = tk.Tk()
        self.root.overrideredirect(True)
        self.root.geometry("+1700+1000")
        self.label = tk.Label(self.root, font=('calibri', 12, 'bold'), background='black', foreground='white')
        self.label.pack(anchor='se')

    def test_time_function(self):
        """
        Тестирует функцию time, которая обновляет метку с текущим временем.
        """
        string = datetime.now().strftime('%H:%M:%S')
        self.time()
        self.assertEqual(self.label.cget("text"), string)

    def test_window_position(self):
        """
        Тестирует позицию окна Tkinter.
        """
        self.root.update_idletasks()
        self.assertEqual(self.root.winfo_x(), 1700)
        self.assertEqual(self.root.winfo_y(), 1000)

    def test_window_on_top(self):
        """
        Тестирует, что окно Tkinter находится поверх всех других окон.
        """
        self.root.attributes("-topmost", True)
        self.root.update_idletasks()
        self.assertTrue(self.root.winfo_ismapped())

    def tearDown(self):
        """
        Закрывает окно Tkinter.
        """
        self.root.quit()
        self.root = None

    def time(self):
        """
        Обновляет метку с текущим временем и вызывает сам себя через 1000 миллисекунд, чтобы обновить время.
        """
        string = datetime.now().strftime('%H:%M:%S')
        self.label.config(text=string)
        self.label.after(1000, self.time)


if __name__ == '__main__':
    unittest.main()