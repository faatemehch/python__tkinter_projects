from operator import le
import os
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk

root = Tk()
root.title("Album")
root.geometry("250x210")
root.resizable(False, False)
root.grid_columnconfigure(1, weight=1)

image_list = []
# load images from img directory
for image in os.listdir("ImageSliderAppTkinter/img"):
    if image.endswith("png"):
        path = os.path.join("ImageSliderAppTkinter/img", image)
        img = ImageTk.PhotoImage(Image.open(path).resize((100, 100)))
        image_list.append(img)

img_lbl = Label(root, image=image_list[0])
img_lbl.grid(row=0, column=0, columnspan=3, pady=10)

global img_number
img_number = 0

def backward():
    global img_number
    if img_number != 0:
        img_number -= 1
    else:
        img_number = len(image_list) - 1
    img_lbl["image"] = image_list[img_number]
    status_label["text"] = f'image {img_number+1} of {len(image_list)}'

def forward():
    global img_number
    if img_number < len(image_list) - 1:
        img_number += 1
    else:
        img_number = 0
    img_lbl["image"] = image_list[img_number]
    status_label["text"] = f'image {img_number+1} of {len(image_list)}'
    # lbl.grid_forget() # disapear the label

def upload():
    """
        upload images: save new image into img directory
    """
    global myImage
    root.filename = filedialog.askopenfilename(initialdir="/img", title="Select A File", filetypes=(("png files", "*.png"), ("all files", "*.*")))
    img = Image.open(root.filename).resize((100, 100))
    myImage = ImageTk.PhotoImage(img)
    img.save("ImageSliderAppTkinter/img/"+root.filename.split("/")[-1])
    image_list.append(myImage)


status_label = Label(root, text=f"image {img_number+1} of {len(image_list)}")
backButton = Button(root, text=u"\u00AB", command=backward,width=5)
exitButton = Button(root, text="Exit", command=root.destroy)
forwardButton = Button(root, text=u"\u00BB", command=lambda: forward(),width=5)
uploadBtn = Button(root, text="upload new image".title(), command=upload)

status_label.grid(row=1, column=1)
backButton.grid(row=2, column=0)
exitButton.grid(row=2, column=1)
forwardButton.grid(row=2, column=2)
uploadBtn.grid(row=3, column=0,columnspan=3)

root.mainloop()
