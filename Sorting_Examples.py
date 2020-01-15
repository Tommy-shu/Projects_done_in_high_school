#Sorting_Examples
#Author: Tommy Shu 
#Date: 16 May, 2019

#Swaping example in a list
#Create a list
print(("swapping example").capitalize())
numbers = [0,1,2,3,4,5, 'before swarp.']
print (numbers)

#Swap the number at index 0 and 1
numbers[0], numbers[1] = numbers [1], numbers [0]
print (numbers)

#Swaping elements in a list
print(("range sublisting exmaple").capitalize())

#Create a list
numbers = [0,1,2,3,4,5]

#Iterating over a sublist from index 3 to the end
for i in range(3, len(numbers)):
    print (numbers[i])

#Selection Sort Example
print(("selection sort example\nThe list was...").capitalize())

#Create a list
scores = [39,2,103,42,50,61,75,42,53]

#print out the socres before sorting
print(scores)

#Loop through all the elements in the list
for i in range(len(scores)):
   
    #We want to find the smallest item
    #In the beginning, let's say our first element
    #is the smallest, until we find something smaller
    smallest_score = scores[i]
    smallest_index = i
   
    #Loop through all the elements except smallest_score
    for j in range(i+1,len(scores)):
        if scores[j]<smallest_score:
            
            #Found a smaller one
            smallest_score = scores[j]
            smallest_index = j
    
    #By the end of the loop, we should find the smallest
    #So, let's swap it with the first element of our sublist
    scores[smallest_index], scores[i] = scores[i], scores[smallest_index]

#Print out the list after sorting
print(scores)

#List Silicing Example
print(("list silicing example").capitalize())

#The list
letters = ["a","b","c","d","e"]
first_three = letters[:3]
last_bit = letters[3:]
middle = letters[2:4]
all_letters = letters[:]
print(first_three)
print(last_bit)
print(middle)
print(all_letters)

