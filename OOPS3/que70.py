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

'''
4. Entry
Use: A single-line text entry field.
Syntax: entry = Entry(parent, options)
Options: bg, fg, font, show, etc.
Methods: pack(), grid(), place(), get(), insert(), delete()
'''

entry = tk.Entry(window, bg="white", fg="black", font=("Arial", 14))
entry.pack()

'''
5. Text
Use: A multi-line text entry field.
Syntax: text = Text(parent, options)
Options: bg, fg, font, height, width, etc.
Methods: pack(), grid(), place(), get(), insert(), delete()
'''

text = tk.Text(window, height=5, width=30, bg="white", fg="black", font=("Arial", 14))
text.pack()

'''
6. Radiobutton
Use: A button representing one choice in a set of mutually exclusive options.
Syntax: radiobutton = Radiobutton(parent, options)
Options: text, variable, value, command, etc.
Methods: pack(), grid(), place()
'''

option = tk.IntVar()
radio1 = tk.Radiobutton(window, text="Option 1", variable=option, value=1)
radio2 = tk.Radiobutton(window, text="Option 2", variable=option, value=2)
radio1.pack()
radio2.pack()

'''
7. Checkbutton
Use: A button that can be either checked or unchecked.
Syntax: checkbutton = Checkbutton(parent, options)
Options: text, variable, onvalue, offvalue, command, etc.
Methods: pack(), grid(), place()
'''

check_var = tk.IntVar()
checkbutton = tk.Checkbutton(window, text="Check Me", variable=check_var)
checkbutton.pack()
'''
8. Listbox
Use: Displays a list of items from which a user can select one or more.
Syntax: listbox = Listbox(parent, options)
Options: height, width, bg, fg, font, selectmode, etc.
Methods: pack(), grid(), place(), insert(), delete(), get()
'''

listbox = tk.Listbox(window, height=5, width=30)
listbox.insert(1, "Item 1")
listbox.insert(2, "Item 2")
listbox.pack()

'''
9. Combobox (from ttk module)
Use: A drop-down list for selecting one option from a list.
Syntax: combobox = ttk.Combobox(parent, options)
Options: values, state, width, height, etc.
Methods: pack(), grid(), place(), get(), set()
'''

from tkinter import ttk

combobox = ttk.Combobox(window, values=["Option 1", "Option 2", "Option 3"])
combobox.pack()

'''
10. Spinbox
Use: An entry widget with increment and decrement arrows.
Syntax: spinbox = Spinbox(parent, options)
Options: from_, to, increment, bg, fg, font, etc.
Methods: pack(), grid(), place(), get(), set()
'''
spinbox = tk.Spinbox(window, from_=0, to=10)
spinbox.pack()

'''
11. OptionMenu
Use: A menu button to select from a list of options.
Syntax: optionmenu = OptionMenu(parent, variable, value, *values)
Options: bg, fg, font, etc.
Methods: pack(), grid(), place()
'''


option_var = tk.StringVar(window)
option_var.set("Option 1")
optionmenu = tk.OptionMenu(window, option_var, "Option 1", "Option 2", "Option 3")
optionmenu.pack()

'''
12. Scale
Use: A slider to select a numerical value.
Syntax: scale = Scale(parent, options)
Options: from_, to, orient, length, tickinterval, etc.
Methods: pack(), grid(), place(), get()
'''
from tkinter import HORIZONTAL

scale = tk.Scale(window, from_=0, to=100, orient=HORIZONTAL)
scale.pack()
'''
13. Canvas
Use: A widget for drawing shapes, lines, and images.
Syntax: canvas = Canvas(parent, options)
Options: bg, height, width, etc.
Methods: pack(), grid(), place(), create_line(), create_oval(), create_rectangle(), etc.
'''


canvas = tk.Canvas(window, bg="white", height=200, width=200)
canvas.create_line(0, 0, 200, 100, fill="blue")
canvas.pack()

'''
14. Checkbox
Use: A checkbox that can be toggled on or off.
syntax: checkbutton = Checkbutton(master, options)
options:text,variable,onvalue,offvalue
Methods:select(),deselect()
'''
var = tk.IntVar()
checkbutton = tk.Checkbutton(window, text="Check me", variable=var)
checkbutton.pack()
