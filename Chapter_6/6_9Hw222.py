# #Ch 6 Programming Assignment:
# #Exercise 6.9, 6.11, 6.18, (6.16)
# #Andres Valenzuela Tamayo

# #6.9 (Conversions between feet and meters) Write a module that contains the following two functions:
# #converts from feet to meters
# 	def footToMeter(foot):

# #converts from meters to feet
# 	def meterToFeet(meter):

# #the formulas for the conversion are
# foot = meter / 0.305
# meter = 0.305 * foot

# #Write a test program that invokes these functions to display the following tables:
# Feet 		Meters 		| 		Metes 		Feet
# 1.0			0.305		|		20.0		66.574
# 2.0			0.610		|		26.0		81.967
# ...
# 9.0			2.745		|		60.0		196.721
# 10.0		3.050		|		66.0		213.115

def footToMeter(foot):
	return 0.305 * foot
def meterToFeet(meter):
	return meter / 0.305

def print_header():
	print("Feet\t\t\tMeters\t\t"+'|'+"\tMeters\t\tFeet")

def number_incrementor(number1,number2,number3,number4,inc1=1,inc2=6):
	for value in range(number1,number2,inc1):
		feet_list =(value / 10) * 10
		s1 = ('\t\t\t' + str(footToMeter(feet_list)))
		print(str(feet_list) + s1)
		for value2 in range(number3,number4,inc2):
			meter_list = (value2 / 1) 
			s2 = (meterToFeet(meter_list))
			print("\t\t\t" +format(meter_list,'30.2f')+ format(s2,'20.2f')) 


def main(): 

	print_header()


	number_incrementor(1,11,20,55)

main()
