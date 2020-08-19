

import random
print(random.randint(5, 20))  # line 1
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))  # line 3

#What did you see on line 1?
#The numbers are random integers from 5 to 20 inclusive, therefore the smallest is 5 and the highest is 20

#What did you see on line 2?
# The numbers are of a random range starting at the first number to the last in increments of the 3rd argument. (number are integers in this case numbers of ((start)+n(increment)<(end)))

#What did you see on Line 3?
#Produces a random float from start (inclusive) to end (exclusive). It can generate the start number but not the end.

print("My random number generator for integers 1-100 inclusive")
print(random.randint(1,100))