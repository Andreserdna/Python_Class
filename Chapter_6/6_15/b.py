def main():
	i = 0
	while i <= 4:
		function1(i)
		i += 1

		print("I is",i)
def function1(i):
	line  = ""
	while i >= 1:
		if i % 3 != 0:
			line += str(i) + " "
			i -= 1
	return line
main()