import random

number = random.randint(0,100)

print("Guess a magic number between 0 and 100")

guess = -1

while guess != number:
	guess = eval(input("enter your guess: "))

	if guess == number:
		print("yes, the number is", number)
	elif guess > number:
		print("your guess is too high!!!")
	elif guess < number:
		print("Your guess is too low!!")