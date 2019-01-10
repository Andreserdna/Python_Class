answer = int(input("Enter an ASCII code between 0 and 127: "))


if answer > 127:
	print("ASCII code must between 0 and 127 try again")
else:
	print("The character is: ", chr(answer))
