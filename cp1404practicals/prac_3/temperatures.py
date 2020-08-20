#TEMPERATURE (mk2)

def c_to_f_converter(c):
    """Takes fahrenheit input and returns celsius equivalent"""
    f = c * 9.0 / 5 + 32
    return f

def f_to_c_converter(f):
    """Takes celsius input and returns fahrenheit equivalent"""
    c = 5 / 9 * (f - 32)
    return c


def main():
    MENU =  """C - Convert Celsius to Fahrenheit
    F - Convert Fahrenheit to Celsius
    Q - Quit"""
    print(MENU)
    #This changes whatever the input is into upper case
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            #Conversion now takes place in separate function
            fahrenheit = c_to_f_converter(celsius)
            print("Result: {:.2f} F".format(fahrenheit))
        elif choice == "F":
            fahrenheit = float(input("Fahreheit: "))
            #Conversion now takes place in separate function
            celsius = f_to_c_converter(fahrenheit)
            print("Result: {:.2f} C".format(celsius))
        else:
            print("Invalid option")
            print(MENU)
            choice = input(">>> ").upper()
    print("Thank you.")

main()