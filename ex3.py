'''
Take a list, say for example this one:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
and write a program that prints out all the elements of the list that are less than 5.

Extras:

Instead of printing the elements one by one, make a new list that has all the elements less than 5 from this list in it and print out this new list.
Write this in one line of Python.
Ask the user for a number and return a list that contains only elements from the original list a that are smaller than that number given by the user.
'''

# Take a list
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Ask the user for a number
num = int(input("Please choose a number between 1 and 10 >>> "))

# make a new list that has all the elements less than 5 from this list in it and print out this new list
new_list = []

# prints out all the elements of the list that are less than 5
for i in my_list:
    if i < num & num < 10:
        new_list.append(i)

# return a list that contains only elements from the original list a that are smaller than that number given by the user
print(new_list)