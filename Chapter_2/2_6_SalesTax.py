#2.6 salestax.py

purchaseAmount = eval(input("Enter a purchase amount: "))
tax = purchaseAmount * 0.06

print("Sales tax is", int(tax * 100) / 100)
