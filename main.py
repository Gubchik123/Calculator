import tkinter as tk

from math import sqrt


def set_window():
    root = tk.Tk()
    root.title("Calculator")
    root.geometry("700x700+700+50")
    root.resizable(False, False)

    return root


def set_button(text, function):
    btn = tk.Button(command=function,
                    text=text,
                    background="#D8D8D8",
                    activebackground="#A9BCF5",
                    font=("Arial", 35, "bold")
                    )
    return btn


def set_entry():
    entry = tk.Entry(font=("Arial", 47, "normal"),
                     justify="right"
                     )
    return entry


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


def action_sum():     get_action("+")
def action_sub():     get_action("-")
def action_mult():    get_action("*")
def action_div():     get_action("/")
def action_percent(): get_action("%")
def action_square():  get_action("^2")


def action_sqrt():
    get_second_number()
    clean_entry()
    ENTRY.insert(0, str(sqrt(SECOND)))
    clear_numbers_and_action()


def action_plus_minus():
    if "-" in ENTRY.get():
        get_second_number()
        clean_entry()
        ENTRY.insert(0, str(abs(SECOND)))
        clear_numbers_and_action()
    else:
        ENTRY.insert(0, "-")


def get_result():
    global RESULT

    get_second_number()

    try:
        match ACTION:
            case "+":  RESULT = FIRST + SECOND
            case "-":  RESULT = FIRST - SECOND
            case "*":  RESULT = FIRST * SECOND
            case "/":  RESULT = FIRST / SECOND
            case "%":  RESULT = FIRST % SECOND
            case "^2": RESULT = FIRST ** SECOND
    except ZeroDivisionError:
        clean_entry()
        ENTRY.insert(0, "Can't divide by zero!!!   ")
    else:
        ENTRY.insert(0, str(RESULT))
        clear_numbers_and_action()


def clear_numbers_and_action():
    global FIRST, SECOND, RESULT, ACTION

    FIRST = SECOND = RESULT = 1
    ACTION = ""


def clean_entry():
    global ENTRY
    ENTRY.delete(0, tk.END)


def calculator():
    global ENTRY

    window = set_window()
    set_column_and_row_grid_configure(window)

    ENTRY = set_entry()
    ENTRY.grid(row=0, column=0, rowspan=2, columnspan=5, sticky="wens")

    # Buttons with numbers - start
    btn_zero = set_button("0", lambda: ENTRY.insert(tk.END, "0"))
    btn_zero.grid(row=6, column=0, columnspan=2, sticky="wens")
    btn_zero.configure(bg="#E6E6E6")

    btn_one = set_button("1", lambda: ENTRY.insert(tk.END, "1"))
    btn_one.grid(row=5, column=0, sticky="wens")
    btn_one.configure(bg="#E6E6E6")

    btn_two = set_button("2", lambda: ENTRY.insert(tk.END, "2"))
    btn_two.grid(row=5, column=1, sticky="wens")
    btn_two.configure(bg="#E6E6E6")

    btn_tree = set_button("3", lambda: ENTRY.insert(tk.END, "3"))
    btn_tree.grid(row=5, column=2, sticky="wens")
    btn_tree.configure(bg="#E6E6E6")

    btn_four = set_button("4", lambda: ENTRY.insert(tk.END, "4"))
    btn_four.grid(row=4, column=0, sticky="wens")
    btn_four.configure(bg="#E6E6E6")

    btn_five = set_button("5", lambda: ENTRY.insert(tk.END, "5"))
    btn_five.grid(row=4, column=1, sticky="wens")
    btn_five.configure(bg="#E6E6E6")

    btn_six = set_button("6", lambda: ENTRY.insert(tk.END, "6"))
    btn_six.grid(row=4, column=2, sticky="wens")
    btn_six.configure(bg="#E6E6E6")

    btn_seven = set_button("7", lambda: ENTRY.insert(tk.END, "7"))
    btn_seven.grid(row=3, column=0, sticky="wens")
    btn_seven.configure(bg="#E6E6E6")

    btn_eight = set_button("8", lambda: ENTRY.insert(tk.END, "8"))
    btn_eight.grid(row=3, column=1, sticky="wens")
    btn_eight.configure(bg="#E6E6E6")

    btn_nine = set_button("9", lambda: ENTRY.insert(tk.END, "9"))
    btn_nine.grid(row=3, column=2, sticky="wens")
    btn_nine.configure(bg="#E6E6E6")
    # Buttons with numbers - finish

    # Buttons with specials symbol - start
    btn_comma = set_button(".", lambda: ENTRY.insert(tk.END, "."))
    btn_comma.grid(row=6, column=2, sticky="wens")
    btn_comma.configure(bg="#E6E6E6")

    btn_sum = set_button("+", action_sum)
    btn_sum.grid(row=6, column=3, sticky="wens")

    btn_sub = set_button("-", action_sub)
    btn_sub.grid(row=5, column=3, sticky="wens")

    btn_mult = set_button("*", action_mult)
    btn_mult.grid(row=4, column=3, sticky="wens")

    btn_div = set_button("/", action_div)
    btn_div.grid(row=3, column=3, sticky="wens")

    btn_change_symbol = set_button("±", action_plus_minus)
    btn_change_symbol.grid(row=2, column=3, sticky="wens")

    btn_row = set_button("√", action_sqrt)
    btn_row.grid(row=2, column=4, sticky="wens")

    btn_percent = set_button("%", action_percent)
    btn_percent.grid(row=3, column=4, sticky="wens")

    btn_square = set_button("^n", action_square)
    btn_square.grid(row=4, column=4, sticky="wens")
    btn_square.configure(font=("Arial", 30, "bold"))

    btn_equal = set_button("=", get_result)
    btn_equal.grid(row=5, column=4, rowspan=2, sticky="wens")

    btn_clear = set_button("C", clean_entry)
    btn_clear.grid(row=2, column=1, columnspan=2, sticky="wens")

    btn_del_last = set_button("←", lambda: ENTRY.delete(len(ENTRY.get())-1))
    btn_del_last.grid(row=2, column=0, sticky="wens")
    # Buttons with specials symbol - finish

    window.mainloop()


if __name__ == "__main__":
    ENTRY: tk.Entry | None = None

    FIRST: int | float = 1
    SECOND: int | float = 1
    RESULT: int | float = 1
    ACTION: str = ""

    calculator()
