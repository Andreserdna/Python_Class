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
def format_values_feet(fNum1,mNum2):
	sNum1 = str(fNum1)
	sNum2 = str(mNum2)

	print()
def format_values_meter(fNum1,mNum2,list1):
	for items in list1:
		pass
def print_header():
	print("Feet\t\t\tMeters\t\t"+'|'+"\tMeters\t\tFeet")

def feet_number_incrementor(number1,number2, incrementor):
	for value in range(number1,number2,incrementor):
		feet_list = (value / 10) * 10
		s1 = ('\t\t\t' + str(footToMeter(feet_list)))
		print(str(feet_list) + s1)

def meter_number_incrementor(number1,number2, incrementor):
	for value in range(number1,number2,incrementor):
		meter_list = (value / 1) 
		s1 = ('\t\t\t' + str(meterToFeet(meter_list)))
		list1.append(meter_list)

	return list1
def number_incrementor(number1,number2,number3,number4,inc1=1,inc2=6):
	for value in range(number1,number2,inc1):
		feet_list =(value / 10) * 10
		s1 = ('\t\t\t' + str(footToMeter(feet_list)))
		print(str(feet_list) + s1)
	for value2 in range(number3,number4,inc2):
		meter_list = (value2 / 1) 
		s2 = (meterToFeet(meter_list))
		print("\t\t\t" +format(meter_list,'30.2f')+ format(s2,'20.2f')) 

				#compute_commision(decide_commision(value),value)
def main(): 

	print_header()

	#feet_number_incrementor(1,11,1,meter_number_incrementor(20,55,6,meter_list))
	number_incrementor(1,11,20,55)
	#meter_number_incrementor(20,55,6)
main()
