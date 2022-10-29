from tkinter import *
import tkinter.messagebox

# ======================== setting ===========================
root = Tk()
root.geometry('300x230')
root.resizable(width=FALSE, height=FALSE)
root.title('calculator')
color = 'dodgerblue'
# root.configure('color')
# ======================== variables ===========================
number = StringVar()
num1 = ''
num2 = ''
off_on = 'off'
# ======================== frames ===========================
top_first = Frame(root, width=400, height=100, bg=color)
top_first.grid(row=0,column=0, ipadx=1,ipady=5, columnspan=2, sticky="NESW")

top_second = Frame(root, width=400, height=100, bg=color)
top_second.grid(row=1,column=0, ipadx=13, sticky="NESW")

top_third = Frame(root, width=400, height=100, bg=color)
top_third.grid(row=2,column=0, ipadx=25,ipady=3, sticky="NESW")
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
btn_plus = Button(top_third, text='+', width=6, highlightbackground=color,
                  command=lambda: plus())
btn_plus.grid(row=0,column=2, padx=5, pady=2)

btn_minus = Button(top_third, text='-', width=6, highlightbackground=color,
                   command=lambda: minus())
btn_minus.grid(row=1,column=1, padx=5, pady=2)

btn_mul = Button(top_third, text='*', width=6, highlightbackground=color,
                 command=lambda: mul(), )
btn_mul.grid(row=1,column=0, padx=5, pady=2)

btn_div = Button(top_third, text='/', width=6, highlightbackground=color,
                 command=lambda: div())
btn_div.grid(row=1,column=2, padx=5, pady=2)

btn_equ = Button(top_third, text='=', width=16, highlightbackground=color,
                 command=lambda: equ(off_on, num1))
btn_equ.grid(row=0,column=0, padx=5, pady=2, columnspan=2, ipadx=5)

btn_clear = Button(top_second, text='C', width=16, highlightbackground=color,
                   command=lambda: clear())
btn_clear.grid(row=3, column=1, padx=1, pady=2, columnspan=2, ipadx=5)

# -----
zero_btn = Button(top_second, text='0', width=6, highlightbackground=color, command=lambda: click('0'), fg='red')
zero_btn.grid(row=3,column=0,padx=5, pady=2)

one_btn = Button(top_second, text='1', width=6, highlightbackground=color, command=lambda: click('1'), fg='red')
one_btn.grid(row=2,column=2, padx=5, pady=2)

two_btn = Button(top_second, text='2', width=6, highlightbackground=color, command=lambda: click('2'), fg='red')
two_btn.grid(row=2,column=1, pady=2)

three_btn = Button(top_second, text='3', width=6, highlightbackground=color, command=lambda: click('3'), fg='red')
three_btn.grid(row=2,column=0,padx=5, pady=2)

four_btn = Button(top_second, text='4', width=6, highlightbackground=color, command=lambda: click('4'), fg='red')
four_btn.grid(row=1,column=2, padx=5, pady=2)

five_btn = Button(top_second, text='5', width=6, highlightbackground=color, command=lambda: click('5'), fg='red')
five_btn.grid(row=1,column=1, padx=5, pady=2)

six_btn = Button(top_second, text='6', width=6, highlightbackground=color, command=lambda: click('6'), fg='red')
six_btn.grid(row=1,column=0, pady=2, padx=5)

seven_btn = Button(top_second, text='7', width=6, highlightbackground=color, command=lambda: click('7'), fg='red')
seven_btn.grid(row=0,column=2, padx=5, pady=2)

eight_btn = Button(top_second, text='8', width=6, highlightbackground=color, command=lambda: click('8'), fg='red')
eight_btn.grid(row=0,column=1, padx=5, pady=2)

nine_btn = Button(top_second, text='9', width=6, highlightbackground=color, command=lambda: click('9'), fg='red')
nine_btn.grid(row=0,column=0, padx=5, pady=2)

# ======================== entries and labels ===========================
label_get_num = Label(top_first, text='Input Number:', bg=color)
label_get_num.grid(row=0, column=0,sticky="NESW")
get_num = Entry(top_first, highlightbackground=color, textvariable=number, bg='yellow')
get_num.grid(row=0, column=1, sticky="W")

root.mainloop()
