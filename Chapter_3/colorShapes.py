import turtle

turtle.pensize(3) # setting the size of the pen
turtle.penup() # pulling the pen up so we dont write when we mobe
turtle.goto(-200,-50) # going to coordinatess
turtle.pendown() # putting the pendown to begin drawing the shape
turtle.begin_fill() # used to initalize the filling of the shape 
turtle.color("red") # color used for fill the shape
turtle.circle(40,steps=3) # draw the triangle
turtle.end_fill() # fill the shapte

turtle.penup()
turtle.goto(200,50)
turtle.pendown()
turtle.begin_fill()
turtle.color('red')
turtle.circle(40)
turtle.end_fill()
turtle.color('green')
turtle.penup()
turtle.goto(-100,50)
turtle.pendown()
turtle.write("cool colorful shapes",font=("Times",18,"bold"))
turtle.hideturtle()
turtle.done()
