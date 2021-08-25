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

print(usr_num)

# usr_num = int(usr_num)

print(usr_num)

multi2 = usr_num * 2
print(multi2)

add10 = multi2 + 10
print(add10)

div2 = add10/2

fin_num = div2 - usr_num
fin_num = int(fin_num)

print("Your final number is 5  " + str(fin_num))
