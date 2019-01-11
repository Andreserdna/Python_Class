#4.11 (Find the number of days in a month) Write a program that prompts the user to
#enter the month and year and displays the number of days in the month. For example, if the user entered month 2 and year 2000, #the program should display that
#February 2000 has 29 days. If the user entered month 3 and year 2005, the program should display that March 2005 has 31 days. 

user_month = int(input("Please Enter a month: "))
user_year = eval(input("Enter a year: "))
month31 = {1:"January",3:"March",5:"May",7:"July",10:"October",12:"December"}
month30 = {4:"April",6:"June",9:"September",11:"November"}

isLeapYear = (user_year % 4 == 0 and user_year % 100 != 0) or \
	(user_year % 400 == 0)

if user_month == 2 and isLeapYear == True:
	print("February " + str(user_year) + " has 29 days!")
elif user_month == 2 and isLeapYear == False:
	print("February " + str(user_year) + " has 28 days!")

if user_month in month31:
	print(str(month31[user_month]) + ' ' + str(user_year) + ' ' + 'has 31 days')

if user_month in month30:
	print(str(month30[user_month]) + ' '+ str(user_year) + ' '+ 'has 30 days')
#print(user_year, "is a is leap year?", isLeapYear)