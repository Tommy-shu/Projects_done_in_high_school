#City Bliss Evaluator
#Author: Tommy Shu
#Date: Feb 20, 2019
#Helps you figure put what job is best


#Introduciton
print("What city would you like to evaluate?")
city=input()
print("Ok, let's evaluate" + city+ "!\n")

#Questions
questions=["How would you rate the enviornment out of 5?\n","How would you rate the safty out of 5?\n", "How yould you rate the public transport out of 5?\n"]

#Initialze score
final_score=0

#Go through each question
for question in questions:
    rating= int(input(question))
    weight=int(input("And how important is that to you, out of 5?\n"))
    final_score= final_score + rating*weight
    print()
    
print("You've rated" + city +"as" +str(fianl_score/(25*len(questions))))