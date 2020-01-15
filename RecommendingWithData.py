#Recommending with data
#Author: Tommy Shu  
#Date: Feb 27, 2019
#This program can print out the survey answers

#Read the data containing survey answers
#and find out which spots were the favourites
#buy counting how many times each spot was voted for

#Open the file
file=open("responses.csv")

#Initialize tallies
club_ilia_tally = 0
uncle_faith_tally = 0  

#Remove the first (header) line of the file
junk = file.readline()

#Loop through the file
for data in file:

    #Split data(string) into a list
    datalist = data.split(",")
    
    #Access the item we want,e.g. 4th item start from 0
    answer = datalist[4]
    
    # Add to appropriate tally
    if answer == "Club Ilia":
        club_ilia_tally+=1
        
    elif answer== "Uncle Faith's":
        uncle_faith_tally+=1
    
#Print results
print("Club Ilia: " + str(club_ilia_tally))
print("Uncle Faith's: " + str(uncle_faith_tally))
    
#Make some comments about the results
if club_ilia_tally < 1:
    print("No one likes club Ilia :(")
elif club_ilia_tally >=1 and club_ilia_tally <5:
    print ("Not bad, Club Ilia")