from tkinter import *

class ChangeLabelDemo:
	def __init__(self):
		window = Tk()
		window.title("Change Label Demo")

		#add a label to frame 1
		frame1 = Frame(window)
		frame1.pack()
		self.lbl = Label(frame1, text="Programminng is fun!")
		self.lbl.pack()

		#add a label, entry, button, and two radio buttons to frame2
		frame2 = Frame(window)
		frame2.pack()

		label = Label(frame2,text="Enter text: ")
		self.msg = StringVar()
		entry = Entry(frame2,textvariable=self.msg)

		btChangeText = Button(frame2,text="Change Text",command=self.processButton)
		self.v1 = StringVar()
		appleButton = Button(frame2,text="apple",fg="white",bg="red",command=self.processApple)
		rbRed = Radiobutton(frame2,text="Red",bg="red",variable=self.v1,value="R",command=self.processRadioButton)
		rbYellow = Radiobutton(frame2,text="Yellow",bg="yellow",variable=self.v1,value="R",command=self.processRadioButton)

		label.grid(row=1,column=1)
		entry.grid(row=1,column=2)
		btChangeText.grid(row=1,column=3)
		rbRed.grid(row=1,column=4)
		rbYellow.grid(row=1,column=5)
		appleButton.grid(row=1,column=1)

		window.mainloop()
	def processApple(self):
		if self.v1.get() == 'applez':
			print("hello")
	def processRadioButton(self):
		if self.v1.get() == "R":
			self.lbl["fg"] = "red"
		elif self.v1.get() == "Y":
			self.lbl["fg"] = "Yellow"
	def processButton(self):
		self.lbl["text"] = self.msg.get()
ChangeLabelDemo()