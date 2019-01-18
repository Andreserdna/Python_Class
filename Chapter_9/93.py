from tkinter import *
import sys
class ProcessButtonEvent:
	def __init__(self):
		window = Tk()#creating the window
		btOK = Button(window,text="Ok",fg="red",command=self.processOK)
		btCancel = Button(window,text="cancel",bg="yellow",command=self.processCancel)
		btExit = Button(window,text="Close",bg="blue",fg="red",command=self.exitApplication)
		btExit.pack()
		btOK.pack() # pack the button to the window,
		btCancel.pack()# pack the cancel button to the window
		window.mainloop()
	def exitApplication(self):
		print("exiting application")
		sys.exit()
	def processOK(self):
		print("Ok button is clicked")
	def processCancel(self):
		print("Cancel button is clicked")
ProcessButtonEvent()