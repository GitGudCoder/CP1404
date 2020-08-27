

numbers = [3, 1, 4, 1, 5, 9, 2]

print(numbers[0]) # Will print '3' (first item)
print(numbers[-1]) # Will print '2' (last item)
print(numbers[3]) # Will print '1' (4th item)
print(numbers[:-1]) # Will print all but last item
print(numbers[3:4]) # Will print '[1]' (list slice is a list and is exclusive of second value
print(5 in numbers) # Will print "True"
print(7 in numbers) # Will print "False"
print("3" in numbers) # Will print "False" as "3" is a string, when all items in numbers list are integers
print(type(numbers[0])) # <--- See? class is int.
print(numbers + [6, 5, 3],"\n") # Will print concatenated list "[3, 1, 4, 1, 5, 9, 2, 6, 5, 3]"
#                                                         |<- original list ->||<addition>|

# 1. Change first item to "ten
numbers[0] = "ten"
# 2. Change last item to 1
numbers[-1] = 1
print(numbers)
# 3. Get all the elements from numbers except for the first 2
sliced_numbers = numbers[2:]
print(sliced_numbers)
# 4. See if 9 is in numbers
print(9 in numbers)
