import os
import shutil
import threading
import tkinter as tk
from tkinter import *
from tkinter import filedialog, messagebox
from pytube import YouTube
from moviepy.editor import VideoFileClip
from tkinter.ttk import Button


class HoverButton(Button):
    def __init__(self, master=None, **kwargs):
        Button.__init__(self, master=master, **kwargs)
        self.default_bg = self["style"]
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)

    def on_enter(self, event=None):
        self.configure(style="Hover.TButton")

    def on_leave(self, event=None):
        self.configure(style=self.default_bg)

class VideoDownloaderApp:
    def __init__(self, master):
        self.master = master
        master.title("Video Downloader")
        master.configure(bg="lightgray")

        self.style = tk.ttk.Style()
        self.style.configure("Hover.TButton", background="sky blue")

        self.url_label = tk.Label(master, text="Enter video URL:", bg="lightgray")
        self.url_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.url_entry = tk.Entry(master, width=40)
        self.url_entry.grid(row=0, column=1, padx=10, pady=5)

        self.path_label = tk.Label(master, text="Select path to download:", bg="lightgray")
        self.path_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.path_var = tk.StringVar()
        self.path_var.set("Select path")
        self.path_display = tk.Label(master, textvariable=self.path_var, width=40, relief="sunken")
        self.path_display.grid(row=1, column=1, padx=10, pady=5)
        self.path_button = HoverButton(master, text="Select", command=self.get_path, style="Hover.TButton")
        self.path_button.grid(row=1, column=2, padx=5, pady=5)

        self.download_button = HoverButton(master, text="Download", command=self.start_download, style="Hover.TButton")
        self.download_button.grid(row=2, column=1, pady=20)

    def get_path(self):
        path = filedialog.askdirectory()
        self.path_var.set(path)

    def start_download(self):
        url = self.url_entry.get()
        path = self.path_var.get()

        if not url:
            messagebox.showerror("Error", "Please enter a valid URL.")
            return
        if path == "Select path":
            messagebox.showerror("Error", "Please select a download path.")
            return

        threading.Thread(target=self.download, args=(url, path)).start()

    def download(self, url, path):
        try:
            loading_label = tk.Label(self.master, text="Downloading...", font=("Arial", 12), bg="lightgray")
            loading_label.place(x=290, y=130, anchor="center")

            video = YouTube(url)
            video_path = path.cget('text')
            mp4 = video.streams.get_highest_resolution()
            
            video_clip = VideoFileClip(mp4)

            audio_clip = video_clip.audio
            audio_clip.write_audiofile(os.path.join(path, "audio.mp3"))
            audio_clip.close()
            shutil.move(video_path, path)

            loading_label.place_forget()
            messagebox.showinfo("Success", "Download complete.")
            self.url_entry.delete(0, tk.END)
            self.path_var.set("Select path")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

def main():
    root = tk.Tk()
    # Ensure the icon path is correct
    icon_path = "C:/python/Udemy-Course/Video_Downloader_App/assets/download.png"
    img = PhotoImage(file=icon_path)
    root.iconphoto(False, img)
    
    # Adjust size
    root.geometry('550x200')
    
    # set minimum window size value
    root.minsize(550, 200)
    
    # set maximum window size value
    root.maxsize(550, 200)
    app = VideoDownloaderApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
