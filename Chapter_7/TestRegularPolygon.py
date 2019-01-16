from HW7_5 import RegularPolygon

def main():
	reg1 = RegularPolygon()
	reg2 = RegularPolygon(6,4)
	reg3 = RegularPolygon(10,4,5.6,7.8)
	print("area for reg1: ", reg1.getArea(),"perimeter is", reg1.getPerimeter())
	print("area for reg2: ", reg2.getArea(),"perimeter is", reg2.getPerimeter())
	print("area for reg3: ", reg3.getArea(),"perimeter is", reg3.getPerimeter())
main()