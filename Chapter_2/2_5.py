def total(int1,int2):
    if isinstance(int1,int):
        print
def tip_equation(tip_p):
    return tip_p / 100
        
def main():
    subtotal = float(input("Enter subtotal: "))
    grat = int(input("Enter gratuity: "))
    grat_conversion = grat / 100
    grat_subtotal = grat_conversion * subtotal
    final_subtotal = grat_subtotal + subtotal
    print ("The gratuity is " + str(grat_subtotal) + " and the total is " + str(final_subtotal))
if __name__ == "__main__":
    main()

