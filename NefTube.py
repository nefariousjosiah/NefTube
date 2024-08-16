import tkinter
import customtkinter
from pytubefix import YouTube

def startDownload():
    try:
        ytLink = link.get()
        ytObject = YouTube(ytLink)
        video = ytObject.streams.get_highest_resolution()
        video.download()
    except:
        title.configure(text="Something went please try again.")
        print("fuck up")
    else:
        title.configure(text="Completed!")
        print("download complete")
        



#settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

# frame
app = customtkinter.CTk()
app.geometry("720x480")
app.title("NefTube")
# app.iconbitmap("favicon.ico")



title = customtkinter.CTkLabel(app, text="Insert Link")
title.pack(padx= 10, pady = 10)

url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url_var)
link.pack()


download = customtkinter.CTkButton(app, text="Download", command= startDownload)
download.pack(padx= 10, pady= 10)

app.mainloop()

 """_   _ ____  _____                                                          
| | | / ___|| ____|                                                         
| | | \___ \|  _|                                                           
| |_| |___) | |___                                                          
 \___/|____/|_____| _ ____ _____  _    _     _     _____ ____    _____ ___  
|  _ \ \ / /_ _| \ | / ___|_   _|/ \  | |   | |   | ____|  _ \  |_   _/ _ \ 
| |_) \ V / | ||  \| \___ \ | | / _ \ | |   | |   |  _| | |_) |   | || | | |
|  __/ | |  | || |\  |___) || |/ ___ \| |___| |___| |___|  _ <    | || |_| |
|_|___ |_| |___|_|_\_|____/_|_/_/___\_\_____|_____|_____|_| \_\   |_| \___/ 
 / ___/ _ \| \ | \ \   / / ____|  _ \_   _|                                 
| |  | | | |  \| |\ \ / /|  _| | |_) || |                                   
| |__| |_| | |\  | \ V / | |___|  _ < | |                                   
 \____\___/|_| \_|  \_/  |_____|_| \_\|_|
"""
