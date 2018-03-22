'''
Create a program that asks the user for a number and then prints out a list of all the divisors of that number. 
 (If you don’t know what a divisor is, it is a number that divides evenly into another number. 
 For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)
 '''
# asks the user for a number
num = int(input("Please enter a number >>> "))

# creates a list of all numbers between 1 and the user's number + 1
x = list(range(1, num + 1))

# empty new divisors list
divisors = []

# iterate through all the numbers in x list
# if any numbers that equal 0 if modulo i
# append that number to new list
for i in x:
    if num % i == 0:
        divisors.append(i)

# prints out a list of all the divisors of that number
print(divisors)