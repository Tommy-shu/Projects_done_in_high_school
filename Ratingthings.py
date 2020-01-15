#Quick Rater App
#Autor:Tommy Shu
#Date: Feb 20, 2019

#This is a movie rater app, it will ask you about your favourite
#and then rate the movie out of 5

#Greetings
print("Welcome to movie rater. I'd like you to answer a few questions.")

#Ask what is the your favourite movie
print(" What is your favourite movie?")

#User response
movie=input()

#Make a list of questions 
questions=["How interesting is the plot out of 5?\n","How would you rate the music out of 5?\n", "Out of 5, how would you rate the actors?\n"]

#Initialize score
final_score=0

#Go through each question and get rating
for q in questions:
    rating= float(input(q))
    final_score+=rating
    
#Calculate final score
number_of_questions= len(questions)
print("You've rated this movie"+ str(final_score/number_of_questions))