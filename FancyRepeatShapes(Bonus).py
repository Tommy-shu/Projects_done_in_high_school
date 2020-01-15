#Fancy repeat shapes
#Author: Tommy Shu
#Date: Mar 12,2019

#Create two turtles (A and B)
#Choose pen colors for both turtles
#Build a for loop for A to move as a square
#Build a for loop for B to move as a circle
#Hide the turtle
#End the program

######CODE#########
#Create two turtles
import turtle
center_graph=turtle.Turtle()
outside_graph=turtle.Turtle()

#Choose pen colors for both turtles
center_graph.color("red")
outside_graph.color("orange")

#Set a speed for both turtles
center_graph.speed(50)
outside_graph.speed(50)

#Build a for loop for A to move as a squre
for times in range(12):
     center_graph.left(150)
     for inside_times in range(4):
          center_graph.forward(200)
          center_graph.left(90)
     
#Build a for loop for outside_graph to move as a circle
for times in range(12):
     outside_graph.left(150)
     outside_graph.circle(147)
    
#Hide the turtle
center_graph.hideturtle()
outside_graph.hideturtle()

#Finish the program
turtle.done()
    

