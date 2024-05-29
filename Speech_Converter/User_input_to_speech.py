from gtts import gTTS
import os
import tkinter as tk
from tkinter import messagebox

class TextToSpeechConverter:
    def __init__(self, root):
        self.root = root
        self.root.title("Text to Speech Converter")
        self.root.geometry("400x300")

        # Load and display the background image
        self.background_image = tk.PhotoImage(file='C:/Users/birst/OneDrive/Pictures/Camera Roll/textToSpeech.png')
        self.background_label = tk.Label(root, image=self.background_image)
        self.background_label.place(relwidth=1, relheight=1)

        # Create the entry and button widgets
        self.entry = tk.Entry(root, width=40)
        self.entry.place(relx=0.5, rely=0.6, anchor=tk.CENTER)

        self.button = tk.Button(root, text='Start', command=self.text_to_speech)
        self.button.place(relx=0.5, rely=0.7, anchor=tk.CENTER)

    def text_to_speech(self):
        text = self.entry.get()
        if not text:
            messagebox.showerror("Error", "Please enter some text.")
            return

        try:
            language = 'en'
            output = gTTS(text=text, lang=language, slow=False)
            output_file = 'text_to_speech.mp3'
            output.save(output_file)
            os.system(f'start {output_file}')
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

def main():
    root = tk.Tk()
    app = TextToSpeechConverter(root)
    root.mainloop()

if __name__ == "__main__":
    main()
