import tkinter as tk
from tkinter import messagebox
import math
import unittest


class CalculatorApp:
    """Основной класс GUI-калькулятора."""

    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.root.title("Калькулятор")
        self.expression = ""
        self.input_text = tk.StringVar()
        self.memory = 0.0
        self.create_widgets()

    def create_widgets(self) -> None:
        """Создаёт виджеты интерфейса калькулятора."""
        input_frame = tk.Frame(
            self.root,
            width=400,
            height=50,
            bd=0,
            highlightbackground="black",
            highlightcolor="black",
            highlightthickness=1,
        )
        input_field = tk.Entry(
            input_frame,
            font=("arial", 18, "bold"),
            textvariable=self.input_text,
            width=50,
            bg="#eee",
            bd=0,
            justify=tk.RIGHT,
        )
        input_field.grid(row=0, column=0)
        input_field.pack(ipady=10)
        input_frame.pack(pady=20)

        btns_frame = tk.Frame(self.root, width=400, height=400, bg="grey")
        btns_frame.pack()

        # Первая строка кнопок
        tk.Button(
            btns_frame,
            text="C",
            fg="black",
            width=10,
            height=3,
            bd=0,
            bg="#eee",
            cursor="hand2",
            command=self.clear,
        ).grid(row=0, column=0, padx=1, pady=1)
        # ... остальные кнопки аналогично

    def btn_click(self, item: str) -> None:
        """Добавляет символ к текущему выражению."""
        self.expression += str(item)
        self.input_text.set(self.expression)

    def evaluate(self) -> None:
        """Вычисляет результат выражения."""
        try:
            result = eval(self.expression)
            self.input_text.set(result)
            self.expression = str(result)
        except Exception:
            messagebox.showerror("Ошибка", "Некорректное выражение")
            self.clear()

    def mem_plus(self) -> None:
        """Добавляет текущее значение в память."""
        try:
            self.memory += float(self.expression)
        except ValueError:
            pass

    def mem_minus(self) -> None:
        """Вычитает текущее значение из памяти."""
        try:
            self.memory -= float(self.expression)
        except ValueError:
            pass

    def clear(self) -> None:
        """Очищает поле ввода."""
        self.expression = ""
        self.input_text.set("")


# --- Математические функции ---

def add(x: float, y: float) -> float:
    """Возвращает сумму x и y."""
    return x + y


def subtract(x: float, y: float) -> float:
    """Возвращает разность x и y."""
    return x - y


def multiply(x: float, y: float) -> float:
    """Возвращает произведение x и y."""
    return x * y


def divide(x: float, y: float) -> float:
    """Возвращает частное x и y. Вызывает ValueError при делении на ноль."""
    if y == 0:
        raise ValueError("Деление на ноль")
    return x / y


def power(x: float, y: float) -> float:
    """Возвращает x в степени y."""
    return x ** y


def sqrt(x: float) -> float:
    """Возвращает квадратный корень из x. Ошибка при x < 0."""
    if x < 0:
        raise ValueError("Корень из отрицательного числа")
    return math.sqrt(x)


# --- Тесты ---

class TestMathFunctions(unittest.TestCase):
    """Тесты для математических функций."""

    def test_add(self) -> None:
        self.assertEqual(add(2, 3), 5)

    def test_subtract(self) -> None:
        self.assertEqual(subtract(5, 3), 2)

    # ... остальные тесты ...


def run_calculator() -> None:
    """Запускает GUI-калькулятор."""
    root = tk.Tk()
    CalculatorApp(root)
    root.mainloop()


if __name__ == "__main__":
    # run_calculator()
    unittest.main()