sKilo = "Kilograms"
sPounds = "Pounds"

#function to convertKiloTopunds`6y 

#Function for formatting strings
def stringFormatter(kiloString,poundString):
	fString = (format(kiloString,"<30"))
	print(fString,poundString)


stringFormatter(sKilo,sPounds)

for number in range(0,23):
	conversion = number * 2.2
	print(number,format(conversion,'35.2f'))