def decimalToHex(decimalValue):
	hex = " "

	while decimalValue != 0:
		hexValue = decimalValue % 16
		hex = toHexChar(hexValue) + hex
		decimalValue = decimalValue // 16
	return hex

#convert an intergerf to a single gex digit as a character
def toHexChar(hexValue):
	if 0 <= hexValue <= 9:
		return chr(hexValue + ord('0'))
	else:
		return chr(hexValue - 10 + ord('A'))

def main():
	#Prompt the user to ehnter decimal integer
	decimalValue = eval(input("enter a decimal number: "))

	print("The hex number for decimal",decimalValue, "is ", decimalToHex(decimalValue))

main()