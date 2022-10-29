from tkinter import *
from random import *
from PIL import Image, ImageTk
import os

def hide_all_frames():
    for widget in countries_frame.winfo_children():
        widget.destroy()
    countries_frame.pack_forget()

def read_records(username):
    with open("flagRecognitionGameTkinter/players.txt", 'r') as f:
        for line in f.readlines():
            if "," in line:
                name, score = line.split(",")
                if name == username:
                    return score

def update_score(username):
    with open("flagRecognitionGameTkinter/players.txt", "r") as f:
        lines = f.readlines()    
    print(lines)     
    with open("flagRecognitionGameTkinter/players.txt", "w") as f:
        for line in lines:
            if "," in line:
                print(line)
                name, score = line.split(",")
                if name ==  "fateme":
                    f.write(f"\n{name},{user_score}")
                else:
                    score = score.replace("\n", "")
                    f.write(f"\n{name},{score}")

def load_countries():
        # load images
        country_names = []
        country_images = []
        for image in os.listdir("flagRecognitionGameTkinter/flag_img"):
            if image.endswith("png"):
                path = os.path.join("flag_img", image)
                slash, dot = path.index("/"), path.index(".")
                country_names.append(path[slash+1:dot])
                img = ImageTk.PhotoImage(Image.open("flagRecognitionGameTkinter/"+path).resize((80, 80)))
                country_images.append(img)
        return country_names, country_images

def check_answer():
    global user_score
    if answer_input.get().lower() == country_names[idx]:
        answer_label.config(text=u"Correct \U0001F44D", fg="green")
        user_score += 1
        score_label.config(text=f"your score: {user_score}")
        update_score("fateme")
    else:
        answer_label.config(text=u"Incorrect \U0001F44E", fg="red") 

def game_entities(): 
    global idx
    global imageLabel
    global answer_input
    global answer_label

    hide_all_frames()
    
    idx = randint(0, len(country_names)-1) # random index of country_names 
    countries_frame.pack(fill=BOTH, expand=1) # pack the frame

    imageLabel = Label(countries_frame, image=country_images[idx]) # show country image
    imageLabel.pack(pady=5)

    # textLabel = Label(countries_frame, text=country_names[idx]) # show country name
    # textLabel.pack(pady=5) # show correct answer

    answer_input = Entry(countries_frame, font=("Helvetica", 15), bg="white", bd=1) # enter your geuss
    answer_input.pack(pady=5)
    answer_input.focus_set()

    random_button = Button(countries_frame, text="next", command=game_entities)
    random_button.pack(pady=5)

    check_button = Button(countries_frame, text="Check Your Answer", command=check_answer)
    check_button.pack(pady=5)

    answer_label = Label(countries_frame, font=("Helvetica", 18))
    answer_label.pack(pady=10)

def game_window(root, username):
    print(username)
    global countries_frame
    global user_score, score_label
    global country_names, country_images
    game_win = Toplevel(root)
    game_win.title(f"{username} Account")
    game_win.geometry("400x300")
    game_win.config(bg="pink")
    user_score = int(read_records(username))
    score_label = Label(game_win, text=f"your score: {user_score}")
    score_label.pack(padx=5, pady=5)
    # load name and image of countries
    country_names, country_images = load_countries()
    countries_frame =  Frame(game_win, width=400, height=250)
    game_entities()
    game_win.mainloop()

# game_window("fateme")       