# Create a program that asks the user to enter their name and their age. 
# Print out a message addressed to them that tells them the year that they will turn 100 years old.

# Extras:
# Add on to the previous program by asking the user for another number and printing out that many copies of the previous message. 
# (Hint: order of operations exists in Python)
# Print out that many copies of the previous message on separate lines. 
# (Hint: the string "\n is the same as pressing the ENTER button)

# ask user for their name and store name
# ask user for their age and store age
name = input("Please tell me your name >>> ")
age = int(input("Please tell me your age >>> "))

# once you have the user's age, subtract it by 100 to see how much to add to the year
year = str((2018 - age) + 100)


# ask user for the amount of times they want to print the year
# get the number from the user
# store number of times in function
times_to_print = int(input("How many times do you want to print this? >>> "))

# print a message for the user telling them the year they will be 100 years old 
# print the message the amount specificed about of times
age_100 = print("\n %s will be 100 years old in %s \n" % (name, year) * times_to_print)