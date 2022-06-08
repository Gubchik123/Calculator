import tkinter as tk

from math import sqrt


def make_window():
    root = tk.Tk()
    root.title("Calculator")
    root.geometry("700x700+700+50")
    root.resizable(False, False)

    return root


def make_entry():
    return tk.Entry(font=("Arial", 47, "normal"), justify="right")


def digit_button(digit):
    return tk.Button(command=lambda: add_digit(digit),
                     text=digit, bg="#E6E6E6", activebackground="#A9BCF5",
                     font=("Arial", 35, "bold"))


def operation_button(operation):
    return tk.Button(command=lambda: get_action(operation),
                     text=operation, bg="#D8D8D8", activebackground="#A9BCF5",
                     font=("Arial", 35, "bold"))


def special_button(text: str, function):
    return tk.Button(command=function,
                     text=text, bg="#D8D8D8", activebackground="#A9BCF5",
                     font=("Arial", 35, "bold"))


def set_column_and_row_grid_configure(root: tk.Tk):
    for i in range(5):
        root.grid_columnconfigure(i, minsize=100)

    for i in range(7):
        root.grid_rowconfigure(i, minsize=100)


def get_first_number():
    global FIRST

    try:
        if "." in ENTRY.get():
            FIRST = float(ENTRY.get())
        else:
            FIRST = int(ENTRY.get())
    except ValueError:
        pass
    finally:
        clean_entry()


def get_second_number():
    global SECOND

    try:
        if "." in ENTRY.get():
            SECOND = float(ENTRY.get())
        else:
            SECOND = int(ENTRY.get())
    except ValueError:
        pass
    finally:
        clean_entry()


def get_action(action: str):
    global ACTION
    ACTION = action
    get_first_number()


def action_sqrt():
    get_second_number()
    clean_entry()
    ENTRY.insert(0, str(sqrt(SECOND)))


def action_plus_minus():
    if "-" in ENTRY.get():
        get_second_number()
        clean_entry()
        ENTRY.insert(0, str(abs(SECOND)))
    elif ENTRY.get()[0] == "0":
        pass
    else:
        ENTRY.insert(0, "-")


def action_clean_all():
    ENTRY.delete(0, tk.END)
    ENTRY.insert(0, "0")


def action_clean_last():
    if ENTRY.get()[0] == "0":
        pass
    else:
        ENTRY.delete(len(ENTRY.get()) - 1)


def add_digit(digit):
    try:
        if ENTRY.get()[0] == "0":
            ENTRY.delete(ENTRY.get()[0])
    except IndexError:
        pass
    finally:
        ENTRY.insert(tk.END, str(digit))


def get_result():
    global RESULT

    get_second_number()
    clean_entry()

    try:
        match ACTION:
            case "+":  RESULT = FIRST + SECOND
            case "-":  RESULT = FIRST - SECOND
            case "*":  RESULT = FIRST * SECOND
            case "/":  RESULT = FIRST / SECOND
            case "%":  RESULT = FIRST % SECOND
            case "^n": RESULT = FIRST ** SECOND
    except ZeroDivisionError:
        clean_entry()
        ENTRY.insert(0, "Can't divide by zero!!!   ")
    else:
        ENTRY.insert(0, str(RESULT))


def clean_entry():
    ENTRY.delete(0, tk.END)


FIRST: int | float = 1
SECOND: int | float = 1
RESULT: int | float = 1
ACTION: str = ""

window = make_window()
set_column_and_row_grid_configure(window)

ENTRY = make_entry()
ENTRY.insert(0, "0")
ENTRY.grid(row=0, column=0, rowspan=2, columnspan=5, sticky="wens")

# Buttons with numbers - start
digit_button("0").grid(row=6, column=0, columnspan=2, sticky="wens")
num = 1
for row in range(3, 6):
    for column in range(3):
        digit_button(f"{num}").grid(row=row, column=column, sticky="wens")
        num += 1
# Buttons with numbers - finish

# Buttons with symbol - start
digit_button(".").grid(row=6, column=2, sticky="wens")
operation_button("+").grid(row=6, column=3, sticky="wens")
operation_button("-").grid(row=5, column=3, sticky="wens")
operation_button("*").grid(row=4, column=3, sticky="wens")
operation_button("/").grid(row=3, column=3, sticky="wens")
operation_button("%").grid(row=3, column=4, sticky="wens")
operation_button("^n").grid(row=4, column=4, sticky="wens")

special_button("±", action_plus_minus).grid(row=2, column=3, sticky="wens")
special_button("√", action_sqrt).grid(row=2, column=4, sticky="wens")
special_button("=", get_result).grid(row=5, column=4, rowspan=2, sticky="wens")
special_button("C", action_clean_all).grid(row=2, column=1, columnspan=2, sticky="wens")
special_button("←", action_clean_last).grid(row=2, column=0, sticky="wens")
# Buttons with symbol - finish

window.mainloop()
