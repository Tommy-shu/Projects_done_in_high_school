

def pet_dictionary():
     """ This fruitful function asks the user for the number of pets they have, and then asks themm for the number of the different type and name of each pet. A dictionary of pets is then returned."""
     # get the number of pets from the user
     num_pets = int(input("How many pets do you have? "))
     # initialize the house_pets dictionary
     house_pets={}
     
     # ask the name and type of each pet
     for i in range(num_pets):
          pet_type = input("Cool, what is one of the type of pets you have? ")
          # note: you can't have two of the same key in the dictionary.  If they have 3 cats only the last cat's name will exist.
          # we must update the key so they are all different
          pet_type = str(i) + ". " + pet_type
          house_pets[pet_type] = input("What is it's name? ")
     
     # return the dictionary of pets
     return (house_pets)

# get the dictionary of pets from the user by calling the pet_dictionary() function
household_pets = pet_dictionary()

# display the ditionary of pets
print("Wow that's quite a menagerie! It looks like you've said that you have...")
print(household_pets)

change_name = input("Would you like to change the name of a pet? yes/no ")

if change_name == "no":
     print("Okay thank you I've got the list of your pets.")
else:
     change_key=input("Which pet_type do you need to change the name of? Please enter the number and type as displayed above. ")
     household_pets[change_key]=input("What is the correct name for " + change_key +"? ")
     print("The updated pet list is...")
     print(household_pets)


# draw_nesting_square(shape_property_dictionar, color_switch):
#     if color_switch = 1
#         turtle.color = shape_prperty_dictionary[color_one]
#         color_switch = 2
#    else
#         turtle.color = shape_property_dictionary[color_two]
#         color_switch = 1
#    code to draw squaire

#    if shape_property_dictionary[size] > 10
#         shape_property_dictionary[size] -= 10
#         draw_nesting_square(shape_property_dictionary, color_switch):
