#A Nosy Question Bot 
#Author: Tommy Shu
#Date: Feb 08,2019
#Description: Asks you from a list of questions and reply them all

import random
import time

#Introduction
print("Hello! This is Nosy Question Bot. I'd like to ask you somequestions! Here we go>")

#Pause for a second
time.sleep(1)

#Create questions list
questions = ["Given the choice of anyone in the world, whom would you want as a dinner guest?", "Would you like to be famous? In what way?" , "Before making a telephone call, do you ever repharse what you are going to say? Why?", "What would constitute a 'Perfect' day for you?"]

#Make a responses list
responses=["Interesting.", "I see!", "Fascinating."]

#Make a loop that will ask the questions from the list
for question in questions:
    
    #Print the question
    print(question)
    
    #Get the response
    input()
    
    #Make a reply
    print(random.choice(responses))
    
#End it offf
print("You are a super intersting person! Thanks for replying eo my questions.")