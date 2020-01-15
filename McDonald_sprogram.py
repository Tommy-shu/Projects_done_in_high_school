#McDonald's program
#Author: Tommy Shu
#Date: Feb 26,2019
#This is a McDonald's program that takes your order and outpurs the total cost

#Set value for order
fries =3
burger=5
big_mac=8

#Initialize final value
final_value=0

#Make a list of questions
questions=["Would you like a burger for 5 dollars?(Yes/No)"," Would you like a fries for 3 dollors?(Yes/No)","Would you like a big Mac for 8 dollars?(Yes/No)",]
    
#Ask the first questions
print(questions[0])

#Let user response
response=input().lower()

#Add up value
if response=="yes":
    final_value+=burger

else:
    final_value+=0
    
#Ask the second questions
print(questions[1])

#Let uesr response
response=input().lower()


#Evaluate response
if response=="yes":
    final_value+=fries
    
else:
    final_value+=0

#Ask question 3
print(questions[2])

#Let user response
response=input().lower()

#Evaluate response
if response=="yes":
    final_value+=big_mac

else:
    final_value+=0

#Print final value with tax
final_value_with_tax = final_value*1.14
print("You order is $" + "% 0.2f" % final_value_with_tax + " dollars including tax")









    
    