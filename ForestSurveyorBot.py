#Forest Surveyor Bot
#Author: Tommy Shu
#Date: May 05, 2019

##################ALGORITHM######################
#tree_number = input("How many tree shall we survey?")
#def valid_input (tree_number):
   #while not int(tree_number) >=0:
      #tree_number = input("Please enter a valid input (positive interger): ")
   #else:
      #return True
   
#def tree_data(tree_number):
   #tree_height_list = []
   #for i in range(int(tree_number)):
      #tree_height = int(input("Enter a tree height: "))
      #valid_input (tree_height)
      #tree_height_list.append (tree_height)
   #print (tree_height_list)
   #return tree_height_list
#def tall_tree (tree_height_list):
   #height_min = input("Let's caluculate the number of tall trees. What's the min height?")
   #valid_input (height_min)
   #while not int(height_min) ==" ":
      #for i in range(len(tree_height_list)):
         #if tree_height < height_min:
            #tree_height_list.remove(tree_height)
            #tall_tree = tree_height_list
         #else:
            #return tall_tree
#########################################CODE############
         
def positive_or_negative(tree_number):
    """This function can check if the input is valid and return a boolean value"""

    #Return a Boolean value to check if user's input is positive or negative
    if int(tree_number) >0 :
        return True
    else:
        return False
    
    
def tree_height(valid_answer,tree_number):
    """This function can get the tree height and return a tree height list"""

    #Initialize tree height list
    tree_height_list = []
    while not valid_answer:

        #Ask user for number of tree that they want to survey
        tree_number = input("Please enter a positive interger for how many trees shall we survey?")

        #Check if the input is positive integer
        valid_answer = positive_or_negative(tree_number)
    else:

        #Loop through the function number of tree times
        for i in range(int(tree_number)):

            #Ask for tree height 
            tree_height = input("Enter a tree height: ")

            #Check if the input is positive or negative
            positive_or_negative(tree_height)

            #Keeps looping if the input is not positive integer
            while not positive_or_negative(tree_height):

                #Keep asking if the input is invalid
                tree_height = input("Please enter a positive interger for tree height: ")
            else:

                #Add valid input to the list
                tree_height_list.append(tree_height)

        #Return the list
        return tree_height_list
    
    
def tall_trees(tree_height_list):
    """This fuction can calculate how many trees are higher than min height"""  \
    #Initialize tall_trees
    tall_trees = 0
    
    #Initialize a condition
    flag = False

    #Keep looping if False
    while not flag:
        
        #Ask for min height
        min_height = input("Let's calculate the number of tall trees. What's the min height?\n")
        
        #If user input nothing
        if min_height == "":
        
            #Print out stop words
            print("Got it,the program is stopped.")

            #Return a boolean value to stop the loop
            return True

        #Check validity of input
        positive_or_negative(min_height)

        #Keep looping if False
        while not positive_or_negative(min_height):

            #Asking for min height
            min_height = input("Please enter a positive integer for min height: ")

            #Loop number of times
        for i in range(len(tree_height_list)):
            if int(tree_height_list[i-1]) > int(min_height) :

                #Remove the short trees from the list
                tall_trees +=1

        #Print out words
        print("There are "+ str(tall_trees) + " tall trees")
        
        #Reintialize tall_trees 
        tall_trees = 0

#Ask for tree number
tree_number = input("How many trees shall we survey?")

#Call valid_answer function
valid_answer = positive_or_negative(tree_number)

#Call tree_height function
tree_height_list = tree_height(valid_answer,tree_number)

#Call tall trees function
tall_trees(tree_height_list)