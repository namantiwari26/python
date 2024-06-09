'''
70. What are widgets in Tkinter? Explain the following widget along with their uses,
syntax, options and methods: Frame, Label, Button, Entry, Text, Radiobutton,
Checkbox, listbox, Combobox, , Spinbox, OptionMenu, Scale, Canvas, Checkbutton.
Also write code for setting these widgets on the window.

'''
#ANSWER
import tkinter as tk

window=tk.Tk()

'''
1. Frame
Use: A container widget used to group other widgets.
Syntax: frame = Frame(parent, options)
Options: bd, bg, height, width, relief, etc.
Methods: pack(), grid(), place()
'''
frame = tk.Frame(window, bg="lightgrey", width=200, height=100)
frame.pack()

'''
2. Label
Use: Displays text or an image.
Syntax: label = Label(parent, options)
Options: text, bg, fg, font, image, etc.
Methods: pack(), grid(), place()
'''

label = tk.Label(window, text="Hello, Tkinter!", bg="yellow", fg="blue", font=("Arial", 16))
label.pack()

'''
3. Button
Use: A clickable button to trigger actions.
Syntax: button = Button(parent, options)
Options: text, command, bg, fg, font, etc.
Methods: pack(), grid(), place()
'''

def on_click():
    print("Button clicked!")

button = tk.Button(window, text="Click Me", command=on_click, bg="blue", fg="white")
button.pack()
