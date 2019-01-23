NUMBER_OF_ELEMENT = 5
numbers = []
sum = 0

for i in range(NUMBER_OF_ELEMENT):
	value = eval(input("enter a new number: "))
	numbers.append(value)
	sum += value

average = sum / NUMBER_OF_ELEMENT

count = 0
for i in range(NUMBER_OF_ELEMENT):
	if numbers[i] > average:
		count += 1

print("average is ", average)
print("number of elements above average is", count)