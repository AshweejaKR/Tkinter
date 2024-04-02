from tkinter import *
from tkinter import messagebox
import os
import socket
from PIL import Image, ImageTk

import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

username = os.getenv("USERNAME") 
hostname = socket.gethostname()

print("Current username: {}".format(username)) 
print("Current hostname: {}".format(hostname))

contactlist = []
Name = None

user = None
image_extension = None
image_path = None

def add_photo():
    print("adding photo ...")

def process_data():
    print("processing data ...")

def InitScreen(root):
    screen_width, screen_height = root.winfo_screenwidth(), root.winfo_screenheight()
    root.x_co = int((screen_width / 2) - (550 / 2))
    root.y_co = int((screen_height / 2) - (400 / 2)) - 80
    root.geometry(f"550x400+{root.x_co}+{root.y_co}")

    first_frame = Frame(root, bg = "sky blue")
    first_frame.pack(fill = "both", expand = True)

    app_icon = Image.open('images/chat_ca.png')
    app_icon = ImageTk.PhotoImage(app_icon)

    root.iconphoto(False, app_icon)

    background = Image.open("images/login_bg_ca.jpg")
    background = background.resize((550, 400), Image.ANTIALIAS)
    background = ImageTk.PhotoImage(background)

    upload_image = Image.open('images/upload_ca.png')
    upload_image = upload_image.resize((25, 25), Image.ANTIALIAS)
    upload_image = ImageTk.PhotoImage(upload_image)

    user_image = 'images/user.png'

    Label(first_frame, image = background).place(x = 0, y = 0)

    head = Label(first_frame, text = "Sign Up", font = "lucida 17 bold", bg = "grey")
    head.place(relwidth = 1, y = 24)

    profile_label = Label(first_frame, bg = "grey")
    profile_label.place(x = 350, y = 75, width = 150, height = 140)

    upload_button = Button(first_frame, image = upload_image, compound = "left", text = "Upload Image", cursor = "hand2", font = "lucida 12 bold", padx = 2, command = add_photo)
    upload_button.place(x = 345, y = 220)

    username = Label(first_frame, text = "Username", font = "lucida 12 bold", bg = "grey")
    username.place(x = 50, y = 75)
    username_entry = Entry(first_frame,  font = "lucida 12 bold", width = 10, highlightcolor = "blue", highlightthickness = 1)
    username_entry.place(x = 195, y = 75)
    username_entry.focus_set()

    host_address = Label(first_frame, text = "host address", font = "lucida 12 bold", bg = "grey")
    host_address.place(x = 50, y = 115)
    host_address_entry = Entry(first_frame,  font = "lucida 12 bold", width = 10, highlightcolor = "blue", highlightthickness = 1)
    host_address_entry.place(x = 195, y = 115)
    host_address_entry.focus_set()

    port_number = Label(first_frame, text = "port number", font = "lucida 12 bold", bg = "grey")
    port_number.place(x = 50, y = 155)
    username_entry = Entry(first_frame,  font = "lucida 12 bold", width = 10, highlightcolor = "blue", highlightthickness = 1)
    username_entry.place(x = 195, y = 155)
    username_entry.focus_set()

    submit_button = Button(first_frame, text = "Connect", font = "lucida 12 bold", padx = 30, cursor = "hand2", command = process_data, bg = "#16cade", relief = "solid", bd = 2)
    submit_button.place(x = 200, y = 275)

    #mainloop
    root.mainloop()

root = Tk()
root.config(bg = '#d3f3f5')
InitScreen(root)

print("Done !")
