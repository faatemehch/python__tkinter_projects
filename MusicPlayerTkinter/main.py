from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
import pygame
import os

root = Tk()
root.geometry("550x300")
root.title("MUSIC PLAYER")
# root.config(bg="tomato")

pygame.mixer.init()  # initialize pygame mixer
# global paused
paused = False
songs_path = {}  # make a dictionary to store songs path
isPlaying = False


# ------------------ Functions -----------------
def add_song():
    # just mp3 files
    songs = filedialog.askopenfilenames(initialdir="music/", title="choose a song", filetypes=(("mp3 Files", "*.mp3"),))

    for song in songs:
        basename = os.path.basename(song)  # extract basename of file from whole path
        songs_path[f"{basename}"] = song
        song_box.insert(END, basename)


def play_song():
    song_name = song_box.get(ACTIVE)
    pygame.mixer.music.load(songs_path[song_name])
    pygame.mixer.music.play(loops=0)


def stop_song():
    pygame.mixer.music.stop()
    song_box.selection_clear(ACTIVE)


def pause_song():
    global paused
    if paused:
        pygame.mixer.music.unpause()
        paused = False
    else:
        pygame.mixer.music.pause()
        paused = True


def previous_song():
    current_song = song_box.curselection()[0]  # the index of currently selected item
    previous_song_name = song_box.get(current_song - 1)
    next_song_path = songs_path[f"{previous_song_name}"]
    song_box.selection_clear(current_song)
    song_box.selection_set(current_song - 1)
    pygame.mixer.music.load(next_song_path)
    pygame.mixer.music.play(loops=0)


def next_song():
    current_song = song_box.curselection()[0]  # the index of currently selected item
    next_song_name = song_box.get(current_song + 1)
    next_song_path = songs_path[f"{next_song_name}"]
    song_box.selection_clear(current_song)
    song_box.selection_set(current_song + 1)
    pygame.mixer.music.load(next_song_path)
    pygame.mixer.music.play(loops=0)


# ------------------- Widgets ------------------
# song listbox
song_box = Listbox(root, bg="black", fg="white", selectbackground="white", selectforeground="black", width=60,
                   font=("arial", 15))
song_box.pack(pady=20)
# button images
back_img = ImageTk.PhotoImage(Image.open("MusicPlayerTkinter/img/back.png").resize((32, 32)))
forward_img = ImageTk.PhotoImage(Image.open("MusicPlayerTkinter/img/forward.png").resize((32, 32)))
play_img = ImageTk.PhotoImage(Image.open("MusicPlayerTkinter/img/play.png").resize((32, 32)))
stop_img = ImageTk.PhotoImage(Image.open("MusicPlayerTkinter/img/stop.png").resize((32, 32)))
pause_img = ImageTk.PhotoImage(Image.open("MusicPlayerTkinter/img/pause.png").resize((32, 32)))
# Player Frame
player_frame = Frame(root)
player_frame.pack()
# add button
back_btn = Button(player_frame, image=back_img, borderwidth=0, bd=0, command=previous_song)
forward_btn = Button(player_frame, image=forward_img, borderwidth=0, bd=0, command=next_song)
play_btn = Button(player_frame, image=play_img, borderwidth=0, bd=0, command=play_song)
pause_btn = Button(player_frame, image=pause_img, borderwidth=0, bd=0, command=pause_song)
stop_btn = Button(player_frame, image=stop_img, borderwidth=0, bd=0, command=stop_song)
# grid btn
back_btn.grid(row=0, column=0, padx=10)
forward_btn.grid(row=0, column=4, padx=10)
play_btn.grid(row=0, column=3, padx=10)
pause_btn.grid(row=0, column=1, padx=10)
stop_btn.grid(row=0, column=2, padx=10)
#  Create Menu
menu = Menu(root)
root.config(menu=menu)
add_song_menu = Menu(menu)
menu.add_cascade(label="File", menu=add_song_menu)
add_song_menu.add_command(label="Add New Song", command=add_song)

# ----------------------------------------------
root.mainloop()
