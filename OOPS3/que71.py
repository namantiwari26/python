'''
71. How would you create a window in Tkinter and set its title and dimensions? Write
code for the same.

'''
#ANSWER

'''
To create a window in Tkinter and set its title and dimensions, 
you need to use the 'Tk' class to create the main window and 
then configure its title and size using the 'title' and 'geometry' methods.
 Here is an example code snippet that demonstrates how to do this:
'''

from tkinter import *

# Create the main window
window = Tk()

# Set the title of the window
window.title("My Tkinter Window")

# Set the dimensions of the window (width x height)
window.geometry("400x300")

# Run the application
window.mainloop()
