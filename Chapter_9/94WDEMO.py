from tkinter import *

class WidgetsDemo:
	def __init__(self):
		window = Tk()# create the window
		window.title("Widgets Demo") #set a title for the window

		#add a check button and a radio
		#button fo frame1 
		frame1 = Frame(window)#create and add a frame to the window
		frame1.pack()# packing frame to window
		self.v1 = IntVar()

		cbtBold = Checkbutton(frame1, text="Bold",variable=self.v1,command=self.processCheckButton)
		self.v2 = IntVar()
		rbRed = Radiobutton(frame1,text="Red",bg="red",variable=self.v2,value=1,command=self.processRadioButton)
		rbYellow = Radiobutton(frame1,text="Yellow",bg="yellow",variable=self.v2,value=2,command=self.processRadioButton)
		cbtBold.grid(row=1,column=1)
		rbRed.grid(row=1,column=2)
		rbYellow.grid(row=1,column=3)

		#Add a label,an entry, a button,and a message to frame1
		frame2 = Frame(window)
		frame2.pack()
		label = Label(frame2,text="enter your name: ")
		self.name = StringVar()
		entryName = Entry(frame2,textvariable=self.name)
		btGetName = Button(frame2,text="Get Name",command=self.processButton)
		message = Message(frame2,text="Its a widgets demo")
		label.grid(row=1,column=1)
		entryName.grid(row=1,column=2)
		btGetName.grid(row=1,column=3)
		message.grid(row=1,column=4)

		#add text
		text = Text(window)
		text.pack()
		text.insert(END,"Tip\nThe best way to learn Tkinter is to read ")
		text.insert(END,"these carefully designed examples and use them")
		text.insert(END,"to create your applications. ")

		window.mainloop()
	def processCheckButton(self):
		print("check button is " + ("checked" if self.v1.get() == 1 else "unchecked"))
	def processRadioButton(self):
		print(("Red" if self.v2.get() == 1 else "unchecked"))
	def processButton(self):
		print("Your name is " + self.name.get())


WidgetsDemo()