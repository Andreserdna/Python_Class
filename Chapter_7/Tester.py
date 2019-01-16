from Circle7_1 import Circle

def main():
	#Create the circle with radius 1
	circle = Circle()
	print("the area of the circle of radius",circle.radius,"is",circle.getArea())

	#Create a circle with radius 25
	circle2 = Circle(25)
	print("the area of the circle of radius",circle2.radius,"is",circle2.getArea())
	
	#Create a circle with the radius of 125
	circle3 = Circle(125)
	print("the area of the circle of radius",circle3.radius,"is",circle3.getArea())

	#modify the circle radius
	circle2.radius = 100
	print("the area of the circle of radius",circle2.radius,"is",circle2.getArea())
main()
