 
subtotal = float(input("Enter subtotal: "))
grat = float(input("Enter gratuity: "))
grat_conversion = grat / 100
grat_subtotal = grat_conversion * subtotal
final_subtotal = grat_subtotal + subtotal
print ("The gratuity is " + str(grat_subtotal) + " and the total is " + str(final_subtotal))
