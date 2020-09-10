

"""
Created on  2020

@author: António Brito / Carlos Bragança


#objective: 
    Calculate the roots of a quadratic equation. 
    If there are no real roots must be sent an appropriate Message
    
# Variables:
# A -> Coefficient of x2
# B -> Coefficient of x
# C -> Independent coefficient
# delta -> Binomial discriminant
# X1, X2 -> Roots of the equation
"""

import math


A = float (input ("Coefficient of x2:"))
B = float (input ("Coefficient of x:"))
C = float (input ("Independent coefficient:"))
if A == 0:
     print ("the equation is not of the second degree")
else:
     delta = B * B - 4 * A * C


     if delta> 0:
         # Two real and distinct roots
         X1 = (- B + math.sqrt (delta)) / (2 * A)
         X2 = (- B - math.sqrt (delta)) / (2 * A)
         print ("Two real roots: X1 =" + str (X1) + "X2 =" + str (X2))
     elif delta == 0:
         # Double real root
         X1 = - B / (2 * A)
         print ("Double root X =" + str (X1))
     else:
         # Imaginary roots
         print ("There are no real roots")
