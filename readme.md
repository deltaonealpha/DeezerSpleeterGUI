 q	![icon](C:\Users\balaj\Desktop\icon.jpg)

# **Deezer Spleeter GUI**

#### A GUI implementation of Spleeter-CLI written in Python

------

[TOC]

------



#### **#Introduction**

SpleeterGUI is a GUI implementation of Spleeter by Deezer in PythonQT5 and Tkinter. It makes use of file analysis and classifiers to handle all compatible file types. It also whitespaces in file names which is typically an issue that SpleeterCLI can't deal with. 

------



#### **#Options**

- 2 step - vocals + accompaniment
- 4 step - vocals + bass + others + accompaniment
- 5 step - vocals + bass + others + piano + accompaniment

------



#### **#Usage**

SpleeterGUI runs a terminal window with log and note messages and a GUI window on-top of it. The window opened provides three processing options and two navigational buttons, one for exiting the app and one for viewing the about section of the same.

On opening any processing option SpleeterGUI opens a file dialog to select a file. Then the app directly proceeds to processing the selected file post validation of it's type (i.e., audio). Afterwards the destination folder (output/filename/) is opened with files depending on your process type (2/4/5).

------



#### **#To-Do**

- [ ] Direct download and processing from YTDL
- [ ] Direct URL-based download
- [ ] Progress bar

------



#### **#Credits**

All credits go to Deezer (github.com/deezer/spleeter). This project only builds a GUI interface on-top of it.

------

<img src="C:\Users\balaj\Desktop\Untitled-1.png" alt="Untitled-1" style="zoom:25%;" />