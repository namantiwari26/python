"""
76. Explain pack(), grid() and place() with their options with the help of suitable code.

"""
#ANSWER
"""
1. pack() Method:
The pack() method organizes widgets in a block format.
 Widgets are packed vertically or horizontally based on the order they are packed and the side option.
"""
import tkinter as tk

root = tk.Tk()

# Widgets
label1 = tk.Label(root, text="Label 1")
label2 = tk.Label(root, text="Label 2")

# Packing widgets
label1.pack(side="top", fill="both", expand=True)
label2.pack(side="left", fill="y", anchor="w")

root.mainloop()

"""
2.grid() Method:
the grid() method arranges widgets in a grid like stucture.widgets are placed in rows and columns

"""

import tkinter as tk

root=tk.Tk()

label1=tk.Label(root,text="Label 1")
label2=tk.Label(root,text="Label 2")

label1.grid(row=0,column=0,padx=5,pady=5)
label2.grid(row=1,column=0,sticky="w",ipadx=10)

root.mainloop()

"""
3.place() method allows you to specify the exact position of a widget using x and y coordinates

"""
import tkinter as tk

root=tk.Tk()

label1=tk.Label(root,text="Label 1")
label2=tk.Label(root,text="Label 2")

label1.place(x=50,y=20)
label2.place(relx=0.5,rely=0.5,anchor="w")

root.mainloop()