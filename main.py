from tkinter import *
from tkinter import messagebox
import os
import socket

username = os.getenv("USERNAME") 
hostname = socket.gethostname()

print("Current username: {}".format(username)) 
print("Current hostname: {}".format(hostname))

root = Tk()
root.geometry("250x250")

#mainloop
root.title("Main Window")
root.mainloop()

print("Done !")