 # 5.17
# (Display the ASCII character table) Write a program that displays the characters
# in the ASCII character table from ! to ~. Display ten characters per line. 
# The characters are separated by exactly one space

#! = 33, ~ = 126
# for i in range(33,126):
#     print(chr(i).format(10,'.2f'),end=' ')

# for x in range(32,127):
# 	while i < 10: 
# 		for j in range(0,10):
# 			print(chr(x),end=' ')
# 		i+= 1
# 	print()
	# for x in range(0,11):
	# 	print(i)

#print(len(item1))
def print_ten(num1,num2):
	for x in range(num1,num2,1):
		print(chr(x),end=' ')
	print()

def print_tren(num,num2):
	i = 0
	while i < 10:
		for x in range(num,num2,1):
			print(chr(x),end=' ')
		print()
		i += 1 
# 	for x in range(43,53):
# 		print(chr(x),end=' ')
# 	#print(chr(i),end=' ')
# while i < 10:
print_ten(32,127)