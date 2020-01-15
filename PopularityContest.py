#Popular fast food restaurant
#Author: Tommy Shu
#Date: Feb 19,2019

#This program gets input from 5 users to find out
#what their favourite fast food restaurant is
#It prints out the numberof people who like McDonalds, KFC, AnW

#Initialize tallies
mcdonalds_tally = 0
kfc_tally=0
anw_tally=0

#Repeat the following 5 times
for i in range(5): #Range(5) is the same as [0,1,2,3,4]
    
    #Ask the user what their favourite fast food restaurant is
    favourite_fast_food_restaurant= input ("What's your favourite fast food restaurant?\n").lower()
    
    #If they say mcdonalds, add one to a mcdonalds tally
    if favourite_fast_food_restaurant.lower()== "mcdonalds":
        mcdonalds_tally+=1
    
    #If they say kfc, add one to a kfc_tally
    elif favourite_fast_food_restaurant.lower()=="kfc":
        kfc_tally+=1
    
    #If they say anw, add one to a anw_tally
    elif favourite_fast_food_restaurant.lower()=="anw":
        anw_tally+=1


#In the end, print out the tallies
print("mcdonalds:"+ str(mcdonalds_tally/5*100)+"%")
print("kfc:"+ str(kfc_tally/5*100)+"%")
print("anw:"+ str(anw_tally/5*100)+"%")