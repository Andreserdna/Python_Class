from tkinter import *

class CanvasDemo:
	def __init__(self):
		window = Tk() #creating the tk 
		window.title("canvas demo") #set the title
		#place the canvas in the window
		self.canvas = Canvas(window, width = 200, height = 100,bg="white")
		self.canvas.pack()

		#place buttons in the frame
		frame= Frame(window)
		frame.pack()
		#creating the buttons and assigning the funvtion commands
		btRectangle = Button(frame,text="Rectangle",command=self.displayRect)
		btOval = Button(frame,text="oval",command=self.displayOval)
		btArc = Button(frame,text='Arc',command=self.displayArc)
		btPolygon = Button(frame,text="polygon",command=self.displayPolygon)
		btString = Button(frame,text='string',command=self.displayString)
		btLine = Button(frame,text="string",command=self.displayLine)
		btClear = Button(frame,text='clear',command=self.clearCanvas)
		e913 = Button(frame,text="913",command=self.drawLine913)
		#aligning the buttons

		btRectangle.grid(row=1,column=1)
		btOval.grid(row=1,column=2)
		btArc.grid(row=1,column=3)
		btPolygon.grid(row=1,column=4)
		btString.grid(row=1,column=5)
		btLine.grid(row=1,column=6)
		btClear.grid(row=1,column=7)
		e913.grid(row=1,column=8)

		window.mainloop()#creating an event loop


	def displayRect(self):
		self.canvas.create_rectangle(10, 10, 190, 90, tags = "rect")
# Display an oval
	def displayOval(self):
		self.canvas.create_oval(10, 10, 190, 90, fill = "red",
			tags = "oval")
# Display an arc
	def drawLine913(self):
		self.canvas.create_rectangle(10,10,190,90,start=70,extent=70,height=100,width=100,fill='blue',tags="e913")
	def displayArc(self):
		self.canvas.create_arc(10, 10, 190, 90, start = 0,
			extent = 90, width = 8, fill = "red", tags = "arc")
# Display a polygon
	def displayPolygon(self):
		self.canvas.create_polygon(10, 10, 190, 90, 30, 50,
			tags = "polygon")
# Display a line
	def displayLine(self):
		self.canvas.create_line(10, 10, 190, 90, fill = "red",
		tags = "line")
		self.canvas.create_line(10, 90, 190, 10, width = 9,
		arrow = "last", activefill = "blue", tags = "line")
# Display a string
	def displayString(self):
		self.canvas.create_text(60, 40, text = "Hi, I am a string",
			font = "Times 10 bold underline", tags = "string")
# Clear drawings
	def clearCanvas(self):
		self.canvas.delete("rect", "oval", "arc", "polygon",
			"line", "string",'e913')

CanvasDemo()