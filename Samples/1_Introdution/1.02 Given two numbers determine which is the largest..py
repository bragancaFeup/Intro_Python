"""
Created on  2020

@author: António Brito / Carlos Bragança


#objective: Given two numbers determine which is the largest.


"""

value1 = float (input ("First value:"))
value2 = float (input ("Second value:"))

if value1> value2:
     maximum = value1
else:
     maximum = value2

print ("Maximum value is =" + str (maximum))
