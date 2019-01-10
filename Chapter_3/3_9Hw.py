#user input
employeeName = input("Enter Employees name: ")
numberOfHoursWorked = eval(input("Enter number of hours worked per week: "))
hourlyPayRate = eval(input("Enter hourly rate: "))
federalTaxWith = eval(input("Enter federal tax withholding rate: "))
stateTaxWith = eval(input("Enter state tax withholding rate: " ))

#Gross pay formula
grossPay = hourlyPayRate * numberOfHoursWorked

#function to convert float to percentage
def convert_to_percentage(value):
	return value * 100

#Federal and tax withholdings formuls
federalTaxPercentageHeld =  (convert_to_percentage(federalTaxWith) * grossPay) / 100

stateTaxPercentageHeld = (convert_to_percentage(stateTaxWith) * grossPay) / 100
totalDeductions = federalTaxPercentageHeld + stateTaxPercentageHeld
netPay = grossPay - totalDeductions

print("Employee name: ",employeeName)
print("Hours worked: ",numberOfHoursWorked)
print("Pay Rate :", hourlyPayRate)
print("Gross Pay: ", grossPay)
print("Deductions: \n",
        "\t", "Federal Withholding: " + "(" + str(format(federalTaxWith,".2%")) + ")" + '$' ,format(federalTaxPercentageHeld,".2f"),"\n",
        "\t", "State Withholding: " + "(" + str(format(stateTaxWith,".2%")) + ")" +'$',format(stateTaxPercentageHeld,".2f"),"\n",
        "\t", "Total Deduction: ",'$',format(totalDeductions,".2f"),"\n",
        "Net Pay: ", '$',str(netPay).strip())

