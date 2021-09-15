# TODO: optimize functions to avoid needless repetition of code

from tkinter import *

root = Tk()
root.title("Calculator")
root.config(bg="#ADD8E6", padx=10)
root.geometry("395x495")
root.resizable(width=False, height=False)
# Creating a Label Widget, defining it
myLabel = Label(root)
# showing the label on the screen, packing it in
myLabel.grid()


def button_click(number):
    current = text_field.get()
    text_field.delete(0, END)
    if str(current) == str(number) == "0":
        text_field.insert(0, str(current))
    else:
        text_field.insert(0, str(current) + str(number))


def button_clear():
    text_field.delete(0, END)
    addition_sign.config(state=NORMAL)
    subtraction_sign.config(state=NORMAL)
    division_sign.config(state=NORMAL)
    multiplication_sign.config(state=NORMAL)


# creating a field
text_field = Entry(root, width=35, borderwidth=5)
text_field.grid(row=0, column=0, columnspan=4, padx=20, pady=20)


# defining buttons
def button_addition():
    try:
        first_number = text_field.get()
        global f_num
        global operation
        operation = "addition"
        f_num = float(first_number)

        text_field.delete(0, END)
        addition_sign.config(state=DISABLED)
        subtraction_sign.config(state=DISABLED)
        division_sign.config(state=DISABLED)
        multiplication_sign.config(state=DISABLED)

    except ValueError:
        button_clear()


def button_subtraction():
    try:
        first_number = text_field.get()
        global f_num
        global operation
        operation = "subtraction"
        f_num = float(first_number)

        text_field.delete(0, END)
        addition_sign.config(state=DISABLED)
        subtraction_sign.config(state=DISABLED)
        division_sign.config(state=DISABLED)
        multiplication_sign.config(state=DISABLED)

    except ValueError:
        button_clear()


def button_multiplication():
    try:
        first_number = text_field.get()
        global f_num
        global operation
        operation = "multiplication"
        f_num = float(first_number)

        text_field.delete(0, END)
        addition_sign.config(state=DISABLED)
        subtraction_sign.config(state=DISABLED)
        division_sign.config(state=DISABLED)
        multiplication_sign.config(state=DISABLED)

    except ValueError:
        button_clear()


def button_division():
    try:
        first_number = text_field.get()
        global f_num
        global operation
        operation = "division"
        f_num = float(first_number)

        text_field.delete(0, END)
        addition_sign.config(state=DISABLED)
        subtraction_sign.config(state=DISABLED)
        division_sign.config(state=DISABLED)
        multiplication_sign.config(state=DISABLED)

    except ValueError:
        button_clear()


def button_equal():
    second_number = text_field.get()
    text_field.delete(0, END)
    result = ""

    if operation == "division":
        if second_number == 0:
            result = "cannot divide by zero"
            button_clear()
        else:
            result = f_num / float(second_number)
    elif operation == "subtraction":
        result = f_num - float(second_number)
    elif operation == "addition":
        result = f_num + float(second_number)
    elif operation == "multiplication":
        result = f_num * float(second_number)

    text_field.insert(0, result)
    addition_sign.config(state=NORMAL)
    subtraction_sign.config(state=NORMAL)
    division_sign.config(state=NORMAL)
    multiplication_sign.config(state=NORMAL)


# creating a button
addition_sign = Button(root, text="+", bg="#FAF0E6", padx=36, pady=21, command=button_addition)
subtraction_sign = Button(root, text="-", bg="#FAF0E6", padx=37, pady=21, command=button_subtraction)
division_sign = Button(root, text="/", bg="#FAF0E6", padx=39, pady=21, command=button_division)
multiplication_sign = Button(root, text="*", bg="#FAF0E6", padx=41, pady=21, command=button_multiplication)
equal_sign = Button(root, text="=", bg="#FAF0E6", padx=39, pady=96, command=button_equal)

# button clear
clear_button = Button(root, text="Clear all", padx=64, pady=40, command=button_clear)

addition_sign.grid(row=1, column=0)
subtraction_sign.grid(row=1, column=1)
division_sign.grid(row=1, column=2)
multiplication_sign.grid(row=1, column=3)

number_0 = Button(root, text="0", bg="#DCDCDC", padx=83, pady=40, command=lambda: button_click(0))
number_1 = Button(root, text="1", bg="#DCDCDC", padx=37, pady=21, command=lambda: button_click(1))
number_2 = Button(root, text="2", bg="#DCDCDC", padx=37, pady=21, command=lambda: button_click(2))
number_3 = Button(root, text="3", bg="#DCDCDC", padx=37, pady=21, command=lambda: button_click(3))
number_4 = Button(root, text="4", bg="#DCDCDC", padx=37, pady=21, command=lambda: button_click(4))
number_5 = Button(root, text="5", bg="#DCDCDC", padx=37, pady=21, command=lambda: button_click(5))
number_6 = Button(root, text="6", bg="#DCDCDC", padx=37, pady=21, command=lambda: button_click(6))
number_7 = Button(root, text="7", bg="#DCDCDC", padx=37, pady=21, command=lambda: button_click(7))
number_8 = Button(root, text="8", bg="#DCDCDC", padx=37, pady=21, command=lambda: button_click(8))
number_9 = Button(root, text="9", bg="#DCDCDC", padx=37, pady=21, command=lambda: button_click(9))

# Putting the buttons on the screen
number_7.grid(row=2, column=0)
number_8.grid(row=2, column=1)
number_9.grid(row=2, column=2)
equal_sign.grid(row=2, column=3, rowspan=3)

number_4.grid(row=3, column=0)
number_6.grid(row=3, column=2)
number_5.grid(row=3, column=1)

number_1.grid(row=4, column=0)
number_3.grid(row=4, column=2)
number_2.grid(row=4, column=1)

number_0.grid(row=5, column=0, columnspan=2)
clear_button.grid(row=5, column=2, columnspan=2)

# displaying everything
root.mainloop()
