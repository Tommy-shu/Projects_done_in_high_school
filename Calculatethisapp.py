#Temperature Calculator
#Author: Tommy Shu
#Date: Feb 21,2019

#This Calculator can convert Celsius degree to Kevin degree
#by using the equations kevin degree = celsius degree + 273.5 

#Convert temperature Celsius degrees to Kevlin
celsius_degree = float(input(" What is the temperature?(in Celsius degree)\n").lower().strip("celcius "))

#Output temperature in kevlin
kevlin_degree= celsius_degree+273.15

print("That is "+ str(kevlin_degree) + " Kevlin degree.")