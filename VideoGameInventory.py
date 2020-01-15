#VideoGameInventory
#Author: Tommy Shu
#Date: Apr 24, 2019

#######################Algorithm
#print("what video game you are making an inventory for?")
#answer = int(input("How many items players can have in the inventory?"))
#def game_inventory():
    #inventory_dic = {}
    #for i in range (answer):
      #type = input("What type of item it is?")
      #inventory_dic = type
      #name = input("What is the name of the item?")
      #inventory_dic[type] = name
    #print("inventory_dic")
    #answer2 = ("If you like to change any name of the items?Y/N").upper())
    #if answer2 == Y:
      #type = input("Please enter the type of item that you want to change.")
      #name = input("What name do you want to change into?")
      #inventory_dic[type] = name
    #else:
      #print("Good!You've already made your own game!")
##########################Code

def game_inventory():
    """This fuction will ask user for their inventory equipments and create a dictionary"""
    #Initialize the dictonary
    inventory_dic = {}
    
    #Run through number of times to get the keys and value
    for i in range (answer):
        
        #Get the type names
        type_name = input("What type of item it is?")
        
        #Get the item names
        name = input("What is the name of the item?")
        
        #Match the keys and values
        inventory_dic[type_name] = name
        
    #Return the fuction
    return inventory_dic


def change_name():
    """This fuction will help the user to change their item name in dictionary"""
    
    #Get the change name of the types
    type_name = input("Which type of item do you want to change?")
    
    #Get the new item name
    name = input("What name do you want to change into?")
    
    #Change the item name in dictionary
    equipment[type_name] = name
    
    #print out the new dictionary
    print(equipment)
    
    
#######################main program
#Ask user the name of the game that they want to create items for
game = input("what video game you are making an inventory for?")

#Ask user how many items do they want the players to have
answer = int(input("How many items players can have in the game "+game+"?"))

#Call the function
equipment = game_inventory()

#Print out the equipment dictionary to show the user their decisions
print(equipment)

#Ask user if they want to change their minds or not
change_decision = input("If you like to change the name of any of the items?Y/N\n").upper()

#If the answer is Y, call the change name fuction, if it's N, print out congradulation
if change_decision == "Y":
    
    #Call the function
    change_name()
    
    #Ask if the user want to make anymore changes
    second_change_decision = input("Would you like to do anymore changes?Y/N\n").upper()
    
    #If the answer is yes, call the change name fuction
    if second_change_decision == "Y":
        change_name()
        
    #If the answer is no, print out congradulation
    elif second_change_decision == "N":
        print("Good!You've already made your own game inventory!")
        
#If the answer is no, print out congradulation
elif change_decision == "N":
    print("Good!You've already made your own game inventory!")


