from tkinter import *#импорт всего из модуля tkinter
operation_number = 0
current_number_sum = 0
current_number_minus = 0
current_number_division = 0
current_number_multiply = 0
bin=0
hex=0
oct=0


root = Tk()#окно
#root.geometry('250x400')#размер
root.title("калькулятор")#заголовок
root.config(background="#F3CFC6")#цвет
root.iconbitmap("cat.ico")#иконка
#root.resizable(False,False)#невозможно изменять размер

def button_click(number, entry):
        current_number = e.get()
        e.delete(0, END)
        e.insert(0, str(current_number) + str(number))


def sum_click():
    global current_number_sum, operation_number
    if operation_number == 0:
        new_current_number = 0
        current_number_sum = e.get()
        if current_number_sum != "":
            e.delete(0, END)
            operation_number = 1
        else:
            print("please input a number")
            pass
    elif operation_number == 1:
        new_current_number = e.get()
        e.delete(0,END)
        if "." in str(current_number_sum):
            current_number_sum = float(current_number_sum) + float(new_current_number)
            e.insert(0, current_number_sum)
        else:
            current_number_sum = int(current_number_sum) + int(new_current_number)
            e.insert(0, str(current_number_sum))

def minus_click():
    global current_number_minus, operation_number
    if operation_number == 0:
        new_current_number = 0
        current_number_minus = e.get()
        if current_number_minus != "":
            e.delete(0, END)
            operation_number = 2
        else:
            print("please input a number")
            pass
    elif operation_number == 2:
        new_current_number = e.get()
        e.delete(0,END)
        if "." in str(current_number_minus):
            current_number_minus = float(current_number_minus) - float(new_current_number)
            e.insert(0, current_number_minus)
        else:
            current_number_minus = int(current_number_minus) - int(new_current_number)
            e.insert(0, str(current_number_minus))

def multiply_click():
    global current_number_multiply, operation_number
    if operation_number == 0:
        new_current_number = 0
        current_number_multiply = e.get()
        if current_number_multiply != "":
            e.delete(0, END)
            operation_number = 3
        else:
            print("please input a number")
            pass
    elif operation_number == 3:
        new_current_number = e.get()
        e.delete(0,END)
        if "." in str(current_number_multiply):
            current_number_multiply = float(current_number_multiply) * float(new_current_number)
            e.insert(0, current_number_multiply)
        else:
            current_number_multiply = int(current_number_multiply) * int(new_current_number)
            e.insert(0, str(current_number_multiply))

def division_click():
    global current_number_division, operation_number
    if operation_number == 0:
        new_current_number = 0
        current_number_division = e.get()
        if current_number_division != "":
            e.delete(0, END)
            operation_number = 4
        else:
            print("please input a number")
            pass
    elif operation_number == 4:
        new_current_number = e.get()
        e.delete(0,END)

        try:
            if "." in str(current_number_division):
                current_number_division = float(current_number_division) / float(new_current_number)
                e.insert(0, current_number_division)
            else:
                current_number_division = int(current_number_division) / int(new_current_number)
                e.insert(0, str(current_number_division))
        except ZeroDivisionError:
            e.insert(0, 'Can not divide by zero.')

def toPowerof():
    global current_number_power, operation_number
    current_number_power = e.get()
    if current_number_power != "":
        e.delete(0, END)
        operation_number = 5
    else:
        print("please input a number")
        pass

def positive_negative():
    try:
        current_number = e.get()
        e.delete(0, END)
        if "." in current_number:
            e.insert(0, -(float(current_number)))
        else:
            e.insert(0, -(int(current_number)))
    except:
        print("There is no number")
        pass

def delete():
    try:
        current_number = e.get()
        e.delete(0, END)
        current_number = current_number[:-1]
        e.insert(0, current_number)
    except:
        print("No number to delete")
        pass

def add_point():
    current_number = e.get()
    if "." in current_number:
        print("Number already has a point")
        pass
    else:
        if current_number != "":
            current_number = str(current_number) + str(".")
            e.delete(0,END)
            e.insert(0, current_number)
        else:
            current_number = "0."
            e.insert(0, current_number)

def equals_click():
    global current_number_sum, current_number_minus, current_number_multiply, operation_number
    current_number = e.get()
    e.delete(0, END)
    if operation_number == 0:
        e.insert(0,current_number)
        print("nothing to do")
    elif operation_number == 1:
        if "." in str(current_number_sum):
            e.insert(0, float(current_number_sum) + float(current_number))
            operation_number = 0
        else:
            e.insert(0, int(current_number_sum) + int(current_number))
            operation_number = 0
    elif operation_number == 2:
        if "." in current_number_minus:
            e.insert(0, float(current_number_minus) - float(current_number))
            operation_number = 0
        else:
            e.insert(0, int(current_number_minus) - int(current_number))
            operation_number = 0
    elif operation_number == 3:
        if "." in current_number_multiply:
            e.insert(0, float(current_number_multiply) * float(current_number))
            operation_number = 0
        else:
            e.insert(0, int(current_number_multiply) * int(current_number))
            operation_number = 0
    elif operation_number == 4:

        try:
            if "." in current_number_division:
                e.insert(0, float(current_number_division) / float(current_number))
                operation_number = 0
            else:
                e.insert(0, int(current_number_division) / int(current_number))
                operation_number = 0
        except ZeroDivisionError:
            e.insert(0, 'Can not divide by zero.')

    elif operation_number == 5:
        if "." in current_number_power:
            e.insert(0, float(current_number_power) ** float(current_number))
            operation_number = 0
        else:
            e.insert(0, int(current_number_power) ** int(current_number))
            operation_number = 0

def clear_entry():
    global current_number_sum, current_number_minus, current_number_multiply,current_number_division, operation_number
    operation_number = 0
    current_number_sum = 0
    current_number_multiply = 0
    current_number_minus = 0
    current_number_division = 0
    e.delete(0, END)


def convert_to_bin():
    global bin,hex,oct
    current_number = e.get()
    if current_number == hex:
        current_number = int(current_number, 16)
    elif current_number == oct:
        current_number = int(current_number, 8)
    else:
        current_number = int(current_number)
    bin = ""
    while current_number>0:
        remainder=current_number%2
        bin=str(remainder)+bin
        current_number=current_number//2
    e.delete(0, END)
    e.insert(0, bin)
    """current_number = e.get()
    current_number=int(current_number)
    result=bin(current_number)
    e.delete(0, END)
    e.insert(0,result)"""
def convert_to_oct():
    global bin, hex, oct
    current_number = e.get()
    if current_number==bin:
        current_number = int(current_number,2)
    elif current_number==hex:
        current_number = int(current_number, 16)
    else:
        current_number = int(current_number)
    oct = ""
    while current_number > 0:
        remainder = current_number % 8
        oct = str(remainder) + oct
        current_number = current_number // 8
    e.delete(0, END)
    e.insert(0, oct)
    """current_number = e.get()
    current_number = int(current_number)
    result = oct(current_number)
    e.delete(0, END)
    e.insert(0, result)"""
def convert_to_hex():
    current_number = e.get()
    global bin, hex, oct
    if current_number == bin:
        current_number = int(current_number, 2)
    elif current_number == oct:
        current_number = int(current_number, 8)
    else:
        current_number = int(current_number)
    hex_d = "0123456789ABCDEF"
    hex = ""
    while current_number > 0:
        remainder = current_number % 16
        hex = hex_d[remainder] + hex
        current_number = current_number // 16
    e.delete(0, END)
    e.insert(0, hex)
    """current_number = e.get()
    current_number = int(current_number)
    result = hex(current_number)
    e.delete(0, END)
    e.insert(0, result)"""



e = Entry(width=15, font=("Courier", 15,"bold"),bg="#FFF5EE")#парметры label
button1 = Button(width=6, height=2, text ='1', font=("Courier", 10, "bold"),bg="#FFF5EE", command=lambda: button_click(1, e))#кнопки с цифрами и их пармаетры \ при нажатии обрабатывается функция digit(x)-x установленное значение кнопки прим 9
button2 = Button(width=6, height=2, text ='2', font=("Courier", 10, "bold"),bg="#FFF5EE", command=lambda: button_click(2, e))
button3 = Button(width=6, height=2, text ='3', font=("Courier", 10, "bold"),bg="#FFF5EE",  command=lambda: button_click(3, e))
button4 = Button(width=6, height=2, text ='4', font=("Courier", 10, "bold"),bg="#FFF5EE", command=lambda: button_click(4, e))
button5 = Button(width=6, height=2, text ='5', font=("Courier", 10, "bold"),bg="#FFF5EE", command=lambda: button_click(5, e))
button6 = Button(width=6, height=2, text ='6', font=("Courier", 10, "bold"),bg="#FFF5EE", command=lambda: button_click(6, e))
button7 = Button(width=6, height=2, text ='7', font=("Courier", 10, "bold"),bg="#FFF5EE", command=lambda: button_click(7, e))
button8 = Button(width=6, height=2, text ='8', font=("Courier", 10, "bold"),bg="#FFF5EE", command=lambda: button_click(8, e))
button9 = Button(width=6, height=2, text ='9', font=("Courier", 10, "bold"),bg="#FFF5EE", command=lambda: button_click(9, e))
button0 = Button(width=6, height=2, text ='0', font=("Courier", 10, "bold"),bg="#FFF5EE", command=lambda: button_click(0, e))
buttonC = Button(width=6, height=2, text ='Clear', font=("Courier", 10, "bold"), bg='#E37383',command= lambda: clear_entry())
buttondot=Button(width=6, height=2, text ='.', font=("Courier", 10, "bold"), bg='#E0BFB8', command= lambda: add_point())
button_equal = Button(width=6, height=2, text ='=', font=("Courier", 10, "bold"),bg="#E37383", command= lambda: equals_click())
button_plus = Button(width=6, height=2, text ='+', font=("Courier", 10, "bold"),bg="#E0BFB8", command= lambda: sum_click())
button_minus = Button(width=6, height=2, text ='-', font=("Courier", 10, "bold"),bg="#E0BFB8", command= lambda: minus_click())
button_multy = Button(width=6, height=2, text ='*', font=("Courier", 10, "bold"),bg="#E0BFB8", command= lambda: multiply_click())
button_division = Button(width=6, height=2, text ='/', font=("Courier", 10, "bold"),bg="#E0BFB8", command= lambda: division_click())
button_sqrt = Button(width=6, height=2, text ='**', font=("Courier", 10, "bold"),bg="#E0BFB8")
button_root = Button(width=6, height=2, text ='√', font=("Courier", 10, "bold"),bg="#E0BFB8")
button_bin=Button(width=6, height=2, text ='bin', font=("Courier", 10, "bold"),bg="#E0BFB8",command=convert_to_bin)
button_oct=Button(width=6, height=2, text ='oct', font=("Courier", 10, "bold"),bg="#E0BFB8",command=convert_to_oct)
button_hex=Button(width=6, height=2, text ='hex', font=("Courier", 10, "bold"),bg="#E0BFB8",command=convert_to_hex)
e.grid(row=0, column=0, columnspan=3,  pady=10, ipadx=8, ipady=8, sticky="nsew")
button1.grid(row=1, column=0, sticky="nsew")
button2.grid(row=1, column=1, sticky="nsew")
button3.grid(row=1, column=2, sticky="nsew")
button4.grid(row=2, column=0, sticky="nsew")
button5.grid(row=2, column=1, sticky="nsew")
button6.grid(row=2, column=2, sticky="nsew")
button7.grid(row=3, column=0, sticky="nsew")
button8.grid(row=3, column=1, sticky="nsew")
button9.grid(row=3, column=2, sticky="nsew")
button0.grid(row=4, column=0, sticky="nsew")
buttondot.grid(row=4, column=1, sticky="nsew")
button_equal.grid(row=4, column=2, sticky="nsew")#в процентах размер и сделать фрейм по центру
button_plus.grid(row=5, column=0, sticky="nsew")
button_minus.grid(row=5, column=1, sticky="nsew")
button_multy.grid(row=5, column=2, sticky="nsew")
button_division.grid(row=6, column=0, sticky="nsew")
#button_sqrt.pack()
#button_root.pack()
button_bin.grid(row=7, column=0, sticky="nsew")
button_oct.grid(row=7, column=1, sticky="nsew")
button_hex.grid(row=7, column=2, sticky="nsew")
buttonC.grid(row=6, column=2, sticky="nsew")
for i in range(8):
    root.grid_rowconfigure(i, weight=1)
    root.grid_columnconfigure(i, weight=1)
root.mainloop()
