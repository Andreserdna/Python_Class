import random
import sys
#4.17(Game: )
choices = ['scissor','rock','paper']


def print_statement(comp_answer,user_answer,list_items):
	print('Computer chose ' + str(list_items[comp_answer]) + \
		"\nYou chose " + str(list_items[user_answer]))

user_answer = int(input("Let's play a game of Rock, Paper, Scissors!\n\nPlease select from the following\nScissor(0), rock(1), paper(2): "))
computer_answer = random.randint(0,2)


#if draw
if user_answer == computer_answer:
	print_statement(computer_answer,user_answer,choices)
	print('Its a draw')
#sci loses to rock
elif user_answer == 0 and computer_answer == 1:
	print_statement(computer_answer,user_answer,choices)
	print("you lost!")
#sci wins over paper
elif user_answer == 0 and computer_answer == 2:
	print_statement(computer_answer,user_answer,choices)
	print("you won!")
#rock beats sci
elif user_answer == 1 and computer_answer == 0:
	print_statement(computer_answer,user_answer,choices)
	print("you won!")
#rock loses to paper
elif user_answer == 1 and computer_answer == 2:
	print_statement(computer_answer,user_answer,choices)
	print("you lost!")
#paper loses to sci
elif user_answer == 2 and computer_answer == 0:
	print_statement(computer_answer,user_answer,choices)
	print("you lost!")
#paper wins over rock
elif user_answer == 2 and computer_answer == 1:
	print_statement(computer_answer,user_answer,choices)
	print("you won!")

else:
	print("Did you make a proper selection?")
	sys.exit()