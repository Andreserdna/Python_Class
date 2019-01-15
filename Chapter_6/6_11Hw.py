def decide_commision(sales_amount):
	if sales_amount <= 0.01 or sales_amount <= 5000:
		#print("8 percent")
		return 8
	elif sales_amount <= 5000.01 or sales_amount <= 10000:
		#print("10 percent")
		return 10
	elif sales_amount >= 10000.01:
		#print("12 percent")
		return 12
		
def incrementor(number1,number2, incrementor):
	for value in range(number1,number2,incrementor):
		compute_commision(decide_commision(value),value)
def compute_commision(commision, sAmount):
	print(sAmount,"\t\t\t\t",(commision / 100) * sAmount)
	return (commision / 100) * sAmount

def print_tables():
	print("Sales Amount\t\t\tComission")

def main():
	print_tables()
	incrementor(1000,100000,500)
main()