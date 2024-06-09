'''
79. How do various operations and manipulations can be done on images in tkinter.
Explain the method used by giving piece of code.

'''

import tkinter as tk
from PIL import Image, ImageTk

def manipulate_image():
    original_image = Image.open("goku.jpg")
    resized_image = original_image.resize((300, 300))
    rotated_image = resized_image.rotate(180)
    tk_image = ImageTk.PhotoImage(rotated_image)
    label.config(image=tk_image)
    label.image = tk_image

root = tk.Tk()
root.title("Image Manipulation")

initial_image = Image.open("goku.jpg")
initial_image.thumbnail((300, 300))
initial_tk_image = ImageTk.PhotoImage(initial_image)

label = tk.Label(root, image=initial_tk_image)
label.pack()

manipulate_button = tk.Button(root, text="Manipulate Image", command=manipulate_image)
manipulate_button.pack()

root.mainloop()
