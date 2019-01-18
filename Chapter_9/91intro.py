from tkinter import *

window = Tk() #create the window
label = Label(window,text="welcome to python")#create the label
button = Button(window,text="click me")#create the button
label.pack()# place the label in the window
button.pack()#place the button in the window
window.mainloop()# create an event loop