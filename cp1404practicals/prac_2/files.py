###NAME.TXT###
#Takes name and saves it to "name.txt" file
name_file = open("name.txt","w")
name = str(input("What is your name?\n>>>"))
name = name.title()
print(name,file=name_file)
name_file.close()

#Deletes name to prove I'm not cheating
name = ""

#Reopens the file and reads and prints it
name_file = open("name.txt","r")
#Name is stored back in name var
name = name_file.readline()
print("Your name is {}".format(name))
name_file.close()



###NUMBERS.TXT###
#Opens the file and writes numbers to it
numbers_file = open("numbers.txt","w")
numbers = [17,42,400]
for i in range(len(numbers)):
    print("{}".format(numbers[i]),file=numbers_file)
numbers_file.close()

#Reopens the file to read only. (Could just change the open type earlier. This is safer)
numbers_file = open("numbers.txt","r")
read_numbers = []
#Adds the numbers back one by one as elements in array
for line in numbers_file:
    integer_number = int(line)
    read_numbers.append(integer_number)

#Adding the first 2 numbers (ensures it is only 2 by indexing from the start)
sum_of_two = sum(read_numbers[0:2])
print("The sum of the first two elements is",sum_of_two)

#Adding all numbers
sum_of_all = sum(read_numbers)
print("The sum of all numbers is",sum_of_all)

#ALWAYS CLOSE FILE
numbers_file.close()