import tkinter as tk
from tkinter import scrolledtext
import pyttsx3

def speak_text():
    text = text_area.get('1.0', tk.END).strip()
    if text:
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()

def clear_text():
    text_area.delete('1.0', tk.END)

app = tk.Tk()
app.title("Text-to-Speech GUI")
app.geometry("500x400")

label = tk.Label(app, text="Enter text to speak:", font=("Arial", 14))
label.pack(pady=10)

text_area = scrolledtext.ScrolledText(app, wrap=tk.WORD, width=60, height=10, font=("Arial", 12))
text_area.pack(padx=10, pady=10)

btn_frame = tk.Frame(app)
btn_frame.pack(pady=10)

speak_btn = tk.Button(btn_frame, text="🎤 Speak", font=("Arial", 12), command=speak_text)
speak_btn.pack(side=tk.LEFT, padx=10)

clear_btn = tk.Button(btn_frame, text="🗑️ Clear", font=("Arial", 12), command=clear_text)
clear_btn.pack(side=tk.LEFT, padx=10)

app.mainloop()
