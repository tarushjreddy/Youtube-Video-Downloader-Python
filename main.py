from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from pytube import YouTube


mainone = Tk()
mainone.title = "Tarush Video Youtube Downloader"
mainone.geometry("700x500")
mainone.columnconfigure(0, weight=1)

ytdlableone = Label(
    mainone, text="Enter the link of the video donwloaded", font=("poppins", 12))
ytdlableone.grid()

ytentryvar = StringVar()
ytentry = Entry(mainone, width=50, textvariable=ytentryvar)
ytentry.grid()


ytderror = Label(
    mainone, text="Error Message", font=("poppins", 10), fg="red")
ytderror.grid()


ytdsave = Label(
    mainone, text="Save Video or Download the Video", font=("poppins", 12),)
ytdsave.grid()

savebtn = Button(mainone, width=10, text="Choose Path", bg='red')
savebtn.grid()

mainone.mainloop()
