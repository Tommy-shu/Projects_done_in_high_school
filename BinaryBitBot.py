#Binary Bit Bot
#Author:Tommy Shu
#Date: Mar 07,2019

#ALGORITHM
#Initialize the base
#Define the fuction with base and exponent and then print the question to get the number of bits
#Evaluate if the answer is suitable, if not, print please give me a number between 1 and 8
#if the answer is suitable, print (2, answer) in range of the answer.

#Initialization
base= 2

#Define fuction
def exponent(base,exponent):
    print(base**exponent)

#Welcome instruction
print("Welcome to Binary Bit Bot.")

#Get the number of bits 
num_bits=int(input("How many bits? Enter a number between 1 and 8: "))

#Evaluate the number
if num_bits>8 or num_bits<1:
    print("please give me a number between 1 and 8....")

else:
    #Output of binary bits
    for number in range(num_bits):
        exponent(base,number)