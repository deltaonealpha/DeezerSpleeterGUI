import os
try:
    import tkinter
except:
    os.system("pip install pytk --user")
    
try:
    import spleeter
except:
    os.system("pip install spleeter --user")
    
try:
    import PySimpleGUI
except:
    os.system("pip install pysimplegui --user")
    
try:
    import tensorflow
except:
    os.system("pip install tensorflow --user")
    
try:
    import fleep
except:
    os.system("pip install fleep --user")


import PySimpleGUI as sg
import  tkinter as tk
from tkinter import filedialog
from tkinter import * 
from tkinter import messagebox
import time, shutil, fleep, sys, subprocess, pkg_resources

from datetime import datetime

required = {'pysimplegui', 'spleeter', 'pytk', 'tensorflow', 'fleep'}


layout = [[sg.Text("Welcome to SpleeterGUI.\nSpleeter can separate voice and accompaniments from audio tracks.\nSelect an option to proceed:", key='text')], 
          [sg.Text("Vocals/ accompaniment separation")], 
          [sg.Button("Start (2)")], 
          
          [sg.Text("\nVocals/ drums/ bass/ other separation")], 
          [sg.Button("Start (4)")], 
          
          [sg.Text("\nVocals/ drums/ bass/ piano/ other separation")], 
          [sg.Button("Start (5)")], 
          
          [sg.Text("")], 
          [sg.Button("About"), sg.Button("Exit")]]

# Create the window
window = sg.Window("SpleeterGUI", layout) #, margins=(10, 50)

print('''                                                                ████████   ██    ██  ██
███████  ██████  ██     █████  █████  ████████  █████  ██████   ██         ██    ██  ██
██       █   ██  ██     ██     ██        ██     ██     ██  ██   ██         ██    ██  ██
 █████   ██████  ██     ████   ████      ██     ████   ██████   ██         ██    ██  ██
     ██  ██      ██     ██     ██        ██     ██     ██  █    ██ ██████  ██    ██  ██
███████  ██      █████  █████  █████     ██     █████  ██   █   ██     ██  ██    ██  ██
                   						█████████  ████████  ██
                         
Close this terminal window if you want to force-terminate the program. 
Please note, while processing your files the application may say 'not responding' 
but worry not your files are actually being processed.''')

# Create an event loop
while True:
    event, values = window.read()
    # End program if user closes window or
    # presses the OK button
    
    if event == "Start (2)":
        #print("openfiledialog")
        now = datetime.now() # current date and time
        date_time = now.strftime("%m%d%Y")
        if not os.path.exists("output" + date_time):
            time.sleep(1)
            os.makedirs("output" + date_time)
        root = tk.Tk()
        root.withdraw()
        file_path = filedialog.askopenfilename()
        # Using embedded configuration.
        if file_path:
            with open(file_path, "rb") as file:
                info = fleep.get(file.read(128))
            if info.type[0] == "audio":
                nfpath = file_path.replace(" ", "_")
                os.rename(file_path, nfpath)
                file_path = nfpath
                stream = os.popen('spleeter separate -p spleeter:2stems -o output' + date_time + " " + file_path)
                output = stream.read()
                print(output)
                os.startfile("output" + date_time)
            else:
                print("")
                messagebox.showwarning("showwarning", "SpleeterGUI can only process audio files(!)")
            
    if event == "Start (4)":
        #print("openfiledialog")
        now = datetime.now() # current date and time
        date_time = now.strftime("%m%d%Y")
        if not os.path.exists("output" + date_time):
            time.sleep(1)
            os.makedirs("output" + date_time)
        root = tk.Tk()
        root.withdraw()
        file_path = filedialog.askopenfilename()
        # Using embedded configuration.
        if file_path:
            with open(file_path, "rb") as file:
                info = fleep.get(file.read(128))
            if info.type[0] == "audio":
                nfpath = file_path.replace(" ", "_")
                os.rename(file_path, nfpath)
                file_path = nfpath
                stream = os.popen('spleeter separate -p spleeter:4stems -o output' + date_time + " " + file_path)
                output = stream.read()
                print(output)
                os.startfile("output" + date_time)
            else:
                print("")
                messagebox.showwarning("showwarning", "SpleeterGUI can only process audio files(!)")
            
        
    if event == "Start (5)":
        #print("openfiledialog")
        now = datetime.now() # current date and time
        date_time = now.strftime("%m%d%Y")
        if not os.path.exists("output" + date_time):
            time.sleep(1)
            os.makedirs("output" + date_time)
        root = tk.Tk()
        root.withdraw()
        file_path = filedialog.askopenfilename()
        # Using embedded configuration.
        if file_path:
            with open(file_path, "rb") as file:
                info = fleep.get(file.read(128))
            if info.type[0] == "audio":
                nfpath = file_path.replace(" ", "_")
                os.rename(file_path, nfpath)
                file_path = nfpath
                stream = os.popen('spleeter separate -p spleeter:5stems -o output' + date_time + " " + file_path)
                output = stream.read()
                print(output)
                os.startfile("output" + date_time)
            else:
                print("")
                messagebox.showwarning("showwarning", "SpleeterGUI can only process audio files(!)")
            
    
    if event == "Exit" or event == sg.WIN_CLOSED:
        break
    
    if event == "About":
        layout = [[sg.Text('''Spleeter is Deezer source separation library with pretrained models written in Python and uses Tensorflow. 
It makes it easy to train source separation model (assuming you have a dataset of isolated sources),
and provides already trained state of the art model for performing various flavour of separation.

SpleeterGUI is a GUI-implementation of Spleeter in Python by @deltaonealpha.

github.com/deltaonealpha''', key="new")], [sg.Button("Close")]]
        window = sg.Window("About SpleeterGUI", layout, modal=True)
        choice = None
        while True:
            event, values = window.read()
            if event == "Close" or event == sg.WIN_CLOSED:
                break
        

window.close()

