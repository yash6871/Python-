import tkinter as tk
from tkinter import ttk

# Callback for button clicks
def on_button_click(char):
    current = entry_var.get()
    if char == 'C':
        entry_var.set('')
    elif char == '=':
        try:
            result = eval(current)
            entry_var.set(str(result))
        except Exception:
            entry_var.set('Error')
    else:
        entry_var.set(current + char)

# Main window setup
root = tk.Tk()
root.title("Calculator")

entry_var = tk.StringVar()
entry = ttk.Entry(root, textvariable=entry_var, font=('Arial', 24), justify='right')
entry.grid(row=0, column=0, columnspan=4, sticky='we', padx=5, pady=5)

# Button definitions
buttons = [
    ('7','8','9','/'),
    ('4','5','6','*'),
    ('1','2','3','-'),
    ('0','.','=','+'),
    ('C',)
]

# Create buttons dynamically
for r, row in enumerate(buttons, 1):
    for c, char in enumerate(row):
        btn = ttk.Button(root, text=char, command=lambda ch=char: on_button_click(ch))
        btn.grid(row=r, column=c, ipadx=10, ipady=10, padx=3, pady=3)

root.mainloop()
