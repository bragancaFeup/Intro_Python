
"""
Created on  2020

@author: António Brito / Carlos Bragança


#objective: 
    Given a list of N values calculate the arithmetic mean.

      # Variables:
          N -> Number of list values
          value -> List values
          k -> Cycle index
          sumValues -> Sum of list values
          mean -> Arithmetic mean of list values
"""

N = int (input ("Number of list values:"))
sumValues = 0     # Initializes the sumValues variable

# Reading cycle and sum of list values
k = 1
while k <= N:
     value = float (input ("Value:"))
     sumValues = sumValues + value
     k = k + 1

mean = sumValues / N # Calculates the arithmetic mean

print ("Arithmetic mean = {}" .format (mean))