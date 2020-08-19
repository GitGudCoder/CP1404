"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""
###ORIGINAL CODE###
# try:
#     numerator = int(input("Enter the numerator: "))
#     denominator = int(input("Enter the denominator: "))
#     fraction = numerator / denominator
#     print(fraction)
# except ValueError:
#     print("Numerator and denominator must be valid numbers!")
# except ZeroDivisionError:
#     print("Cannot divide by zero!")
# print("Finished.")

#1. A value error will occur when a value other than the expected type. In this case the numerator and denominator MUST BE integers. A float or string will produce this error

#2. Zero division error is what it says: If you attempt to divide by zero, this error will occur

#3.
###MODIFIED CODE###
#Code will avoid carrying out division if answer of zero is detected using an if statement
try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    #Detect denominator of zero
    if denominator == 0:
        print("Cannot divide by zero!")
    else:
        fraction = numerator / denominator
        print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
#This will not be needed
# except ZeroDivisionError:
#     print("Cannot divide by zero!")
print("Finished.")