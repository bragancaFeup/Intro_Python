"""
Created on  2020

@author: António Brito / Carlos Bragança


#objective:  Given an integer value determine whether it is even or odd.
# Variables:
# n -> Number given
# quo -> The Quotient of the entire division of N by 2 EX: 7/2 -> 3
# rest -> The Rest of the entire division of N by 2 EX: 7/2 -> 0.5
"""


n = int (input ("Value:"))
quo = int (n / 2)
rest = n - quo * 2

if rest == 0:
     print ("The given value is even")
else:
     print ("The given value is odd")