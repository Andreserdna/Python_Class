import random

number1 = random.randint(0,9)
number2 = random.randint(0,9)

if number1 < number2:
	number1,number2 = number2,number1

answer = eval(input("what is" + str(number1) + '-' + str(number2) + '?'))

#4 repeatedly as the question until the answer is correct

while number1 - number2 != answer:
	answer = eval(input("what is" + str(number1) + '-' + str(number2) + '?'))

print("You got it!")
