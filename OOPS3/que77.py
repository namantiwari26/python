import tkinter as tk
from tkinter import colorchooser
from tkcalendar import DateEntry

def choose_color():
    color = colorchooser.askcolor(title="Colors")
    print("Selected Color:", color)

def choose_date():
    date_entry = tk.DateEntry(root)
    date_entry.pack()

root = tk.Tk()

color_button = tk.Button(root, text="Choose Color", command=choose_color)
color_button.pack()

date_button = tk.Button(root, text="Choose Date", command=choose_date)
date_button.pack()

root.mainloop()
