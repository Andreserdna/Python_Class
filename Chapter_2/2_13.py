#2.13Write a program that prompts the user to enter a four-digit integer and displays the number in reverse order

userAnswer = (input("Enter an integer: "))

for x in reversed(userAnswer):
    print(x)
