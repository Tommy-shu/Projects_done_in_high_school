#How's it Going Bot     
#Author: Tommy Shu      
#Date: Feb 04, 2019

#Description: This bot will ask you how it's goinf and make a comment depengding on how you answered

#Ask user how it's going 
print("How's it going?")

#Get the user's reply
reply= input()

#If they said Good, them reply Good!
if reply == "Good":
    print("Good!")

#Otherwise, if they said Bad, then reply Oh no!
elif reply== "Bad":
     print ("Oh no!")

# In all other cases, reply "I see ...."    
else:
    print ("I see....")