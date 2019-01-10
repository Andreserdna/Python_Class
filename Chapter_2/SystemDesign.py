annualInterestRate = eval(input("Enter annual interest rate, e.g., 8.38: "))

monthlyInterestRate = annualInterestRate / 1200

numberOfYears = eval(input("Enter number of years an integer, e.g., 5: "))

#Enter loan amount

loanAmount = eval(input("Enter loan amount, e.g., 12000.89: "))

#Calculate Payment

monthlyPayment = loanAmount * monthlyInterestRate / (1 -1 / (1 + monthlyInterestRate) **(numberOfYears * 12))

totalPayment = monthlyPayment * numberOfYears * 12

#Display the results
print("the montly payment is", int(monthlyPayment * 100) / 100)
print("the total payment is",int(totalPayment * 100) / 100)



