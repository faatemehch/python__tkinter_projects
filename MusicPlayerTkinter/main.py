from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
from mutagen.mp3 import MP3
import tkinter.ttk as ttk
import pygame
import time
import os

root = Tk()
root.geometry("570x380")
root.title("MUSIC PLAYER")
root.resizable(False, False)
# root.config(bg="tomato")

pygame.mixer.init()  # initialize pygame mixer
# ------------------ Variables -----------------
# global paused
paused = False
songs_path = {}  # make a dictionary to store songs path
after_id = None

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
    print(song_name, songs_path[song_name])
    pygame.mixer.music.load(songs_path[song_name])
    pygame.mixer.music.play(loops=0)
    song_duration()

def stop_song():
    pygame.mixer.music.stop()
    song_box.selection_clear(ACTIVE)
    remaining_time_label.config(text="")
    total_time_label.config(text="")
    if after_id is not None:
        remaining_time_label.after_cancel(after_id)

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
    song_box.activate(current_song - 1)
    song_box.selection_set(current_song - 1)
    play_song()
    # pygame.mixer.music.load(next_song_path)
    # pygame.mixer.music.play(loops=0)


def next_song():
    current_song = song_box.curselection()[0]  # the index of currently selected item
    next_song_name = song_box.get(current_song + 1)
    next_song_path = songs_path[f"{next_song_name}"]
    song_box.selection_clear(current_song)
    song_box.activate(current_song + 1)
    song_box.selection_set(current_song + 1)
    play_song()
    # pygame.mixer.music.load(next_song_path)
    # pygame.mixer.music.play(loops=0)


def song_duration():
    global after_id
    current_time = pygame.mixer.music.get_pos()  # ms
    # ------------- song length -------------
    # current_song_idx = song_box.curselection()[0]
    song_name = song_box.get(ACTIVE)
    current_song_path = songs_path[f"{song_name}"]
    length = MP3(current_song_path).info.length
    total = time.strftime("%M:%S", time.gmtime(length))
    # ----------------------------------------
    # formatted = str(datetime.timedelta(seconds=current_time // 1000))
    seconds = current_time // 1000  # current_time//1000: convert ms to second
    m, s = divmod(seconds, 60)
    remaining_time_label.config(text="{:02d}:{:02d}".format(m, s))
    total_time_label.config(text="{}".format(total), fg="purple")
    slider.config(to=length, value=seconds)
    after_id = remaining_time_label.after(1000, song_duration)  # every 1s call 'song_duration' func


def song_slider(value): print(value)

# ------------------- Widgets ------------------
# song listbox
song_box = Listbox(root, bg="black", fg="white", selectbackground="white", selectforeground="black", width=60,
                   font=("arial", 15))
song_box.pack(pady=20)
# button images
back_img = ImageTk.PhotoImage(Image.open("MusicPlayerTkinter/img/back.png").resize((64, 64)))
forward_img = ImageTk.PhotoImage(Image.open("MusicPlayerTkinter/img/forward.png").resize((64, 64)))
play_img = ImageTk.PhotoImage(Image.open("MusicPlayerTkinter/img/play.png").resize((64, 64)))
stop_img = ImageTk.PhotoImage(Image.open("MusicPlayerTkinter/img/stop.png").resize((64, 64)))
pause_img = ImageTk.PhotoImage(Image.open("MusicPlayerTkinter/img/pause.png").resize((64, 64)))
# Player Frame
player_frame = Frame(root)
player_frame.pack()
# add button (back-forward-play-pause-stop)
back_btn = Button(player_frame, image=back_img, command=previous_song)
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
add_song_menu.add_command(label="Quit", command=root.quit)
# music slider
slider = ttk.Scale(root, from_=0, to=100, orient=HORIZONTAL, value=0, command=song_slider)
slider.pack(pady=10, padx=10, fill=X)
# remaining time
remaining_time_label = Label(root, text="", relief=FLAT)
remaining_time_label.pack(fill=X, side=LEFT, ipady=2, padx=10)
# total time
total_time_label = Label(root, text="", relief=FLAT)
total_time_label.pack(fill=X, side=RIGHT, ipady=2, padx=(10, 0))
# ----------------------------------------------
root.mainloop()
