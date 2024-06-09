'''
72. The following program creates a graphical user interface that allows the user to enter
a list of numbers and either find the smallest value or calculate the average. Assume
that the functions minList and avgList each take a string as a parameter and return
the appropriate value. For example, minList("2 5 1 4") returns 1, and avgList("2 5 1
4") returns 3.0.'''

#NOTICE-This code is from oops practice set question number 72 which is incorrect ,so just read answer ignore this code
'''
from tkinter import * #1
window = Tk() #2
frame = Frame(window) #3
frame.pack() #4
def compute(): #5
   input_str = entry.get() #6
   choice = option.get() #7
   if choice == 1: #8
    #result = minList(input_str) #9
   #else: #10
    #result = avgList(input_str) #11
   # result_label.config(text=str(result)) #12
    result_label.update() #13
entry = Entry(frame) #14
entry.pack() #15
result_label = Label(frame, text="") #16
result_label.pack() #17
option = IntVar() #18
radio_min = Radiobutton(frame, text="Min", variable=option, value=1,
command=compute) #19
radio_min.pack() #20
radio_avg = Radiobutton(frame, text="Avg", variable=option, value=2,
command=compute) #21
radio_avg.pack() #22
exit_button = Button(frame, text="Exit", command=window.destroy) #23
exit_button.pack() #24
window.mainloop() #25
'''
'''
Explain the purpose of each line or group of lines in the program, and describe
exactly how the user should interact with it. Ignore any errors that may occur due to
inappropriate input.

'''
#ANSWER
'''


1. from tkinter import *: Imports all classes and functions from the tkinter module, allowing the use of Tkinter widgets and methods.

2. window = Tk(): Creates the main window of the application.

3. frame = Frame(window): Creates a frame inside the main window to hold the widgets.

4. frame.pack(): Packs the frame into the main window, making it visible.

5. def compute():: Defines a function named compute which will be called when the user interacts with the GUI.

6. input_str = entry.get(): Retrieves the text entered by the user in the Entry widget and stores it in the variable input_str.

7. choice = option.get(): Retrieves the value selected by the user in the Radiobuttons (1 for Min, 2 for Avg) and stores it in the variable choice.

8. if choice == 1:: Checks if the user selected the option for finding the minimum value.

9. result = minList(input_str): Calls the minList function with the input string provided by the user and stores the result in the variable result.

10. else:: If the user didn't select the option for finding the minimum value.

11. result = avgList(input_str): Calls the avgList function with the input string provided by the user and stores the result in the variable result.

12. result_label.config(text=str(result)): Updates the text displayed in the result_label widget with the calculated result.

13. result_label.update(): Ensures that the result_label widget is updated with the new text.

14. entry = Entry(frame): Creates an Entry widget where the user can input a list of numbers.

15. entry.pack(): Packs the Entry widget into the frame.

16. result_label = Label(frame, text=""): Creates a Label widget to display the result.

17. result_label.pack(): Packs the result_label widget into the frame.

18. option = IntVar(): Creates an IntVar to store the value of the selected option (1 for Min, 2 for Avg) in the Radiobuttons.

19. radio_min = Radiobutton(frame, text="Min", variable=option, value=1, command=compute): Creates a Radiobutton widget for finding the minimum value, linked to the compute function.

20. radio_min.pack(): Packs the radio_min widget into the frame.

21. radio_avg = Radiobutton(frame, text="Avg", variable=option, value=2, command=compute): Creates a Radiobutton widget for calculating the average, linked to the compute function.

22. radio_avg.pack(): Packs the radio_avg widget into the frame.

23. exit_button = Button(frame, text="Exit", command=window.destroy): Creates a Button widget labeled "Exit" that closes the window when clicked.

24. exit_button.pack(): Packs the exit_button widget into the frame.

25. window.mainloop(): Starts the main event loop, allowing the user to interact with the GUI. The user can enter a list of numbers, select whether to find the minimum value or calculate the average, and click the Exit button to close the window.
'''
