from tkinter import *
from tkinter import filedialog
from pytube import YouTube
import shutil
import os


root = Tk()
root.title("YouTube Downloader")


def download_highest_res():

    get_url = url_enter.get() # Gets the YT URL
    user_path = path_label.cget("text") # Gets the path the user chose
    root.title("Downloading...")
    mp4_highest = YouTube(get_url).streams.get_highest_resolution().download()# Download highest resolution vid
    shutil.move(mp4_highest, user_path)
    root.title("Download complete!")

def download_mpthree():
    get_url = url_enter.get() # Gets the YT URL
    user_path = path_label.cget("text") # Gets the path the user chose
    root.title("Downloading...")
    mpthree = YouTube(get_url).streams.filter(only_audio=True).first().download()  # Download highest audio sample
    base, ext = os.path.splitext(mpthree)
    new_file = base + ".mp3"
    os.rename(mpthree, new_file)
    shutil.move(new_file, user_path)
    root.title("Download complete!")

def show():
    final = ""
    confirm_label = Label(root, text=clicked.get())
    final = clicked.get()
    custom_download(final)

def custom_download(resolution):
    get_url = url_enter.get()  # Gets the YT URL
    user_path = path_label.cget("text")  # Gets the path the user chose
    root.title("Downloading...")
    mp4_custom = YouTube(get_url).streams.filter(res=resolution).first().download()
    shutil.move(mp4_custom, user_path)
    root.title("Download complete!")


# Dropdown menu
clicked = StringVar()
clicked.set("choose")
drop = OptionMenu(root, clicked, "360p", "480p", "720p", "1080p")

#button to the right of the dropdown list
custom_final_download = Button(root, text="Confirm", bg='grey', padx=20, pady=20, command=show)



def path_selection():
    path = filedialog.askdirectory() # allows user to select a path from the file explorer
    path_label.config(text=path)

# defining stuff
enter_youtube_label = Label(root, text="Enter a YouTube URL:", font=('Arial',30))
url_enter = Entry(root, width=80)
path_label = Label(root, text="Select path for the download:\n", font=('Arial',20))
path_button = Button(root, text="Path", bg='grey', padx=30, pady=20, command=path_selection)
download_explanation = Label(root, text="CHOOSING A PATH IS MANDATORY\nRed Button: Highest Resolution, Green Button: Mp3", font=('Arial',13))
custom_label_below = Label(root, text="Custom Resolution? Choose Below:\n", font=('Arial',20))
extra_bottom_space = Label(root, text="\n")
extra_bottom_space2 = Label(root, text="\n")
drop.configure(bg="grey")
#options defined buttons
download_button_highest = Button(root, text="Highest", bg='red', padx=30, pady=20, command=download_highest_res)
download_audio = Button(root, text="Audio", bg='Green', padx=30, pady=20, command=download_mpthree)





# Placing onto the screen
enter_youtube_label.grid(row=1, column=1, columnspan=3)
url_enter.grid(row=2, column=1, columnspan=3)
path_label.grid(row=3, column=1, columnspan=3)
download_button_highest.grid(row=4, column=1)
path_button.grid(row=4, column=2)
download_audio.grid(row=4, column=3)
extra_bottom_space.grid(row=5, column=1, columnspan=3)
download_explanation.grid(row=6, column=1, columnspan=3)
custom_label_below.grid(row=7, column=1, columnspan=3)
drop.grid(row=8, column=1, columnspan=2)
custom_final_download.grid(row=8, column=2, columnspan=3)
extra_bottom_space2.grid(row=9)







root.mainloop()