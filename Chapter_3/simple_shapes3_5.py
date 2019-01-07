import turtle

turtle.pensize(3) #set the pen thickness to 3 pixels
turtle.penup() # pull the pen up
turtle.goto(-200, -50)
turtle.pendown() # pull the pen down
turtle.circle(40,steps=7) # Draw the triangle

turtle.penup()
turtle.goto(-100,-50)
turtle.pendown()
turtle.circle(40, steps=4) # draw a square

turtle.penup()
turtle.goto(0,-50)
turtle.pendown()
turtle.circle(40, steps=5) # draw a pentagon

turtle.penup()
turtle.goto(100,-50)
turtle.pendown()
turtle.circle(40, steps=6) # draw a hexagon

turtle.penup()
turtle.goto(200,-50)
turtle.pendown()
turtle.circle(40)

turtle.done()