from tkinter import *

class GridManager:
	window = Tk()
	window.title("Grid Manager Demo")

	message = Message(window,text="this message widget occupies three rows and two columsn")
	message.grid(row=1,column=1,rowspan=3,columnspan=2)
	Label(window,text="First Name:").grid(row=1,column=3)
	Entry(window).grid(row=1,column=4,padx=5,pady=5)
	Label(window,text="Last Name").grid(row=2,column=3)
	Entry(window).grid(row=2,column=4)
	Button(window,text="Get Name").grid(row=3,padx=5,pady=50,column=4,sticky=E)
	window.mainloop()

GridManager()