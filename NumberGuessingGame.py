#NumberGuessingGame
#Author: Tommy Shu
#Date: Apr 27, 2019

##############################ALGORITHM
#def random_num ():
#   return (random.randomrange[0,100])
#guessing_answer = int(input("Please give me a positive interger between 0 and 100, then I will check if it is too high or too low.")
#def valid_num (guessing_answer):
#while True:
#   guessing_answer >= 0 and guessing_answer <= 100
#   return True
# else:
#   return False
# def comparing_num(guessing_answer):
#   valid_num(guessing_answer)
#   if guessing_answer > random_num():
#       print("Too high!Please enter another number.")
#       comparing_num(guessing_answer)
#   if guessing_answer < random_num():
#       print("Too low!Please enter another number.")
#       comparing_num(guessing_answer)
#   else:
#       print("You are correct!")
################################CODE
import random
def random_num ():
  """This function will create a random number for user to guess"""
  #random number function
  random_number = random.randrange(0,100)
  #return the random number
  return random_number   

       
def valid_num (guessing_answer):
  """This function will check if user's input is valid"""
  #Chek if user's input is smaller than zero or larger than 100
  if guessing_answer <= 0 or guessing_answer >= 100:
    #Return a Boolean value
    return False
  else:
    return True


def comparing_num(random_number, guessing_answer):
  """This function will compare user's input with the random number that was given"""  
  #Call the valid_num fuction
  guess = valid_num(guessing_answer)

  #Keep looping if user's input is invalid
  while not guess:

    #Ask for the new guessing answer
    guessing_answer = int(input("Please enter a positive number for your guessing answer: "))

    #Call the function
    guess = valid_num(guessing_answer)
  
  if guessing_answer > random_number:

    #Ask user to enter another guessing number
    guessing_answer = int(input("Too high!Please enter another number."))

    #Call the comparing function
    comparing_num(random_number,guessing_answer)
    
  elif guessing_answer < random_number:

    #Ask user to enter another guessing number
    guessing_answer = int(input("Too low!Please enter another number."))

    #Call the comparing function
    comparing_num(random_number,guessing_answer)
  else:

    #Print out the words
    print("You are correct!")

#Initialize a random number
random_number = random_num()

#Ask user for their guessing number
guessing_answer = int(input("Please give me a positive interger between 0 and 100, then I will check if it is too high or too low.\n"))

#Call the comparing funcion
comparing_num(random_number, guessing_answer)