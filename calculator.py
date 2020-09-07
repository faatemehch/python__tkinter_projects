from tkinter import *
import tkinter.messagebox

# ======================== setting ===========================
root = Tk()
root.geometry('700x300')
root.resizable(width=FALSE, height=FALSE)
root.title('calculator')
color = 'white'
root.configure('color')
# ======================== variables ===========================
number = StringVar()
num1 = ''
num2 = ''
off_on = 'off'
# ======================== frames ===========================
top_first = Frame(root, width=400, height=100, bg=color)
top_first.pack(side=TOP)

top_second = Frame(root, width=400, height=100, bg=color)
top_second.pack(side=TOP)

top_third = Frame(root, width=400, height=100, bg=color)
top_third.pack(side=TOP)


# ======================== functions ===========================
def errorMsg(msg):
    if msg == 'error':
        tkinter.messagebox.showerror('Error', 'something went wrong!')
    elif msg == 'division zero error':
        tkinter.messagebox.showerror('Division Error', 'cannot divide by 0!')


def click(x):
    a = number.get()
    a += x
    number.set(a)


def clear():
    global num1, num2, off_on
    number.set('')
    off_on = ''
    num1 = ''
    num2 = ''


def plus():
    global num1
    global off_on
    num1 = number.get()
    number.set('')
    off_on = 'plus_on'


def minus():
    global num1
    global off_on
    num1 = number.get()
    number.set('')
    off_on = 'minus_on'


def mul():
    global num1
    global off_on
    num1 = number.get()
    off_on = 'mul_on'
    number.set('')


def div():
    global num1
    global off_on
    num1 = number.get()
    number.set('')
    off_on = 'div_on'


def equ(off_on, num1):
    num2 = number.get()
    if off_on == 'plus_on':
        try:
            number.set(float(num1) + float(num2))
            off_on = 'off'
        except:
            errorMsg('error')
    elif off_on == 'minus_on':
        try:
            number.set(float(num1) - float(num2))
        except:
            errorMsg('error')
    elif off_on == 'mul_on':
        try:
            number.set(float(num1) * float(num2))
        except:
            errorMsg('error')
    elif off_on == 'div_on':
        try:
            number.set(float(num1) / float(num2))
        except ZeroDivisionError:
            errorMsg('division zero error')
        except:
            errorMsg('error')
    else:
        errorMsg('error')

# ======================== buttons ===========================
btn_plus = Button(top_third, text='+', width=10, highlightbackground=color,
                  command=lambda: plus())
btn_plus.pack(side=LEFT, padx=10, pady=20)

btn_minus = Button(top_third, text='-', width=10, highlightbackground=color,
                   command=lambda: minus())
btn_minus.pack(side=LEFT, padx=10, pady=20)

btn_mul = Button(top_third, text='*', width=10, highlightbackground=color,
                 command=lambda: mul(), )
btn_mul.pack(side=LEFT, padx=10, pady=20)

btn_div = Button(top_third, text='/', width=10, highlightbackground=color,
                 command=lambda: div())
btn_div.pack(side=LEFT, padx=10, pady=20)

btn_equ = Button(top_third, text='=', width=10, highlightbackground=color,
                 command=lambda: equ(off_on, num1))
btn_equ.pack(side=LEFT, padx=10, pady=20)

btn_clear = Button(top_third, text='C', width=10, highlightbackground=color,
                   command=lambda: clear())
btn_clear.pack(side=LEFT, padx=10, pady=20)

# -----
zero_btn = Button(top_second, text='0', width=5, highlightbackground=color, command=lambda: click('0'), fg='red')
zero_btn.pack(side=LEFT, padx=5, pady=20)

one_btn = Button(top_second, text='1', width=5, highlightbackground=color, command=lambda: click('1'), fg='red')
one_btn.pack(side=LEFT, padx=5, pady=20)

two_btn = Button(top_second, text='2', width=5, highlightbackground=color, command=lambda: click('2'), fg='red')
two_btn.pack(side=LEFT, padx=5, pady=20)

three_btn = Button(top_second, text='3', width=5, highlightbackground=color, command=lambda: click('3'), fg='red')
three_btn.pack(side=LEFT, padx=5, pady=20)

four_btn = Button(top_second, text='4', width=5, highlightbackground=color, command=lambda: click('4'), fg='red')
four_btn.pack(side=LEFT, padx=5, pady=20)

five_btn = Button(top_second, text='5', width=5, highlightbackground=color, command=lambda: click('5'), fg='red')
five_btn.pack(side=LEFT, padx=5, pady=20)

six_btn = Button(top_second, text='6', width=5, highlightbackground=color, command=lambda: click('6'), fg='red')
six_btn.pack(side=LEFT, padx=5, pady=20)

seven_btn = Button(top_second, text='7', width=5, highlightbackground=color, command=lambda: click('7'), fg='red')
seven_btn.pack(side=LEFT, padx=5, pady=20)

eight_btn = Button(top_second, text='8', width=5, highlightbackground=color, command=lambda: click('8'), fg='red')
eight_btn.pack(side=LEFT, padx=5, pady=20)

nine_btn = Button(top_second, text='9', width=5, highlightbackground=color, command=lambda: click('9'), fg='red')
nine_btn.pack(side=LEFT, padx=5, pady=20)

# ======================== entries and labels ===========================
label_get_num = Label(top_first, text='Input Number: ', bg=color)
label_get_num.pack(side=LEFT, padx=10, pady=20)
get_num = Entry(top_first, highlightbackground=color, textvariable=number, bg='yellow')
get_num.pack(side=LEFT, padx=10, pady=20)

root.mainloop()
