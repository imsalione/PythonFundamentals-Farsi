import tkinter
import customtkinter
import pytube

def download():
    try:
        link = ulr_var.get()
        yt = pytube.YouTube(link)
        stream = yt.streams.get_highest_resolution()
        stream.download()
        title.configure(text="Downloaded Successfully")
    except:
        title.configure(text="Download Failed")

# System Setting
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

# Our app frame
app = customtkinter.CTk()
app.geometry("720*480")
app.title("YouTube Downloader")

# Adding UI Elements
title = customtkinter.CTkLabel(app, text="Insert YouTube Link")
title.pack(pady=12, padx=10)

# Link Input
ulr_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app,width=350, height=40, placeholder_text="Enter YouTube Link")
link.pack(pady=12, padx=10)

# Download Button
download_button = customtkinter.CTkButton(app, text="Download", command=lambda: download())
download_button.pack(pady=8, padx=5)

# Run app
app.mainloop()