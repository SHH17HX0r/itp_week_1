# ITP Week 1 Day 2 Exercise

# Take an user's input for his age
age = input('What is your age? ?')

# The user input comes in as a string so we have to cast it to a int!
age = int(age)

# Use an if/else to determine if they are of legal drinking age.
# if the user is of age, print "Welcome!"
# else, tell them to come back in X amount of years (use math operations)

if age <= 21:
    print('Welcome')
else:
    print("Come back in " + str(age - 21) + " years")

# Bonus: Add a validation by checking the type of the user input
# to ensure it can be casted as an int. Handle any other input that
# are not numbers to try again.
