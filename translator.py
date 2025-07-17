import tkinter as tk
from tkinter import ttk
from googletrans import Translator

# some languages
LANGUAGES = {
    'Arabic': 'ar',
    'Bengali': 'bn',
    'Chinese (Simplified)': 'zh-cn',
    'Dutch': 'nl',
    'English': 'en',
    'French': 'fr',
    'German': 'de',
    'Gujarati': 'gu',
    'Hindi': 'hi',
    'Italian': 'it',
    'Japanese': 'ja',
    'Kannada': 'kn',
    'Korean': 'ko',
    'Marathi': 'mr',
    'Portuguese': 'pt',
    'Punjabi': 'pa',
    'Russian': 'ru',
    'Spanish': 'es',
    'Tamil': 'ta',
    'Telugu': 'te',
    'Urdu': 'ur'
}

def translate_text():
    dest_lang_name = lang_combo.get()
    text = src_text.get("1.0", tk.END).strip()

    if not text:
        result_label.config(text="Enter text to translate.")
        return

    dest_lang_code = LANGUAGES.get(dest_lang_name)
    translator = Translator()

    try:
        translation = translator.translate(text, src='en', dest=dest_lang_code)
        result_label.config(text=translation.text)
    except Exception as e:
        result_label.config(text=f"Error: {e}")

# main GUI setup
root = tk.Tk()
root.title("English Text Translator")
root.geometry("500x450")
root.resizable(False, False)

tk.Label(root, text="Enter Text in English", font=('Arial', 12)).pack(pady=(10, 0))
src_text = tk.Text(root, height=5, width=60)
src_text.pack(pady=5)

tk.Label(root, text="Select Destination Language", font=('Arial', 12)).pack(pady=(10, 0))
lang_combo = ttk.Combobox(root, values=list(LANGUAGES.keys()), state="readonly", width=30)
lang_combo.set("Spanish")  # default
lang_combo.pack(pady=5)

tk.Button(root, text="Translate", command=translate_text, font=('Arial', 12)).pack(pady=15)

result_label = tk.Label(root, text="", wraplength=450, justify="left", font=('Arial', 11), fg="blue")
result_label.pack(pady=(5, 10))

root.mainloop()
