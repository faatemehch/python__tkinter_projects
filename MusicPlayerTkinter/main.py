# import needed packages
from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
from mutagen.mp3 import MP3
import tkinter.ttk as ttk
import pygame
import time
import os

root = Tk()
root.geometry("450x400")
root.title("MUSIC PLAYER")
root.resizable(False, False)
color = "skyblue"
root.config(bg=color)

pygame.mixer.init()  # initialize pygame mixer
# ------------------ Variables -----------------
# global paused
paused = False
isPlaying = False
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


def song_duration():
    global after_id, length, total
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
    total_time_label.config(text="{}".format(total), fg="blue")
    duration_slider.config(to=length)
    if seconds - 1 == duration_slider.get():
        m, s = divmod(seconds, 60)
        duration_slider.config(value=seconds)
        remaining_time_label.config(text="{:02d}:{:02d}".format(m, s), fg="blue")
    else:
        seconds = int(duration_slider.get())
        m, s = divmod(seconds, 60)
        duration_slider.config(value=seconds + 1)
        remaining_time_label.config(text="{:02d}:{:02d}".format(m, s), fg="blue")
    if int(duration_slider.get()) == int(length):
        stop_song(e=None)
    else:
        after_id = remaining_time_label.after(1000, lambda: song_duration())  # every 1s call 'song_duration' func
    volume_slider.config(value=1 - pygame.mixer.music.get_volume())


def reset_widgets():
    global paused, isPlaying
    paused = False
    isPlaying = False
    duration_slider.config(value=0)
    remaining_time_label.config(text="")
    total_time_label.config(text="")
    remaining_time_label.after_cancel(after_id)


def play_song(e):
    global isPlaying
    if isPlaying:
        pause_song()
    else:
        song_name = song_box.get(ACTIVE)
        pygame.mixer.music.load(songs_path[song_name])
        pygame.mixer.music.play(loops=0)
        print("played")
        song_duration()
        duration_slider.config(value=0)
        isPlaying = True


def stop_song(e):
    reset_widgets()  # reset things
    pygame.mixer.music.stop()  # stop the music
    song_box.selection_clear(ACTIVE)  # clear stopped item
    print("stopped")


def pause_song():
    global paused
    if paused:
        pygame.mixer.music.unpause()
        paused = False
        remaining_time_label.after(1000, song_duration)
        print("un-paused")
    else:
        pygame.mixer.music.pause()
        paused = True
        remaining_time_label.after_cancel(after_id)
        print("paused")


def previous_song(e):
    reset_widgets()
    current_song = song_box.curselection()[0]  # the index of currently selected item
    # previous_song_name = song_box.get(current_song - 1)
    # previous_song_path = songs_path[f"{previous_song_name}"]
    song_box.selection_clear(current_song)
    song_box.activate(current_song - 1)  # activate previous item
    song_box.selection_set(current_song - 1)
    play_song(e)


def next_song(e):
    reset_widgets()
    current_song = song_box.curselection()[0]  # the index of currently selected item
    # next_song_name = song_box.get(current_song + 1)
    # next_song_path = songs_path[f"{next_song_name}"]
    song_box.selection_clear(current_song)
    song_box.activate(current_song + 1)  # activate next item
    song_box.selection_set(current_song + 1)
    play_song(e)


def song_slider(value):
    song_name = song_box.get(ACTIVE)
    pygame.mixer.music.load(songs_path[song_name])
    pygame.mixer.music.play(loops=0, start=float(value))


def change_volume(value):
    pygame.mixer.music.set_volume(1 - float(value))
    # current_volume = pygame.mixer.music.get_volume()


# ---------------- Hover Functions -------------
# ------------------- Widgets ------------------
# main frame
main_frame = Frame(root, bg=color)
main_frame.pack(pady=20)
# song listbox
song_box = Listbox(main_frame, bg="black", fg="white", selectbackground="white", selectforeground="black", width=40,
                   font=("arial", 15))
song_box.pack(side=LEFT, padx=(0, 10))
# Volume Slider
volume_slider = ttk.Scale(main_frame, orient=VERTICAL, value=1, from_=0, to=1, command=change_volume)
volume_slider.pack(side=RIGHT, padx=(10, 0), fill=Y)
# Player Frame
player_frame = Frame(root, bg=color)
player_frame.pack(pady=20, padx=(10, 80))
# add button (back-forward-play-pause-stop)
back_btn = Button(player_frame, text=u"\u23EE", font=("arial", 55), width=2, height=1, borderwidth=0, border=0, anchor=S)
forward_btn = Button(player_frame, text=u"\u23ED", font=("arial", 55), width=2, height=1, borderwidth=0, border=0, anchor=S)
play_btn = Button(player_frame, text="\u23EF", font=("arial", 55), width=2, height=1, borderwidth=0, border=0, anchor=S)
stop_btn = Button(player_frame, text=u"\u23F9", font=("arial", 55), width=2, height=1, borderwidth=0, border=0, anchor=S)
# grid btn
back_btn.grid(row=0, column=0, padx=0, ipady=2, ipadx=0)
forward_btn.grid(row=0, column=3, padx=0, ipady=2, ipadx=0)
play_btn.grid(row=0, column=2, padx=0, ipady=2, ipadx=0)
stop_btn.grid(row=0, column=1, padx=0, ipady=2, ipadx=0)
# bind labels to work as button
back_btn.bind("<Button-1>", previous_song)
forward_btn.bind("<Button-1>", next_song)
play_btn.bind("<Button-1>", play_song)
stop_btn.bind("<Button-1>", stop_song)
#  Create Menu
menu = Menu(root)
root.config(menu=menu)
add_song_menu = Menu(menu)
menu.add_cascade(label="File", menu=add_song_menu)
add_song_menu.add_command(label="Add New Song", command=add_song)
add_song_menu.add_command(label="Quit", command=root.quit)
# music position slider --> Show Duration
duration_slider = ttk.Scale(root, from_=0, orient=HORIZONTAL, value=0, command=song_slider)
duration_slider.pack(pady=10, fill=X, padx=20)
# pass song time
remaining_time_label = Label(root, text="", bg=color, relief=FLAT, font=("arial", 15, "bold"))
remaining_time_label.pack(side=LEFT, ipady=2, padx=15)
# total song time
total_time_label = Label(root, text="", bg=color, relief=FLAT, font=("arial", 15, "bold"))
total_time_label.pack(side=RIGHT, ipady=2, padx=(10, 15))

# ----------------------------------------------
root.mainloop()
