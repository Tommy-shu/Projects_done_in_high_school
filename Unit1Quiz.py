#Star Wars bot
#Author: Tommy Shu  
#Date: Feb 13,2019
# Description:This bot will determine if you can be on the Dark side, or the Light side.Just response to the questions!


#Instruction
print("Yoda must decide if you can be a jedi knight of if you are destined to become a sith. Answer yes or no for the questions.")

#Ask if red is your favourite colour?
print("Is red your favourite colour?(yes/no)")

#User answer1
answer1=input().lower().strip("!").strip(" ")

#Ask if you like capes
print("Do you like capes?(yes/no)")

#User answer2
answer2=input().lower().strip("!").strip(" ")

#Make different comments to user's responses
if answer1==("yes") or answer2==("yes"):
    print("On the path to the dark side you are.")
    
elif answer1==("no") and answer2==("no"):
    print("The light side of the force welcomes you.")