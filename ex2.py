# Ask the user for a number. 
number = int(input("Please enter a number >>> "))

# Depending on whether the number is even or odd, print out an appropriate message to the user. 
even_odd = number % 2
if even_odd > 0:
    print("That number is odd")
else:
    print("That number is even")

# If the number is a multiple of 4, print out a different message.
div_four = even_odd / 4
if div_four == 0:
    print("AND That number is divisible by 4")

# Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). 
print("Now please enter two more numbers")
num = int(input("First number >>> "))
check = int(input("Second number >>> "))

# If check divides evenly into num, tell that to the user. 
# If not, print a different appropriate message.
if num % check == 0:
    print("The second number divides evenly into the first!")
else:
    print("The second number doesn't divide evenly into the first. :(")