#Convert from binary to decimal
#Author: Tommy Shu  
#Date: Mar 06,2019

#Get an input string wirh a binary number
binary_input = input("Input a binary number: ")

#Initialize the accumulator
decimal_output = 0

#Length of the string
length=len(binary_input)

#Loop through each character in the string
for i in range(length):
    
    #Start from the last character in the string, going right to left
        bit_index =length-1-i
        
    #If the bit value is 1
        bit =binary_input[bit_index]
        
    #Add 2 to the power of that bit's index
        if bit =="1":
            decimal_output+=2**i
            
#Output the total in decimal
print("That's equal to " + str(decimal_output))
