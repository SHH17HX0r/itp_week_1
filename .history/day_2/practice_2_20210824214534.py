# This is a number magic trick
# Pick a number from 1 - 9
# Multiple by 2
# Add 10 to the total
# Divide by 2
# Subtract by the original number
# Final number is 5

# Take an user's input
# Assign a new variable for each step
# at the end, use an if statement to see if the final is always 5!

usr_num = input("Enter any number between 1-9: ")

usr_num = int(usr_num)

multi2 = usr_num * 2

add10 = multi2 + 100

fin_num = usr_num - add10

print(fin_num)
