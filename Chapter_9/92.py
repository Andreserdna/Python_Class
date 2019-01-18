from tkinter import *

def processOK():
	print("Ok the buttton is clicked")
def processCancel():
	print("cancel button is clicked")
window = Tk()
btOk = Button(window, text="ok",fg="red",bg="red",command=processOK)
btCancel = Button(window,text="cancel",bg="yellow",command=processCancel)
btOk.pack()#place the ok button in the windown
btCancel.pack()#place the ok button in the window

window.mainloop()