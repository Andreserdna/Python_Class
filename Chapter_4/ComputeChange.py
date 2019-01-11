#(Financial application: monetary units) Modify Listing 3.4, ComputeChange.py,
#to display the not equal to zero denominations only, using singular words for single units
#such as 1 dollar and 1 penny, and plural words for more than one unit such as 2
#dollars and 3 pennies



# Receive the amount
amount = eval(input("Enter an amount, for example, 11.56: "))

# Convert the amount to cents
remainingAmount = int(amount * 100)

# Find the number of one dollars
numberOfOneDollars = remainingAmount // 100
remainingAmount = remainingAmount % 100
# Find the number of quarters in the remaining amount
numberOfQuarters = remainingAmount // 25
remainingAmount = remainingAmount % 25
# Find the number of dimes in the remaining amount
numberOfDimes = remainingAmount // 10
remainingAmount = remainingAmount % 10

 # Find the number of nickels in the remaining amount
numberOfNickels = remainingAmount // 5
remainingAmount = remainingAmount % 5
# Find the number of pennies in the remaining amount
numberOfPennies = remainingAmount

# Display the results
print("Your amount", amount, "consists of: ")
if numberOfOneDollars == 0:
	pass
elif numberOfOneDollars <= 1:
	print('\t' + str(numberOfOneDollars) + ' '+ 'dollar')
elif numberOfOneDollars > 1:
	print('\t' + str(numberOfOneDollars) + ' '+ 'dollars')
if numberOfQuarters == 0:
	pass
elif numberOfQuarters <= 1:
	print('\t' + str(numberOfQuarters) + ' '+ 'quarter')
elif numberOfQuarters > 1:
	print('\t' + str(numberOfQuarters) + ' ' + 'quarters')
if numberOfDimes == 0:
	pass
elif numberOfDimes <= 1:
	print('\t' + str(numberOfDimes) + ' '+ 'dime')
elif numberOfDimes > 1:
	print('\t' + str(numberOfDimes) + ' ' + 'dimes')
if numberOfNickels == 0:
	 pass
elif numberOfNickels <= 1:
	print('\t' + str(numberOfNickels) + ' '+ 'nickel')
elif numberOfNickels > 1:
	print('\t' + str(numberOfNickels) + ' ' + 'nickels')
if numberOfPennies == 0:
	pass
elif numberOfPennies <= 1:
	print('\t' + str(numberOfPennies) + ' '+ 'penny')
elif numberOfPennies > 1:
	print('\t' + str(numberOfPennies) + ' ' + 'pennies')
