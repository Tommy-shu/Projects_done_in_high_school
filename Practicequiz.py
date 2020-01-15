# An asking name Robort
#Author: Tommy Shu      
#Date: Feb 11,2019

#Make a list of Good names
Good_names=["bob","susan","big bird","oscar","bert","ernie","grover","abby","elmo"]

#Ask the user for their name
print("what is your name?")

#Get the respone from the user
name=input().lower()

#Reply the author
if name in Good_names:
    print("You are so lucky because there is a Sesame Street charcater with the same name.")
else:
    print("You have a nice name but it's too bad there isn't a Sesame Street character named after them.")