#Nesting Square
#Author: Tommy Shu
#Date: Apr 05,2019

######################################ALGORITHM 
#def get_properties():
#   size_num=int(input("What size do you want for the square??(Enter a number between 50 and 300"))
#   colour1=input("What is the first colour you want for the square?")
#   colour2=input("What is the second colour you want for the square?")
#   shape_properties_dictionary={}
#   dict={"first_colour":colour1,"second_colour":colour2,"size":size_num}

#def drawing_nesting_square(shape_property_dictionary, color_switch):
    #t=turtle.Turtle()
    #color_switch=1
    #if color_switch==1:
        #turtle.color(shape_property_dictionary["first_color"])
        
    #else:
        #color_switch==2
        #turtle.color(shape_property_dictionary["second_color"])

#for i in range(4):
    #t.forward(get_properties["size"])
    #t.right(90)
#size-=10

#if size=>5:
  #drawing_nesting_square(shape_property_dictionary, color_switch)

#else:
    #turtle.done()

#get_properties()
#drawing_nesting_square(shape_property_dictionary, color_switch)
######################################CODE
def get_properties():
    """this function ask user for the size, first colour and second colour of the largest square
    then collect all the information into a dictionary
    return the dictionary"""
    
    #initialize the dictionary
    shape_property_dictionary={}
    
    #ask user for the size, colour1 and colour2 for the square
    shape_property_dictionary['size'] = int(input("What size do you want for the square?(Enter a number between 50 and 300)"))
    while shape_property_dictionary['size']>300 or shape_property_dictionary['size']<50:
        shape_property_dictionary['size']=int(input("What size do you want for the square?(Enter a number between 50 and 300)"))
    shape_property_dictionary['colour1'] = input("What is the first colour you want for the square?")
    shape_property_dictionary['colour2'] = input("What is the second colour you want for the square?")
    
    #return the value
    return shape_property_dictionary
    
def drawing_nesting_square(shape_property_dictionary, color_switch):
    """this function uses the dictionary to determine and switch the colour of square
    then draw the square and repeat it untill the size of square is less than 5"""
    import turtle
    t=turtle.Turtle()
    t.speed(100)

    #switch the colour between colour1 and colour2
    if color_switch==1:
        tcolor=shape_property_dictionary['colour1']
        t.color(tcolor)
        color_switch = 2
    else:
        t.color(shape_property_dictionary['colour2'])
        color_switch = 1
        
    #draw the square and subtract the size each time
    for i in range(4):
        t.forward(shape_property_dictionary['size'])
        t.right(90)
    shape_property_dictionary['size']-=10
    
    #base case
    if shape_property_dictionary['size'] >5:
        drawing_nesting_square(shape_property_dictionary, color_switch)
    else:
        turtle.done()

#call the function    
properties_dictionary = get_properties()
drawing_nesting_square(properties_dictionary, 1)
    
    
    
    