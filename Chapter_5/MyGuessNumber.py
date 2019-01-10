import random

computer_answer = random.randint(0,100)

print("Guess a magic number between 0 and 100")

user_answer = eval(input("Enter your Guess: "))

while user_answer != computer_answer:
	user_answer = eval(input("Enter your guess: "))

	if user_answer == computer_answer:
		print("Yes, the number is", computer_answer)
	elif user_answer > computer_answer:
		print("Your guess is too high!!")
	elif user_answer < computer_answer:
		print("Your guess is too low")