
"""
Created on  2020

@author: António Brito / Carlos Bragança


#objective: 
     Given an integer value determine its factors (numbers that divide the given number).
 # Variables:
         value -> Value given
         limDiv -> Maximum value of the potential divisors of the given value
         divisor -> Potential divisors of the given value
         quoc -> Integer Value Quotient / divisor
         rest -> Rest of the entire Value / divisor division
"""

value = int (input ("Value:"))

limDiv = int (value / 2) # No value greater than its half can be its divisor except himself

# Cycle to obtain the potential divisors of the given value
divisor = 1
while divisor <= limDiv:
     quoc = int (value / divisor)
     rest = value - quoc * divisor
     if rest == 0:
         print ("Divisores" + str (divisor)) # It is divisor of the given value

     divisor = divisor + 1

print ("Divisores {0}" .format (value)) # Every number is a divisor of itself