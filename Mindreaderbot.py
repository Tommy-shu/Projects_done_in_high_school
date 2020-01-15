#How Well Do You Know Me?
#Author: Tommy Shu  
#Date: Feb 07,2019

#Description:This is a 2-player game where you The 1st player reads a word,
#and secretly enters 3words they associate with it.
#If it's a match, they win!

import time
number=0

#Introduce the game
print("Welcome to Mind Reader!")
print("score:",number)

word_list=["cat", "dog", "cow", "elephant"]


for word in word_list:
        
    #Aske the first player to enter 3 words associated with a given word
    print("Player 1, enter 3 words you think when I say " + word + ": \n")
    
    #Get the 3 words
    first=input("First word:")
    second=input("Second Word:")
    third=input("third word:")
    
    #Puse for 1 second
    time.sleep(1)
    
    #Clear the screen
    for i in range (200):
        print( )
    
    #Ask the 2nd player to guess an associated word
    print("Player 2, what is one word you think Player 1 associates with" + word + ": \n")
    guess= input()
    
    #Check if they match and tell them if they won!
    if guess in [first,second,third]:
        print("You've got it!")
        number +=1
        print("score: " + str(number))
    
    else:
        print("Wrong, you lose.")
    