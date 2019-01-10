userInput = eval(input("enter a dollar amount in decimals e.g., 11.58: "))

cents = int(userInput * 100)

numberOfDollars = cents // 100

remainingCents = numberOfDollars % 100

numberOfQuarters = remainingCents // 25

remainQuarts = numberOfQuarters % 25

numberOfDimes = remainQuarts // 10

remainDimes = numberOfDimes % 10

numberOfNickels = remainDimes // 5

remainNicks = numberOfNickels % 5

print("your amount", userInput, "consists of\n",
	"\t", numberOfDollars, "dollars\n",
	"\t", numberOfQuarters,"quarters\n",
	"\t", numberOfDimes,"dimes\n",
	"\t", numberOfNickels,"nickels\n",
	"\t", remainNicks,"pennies")
