### Working with Conditionals
### In this exercise, you will edit a Python script to ship packages.

## Working with the if statement
userReply = input("Do you need to ship a package? (Enter yes or no) ")
# Use the if statement to print a response.
# Note: The == symbol is a comparative operator. It means is equal to. It's case sensetive
if userReply == "yes":
    print("We can help you ship that package!")
else:
    print("Please come back when you need to ship a package. Thank you.")    
    
## Note: The elif statement always comes after an if statement and before the else statement.

userReply = input("Would you like to buy stamps, buy an envelope, or make a copy? (Enter stamps, envelope, or copy) ")
if userReply == "stamps":
    print("We have many stamp designs to choose from.")
elif userReply == "envelope":
    print("We have many envelope sizes to choose from.")
elif userReply == "copy":
    copies = input("How many copies would you like? (Enter a number) ")
    print("Here are {} copies.".format(copies))
else:
    print("Thank you, please come again.")
    