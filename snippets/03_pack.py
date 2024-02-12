# ================= side ===================

import tkinter as tk
from tkinter import ttk

# Window
root = tk.Tk()
root.title('Pack')
root.geometry('400x600')

# Widgets
label1 = ttk.Label(text='Label 1',background='red')
label2 = ttk.Label(text='Label 2',background='blue')
label3 = ttk.Label(text='Label 3',background='green')
button = ttk.Button(text='Button')

# layout
label1.pack(side='left')
label2.pack(side='left')
label3.pack(side='left')
button.pack(side='left')

root.mainloop()