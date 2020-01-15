#PalindromeChecker
#Author: Tommy Shu
#Date: Mar 15, 2019

#DISCRIPTION
#This is a Palindrome checker, you can input your name to see if it is Palindrome!

#Algorithmn
#Ask user for the word
#Get the answer from user's input
#Check if user's answer is Palindrome
#Create a fuction define if the name is Palindrome
#def palindrome_checker(word):
#    start=0
#    end = len(word)-1
#    while start<end:
#        if word[start] != word[end]:
#             return False
#             start+=1
#             end-=1
#    else:
#             return True
#if palindrome_checker(word) ==True
#print("That is a palindrome!")
#if palindrome_checker(word) ==False
#print("That is no palindrome!")


#Define a function to check if the word is palindrome or not
def palindrome_checker(word):
    """The function can check if the words are palindrome"""
    #initialize the start character
    start = 0
    
    #end character
    end = len(word)-1
    
    #While loop loop through every letter
    while start < end:
        
        #return False if start and end characters are different
        if word[start] != word[end]:
            return False
        start +=1
        end -=1
        
    else:
            return True
        
#Make a question to ask for input word
word = input("Enter a word to check if it is palindrome or not?\n")

#Call the function
palindrome_checker(word)

#If statement to print out the result
if palindrome_checker(word) == True:
    print("That's a palindrome!")
    
elif palindrome_checker(word) == False:
    print("That's no palindrome!")