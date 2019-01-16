from HW8_4 import checkString
def main():
	user_string_input= input("enter a string: ")
	user_char_input = input("enter a character: ")
	cs = checkString(user_string_input,user_char_input)
	print(cs.print_result())
main()
