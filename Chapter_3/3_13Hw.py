import turtle

turtle.pensize(5)
turtle.screensize(200,200)

turtle.home()
turtle.begin_fill()
turtle.color('red')
turtle.circle(100,steps=6)
turtle.end_fill()
turtle.penup()

turtle.goto(-50,75)
turtle.color('white')
turtle.pendown()
turtle.write("STOP",font=("Times",30,"bold"))
turtle.hideturtle()
turtle.done()