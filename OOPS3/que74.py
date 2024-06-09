"""
74. How Create_line method can be used to draw different types of lines, rectangle,
square and triangle?
"""
import tkinter as tk

# Create a window
window = tk.Tk()
window.title("Draw Shapes with create_line")

# Create a canvas widget
canvas = tk.Canvas(window, width=600, height=600)
canvas.pack()

# Draw a straight line
canvas.create_line(10, 10, 200, 10)  # x1, y1, x2, y2

# Draw a dashed line
canvas.create_line(10, 30, 200, 30, dash=(6, 9))

# Draw a rectangle using lines
canvas.create_line(10, 50, 200, 50)  # Top edge
canvas.create_line(200, 50, 200, 150)  # Right edge
canvas.create_line(200, 150, 10, 150)  # Bottom edge
canvas.create_line(10, 150, 10, 50)  # Left edge

# Draw a square using lines
side_length = 100
canvas.create_line(10, 200, 10 + side_length, 200)  # Top edge
canvas.create_line(10 + side_length, 200, 10 + side_length, 200 + side_length)  # Right edge
canvas.create_line(10 + side_length, 200 + side_length, 10, 200 + side_length)  # Bottom edge
canvas.create_line(10, 200 + side_length, 10, 200)  # Left edge

# Draw a triangle using lines
canvas.create_line(220, 50, 300, 150)  # First side
canvas.create_line(300, 150, 200, 150)  # Second side
canvas.create_line(200, 150, 220, 50)  # Third side

# Run the Tkinter event loop
window.mainloop()
