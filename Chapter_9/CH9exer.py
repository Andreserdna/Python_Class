from tkinter import *

class Exer:
	def __init__(self):
		window = Tk()
		window.title("Chaper 9 Exercises")

		frame1 = Frame(window)
		frame1.pack()
		self.lbl = Label(frame1,text="welcome",fg="white",bg='red')
		self.lbl.pack()
		button1 = Button(frame1,text="OK",fg='white',bg='red')
		frame2 = Frame(window)
		frame2.pack()
		self.v1 = StringVar()
		self.msg = StringVar()
		checkButton = Button(frame2,text='apple',fg='red',bg='white',command=self.processApple)
		entry = Entry(frame2,fg='white',bg='red',textvariable = self.msg)
		mess = Message(frame2,text="welcome!!!")
		#placing the buttons
		self.lbl.grid(row=1,column=1)
		button1.grid(row=1,column=2)
		checkButton.grid(row=1,column=3)
		entry.grid(row=1,column=4)
		mess["justify"] = LEFT
		mess.grid(row=2,column=8)

		window.mainloop()

	def processApple(self):
		if self.v1.get():
			print("hello")



Exer()
