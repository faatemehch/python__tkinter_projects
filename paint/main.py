from tkinter import *
from tkinter.colorchooser import askcolor
import time
from PIL import Image, ImageDraw

root = Tk()
root.geometry("526x650")
root.title("Paint")
root.resizable(False, False)

# default values
color = "black"
backgroundColor = "white"
pensize = 5
# create new image
image = Image.new('RGB', (526,650), backgroundColor)
draw = ImageDraw.Draw(image)
# -------------------------------------
# ------------- functions -------------
# -------------------------------------
def change_color():
    global color
    color = askcolor()[1]
    print(color)

def paint(event):
    oldx, oldy = event.x, event.y
    newx, newy = oldx+1, oldy+1
    canvas.create_line((oldx, oldy, newx, newy), fill=f"{color}", width=pensize)
    wh_label.config(text=f"({event.x}, {event.y})")
    draw.line((oldx, oldy, newx, newy), fill=f"{color}", width=int(pensize))

def motion(event):
    wh_label.config(text=f"({event.x}, {event.y})")

def change_background_color():
    global backgroundColor
    bgcolor = askcolor()[1]
    canvas.config(bg=bgcolor)

def change_pensize(value):
    global pensize
    pensize = clicked.get()

def clear():
    canvas.delete('all')

def save():
    global image_number
    filename = f'image_{time.time()}.png' 
    image.save(f"paint/{filename}")
# -------------------------------------
# ------------- widgets ---------------
# -------------------------------------
canvas = Canvas(root, bg="white", width=500, height=500)
canvas.grid(row=1, column=0, pady=10, padx=10, columnspan=12)
# -------------------------------------
change_color_btn = Button(root, text="change color", command=change_color)
change_color_btn.grid(row=2, column=2, pady=15)
# -------------------------------------
pensize_label = Label(root, text="pensize:", fg="white")
pensize_label.grid(row=2, column=0, pady=15, padx=10)
# -------------------------------------
options = range(1, 50)
clicked = StringVar()
clicked.set(pensize)
change_pensize_options = OptionMenu(root,  clicked, *options, command=change_pensize)
change_pensize_options.grid(row=2, column=1, pady=15)
# -------------------------------------
clear_button = Button(root, text="🗑", command=clear)
clear_button.grid(row=2, column=3, ipadx=25)
# -------------------------------------
change_background_color = Button(root, text="Background color", command=change_background_color)
change_background_color.grid(row=2, column=4)
# -------------------------------------
wh_label = Label(root, text="")
wh_label.grid(row=0, column=0,padx=15, columnspan=12)
# -------------------------------------
save_button = Button(root, text="save", command=save)
save_button.grid(row=3, column=0,ipadx=220, columnspan=12)
# -------------------------------------
canvas.bind("<B1-Motion>", paint)
canvas.bind("<Motion>", motion)
# -------------------------------------
root.mainloop()