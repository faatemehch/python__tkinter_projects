from tkinter import *
from game import *
from tkinter import messagebox

root = Tk()
root.geometry("400x300")
root.config(bg="tomato")
root.title("FLAG RECOGNITION")
root.resizable(False, False)
# root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

def signin():
    username = name_entry.get()
    with open("flagRecognitionGameTkinter/players.txt", 'r') as f:
        for line in f.readlines():
            if "," in line:
                name, score = line.split(",")
                if username == name:
                    print("yes user exist")
                    game_window(root, username) # enter the game
                    break
        else:
            messagebox.showwarning(messagebox.WARNING, f"Ops. {username} Not Found. Signup First.")
            print("User Not Found.")

def signup():
    username = name_entry.get()
    with open("players.txt", 'a') as f:
        f.write(f"\n{username},0")
    name_entry.delete(0, END)

welcomLabel= Label(root, text="Welcome To Flag Recognition Game", fg="blue", font=("Arial", 22, "bold"))
# welcomLabel.grid_columnconfigure(0, weight=1)
welcomLabel.grid(row=0, column=0, columnspan=3, pady=5,padx=2)

name_label = Label(root, text="Name:", fg="black", font=("Helvetica", 15, "bold"))
name_label.grid(pady=10, row=1,column=0, sticky="w", padx=10)

name_entry = Entry(root,font=("Arial", 20))
name_entry.grid(pady=10, row=1,column=1, sticky="w", padx=(1, 50))

login_btn = Button(root, text="Login", command=signin)
login_btn.grid(pady=10, padx=10, row=2,column=0)

signuo_btn = Button(root, text="Signup", command=signup)
signuo_btn.grid(pady=10, row=3,column=0)

exit_btn = Button(root, text="Exit", command=root.destroy)
exit_btn.grid(pady=10, row=4, column=0)

root.mainloop()