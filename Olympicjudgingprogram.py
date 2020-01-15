#Olympic Judging program
#Author: Tommy Shu
#Date: Feb 25, 2019
#The program will outputs the average scores from 5 differernt judges

#Ask questions
print("How well do you think is the performance of the althlete out of 10? (half points are allowed)")

#Initialize final score
final_score = 0

#let judges input the scores
scores=["Judge 1:", "Judge 2:","Judge 3:","Judge 14:","Judge 5:"]

#Go through each score and  get rating
for q in scores:
    rating=float(input(q))
    final_score += rating

#Print fianl score
number_of_socres=len(scores)
print("Your Olympic score is" + str(final_score/number_of_socres) )
    