'''
    The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some order, but it also has a  
    rather interesting sub-string divisibility property.

    Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:
        d2d3d4=406 is divisible by 2
        d3d4d5=063 is divisible by 3
        d4d5d6=635 is divisible by 5
        d5d6d7=357 is divisible by 7
        d6d7d8=572 is divisible by 11
        d7d8d9=728 is divisible by 13
        d8d9d10=289 is divisible by 17
    Find the sum of all 0 to 9 pandigital numbers with this property.
'''

from StringUtilities import rearrangements

# Create a list of all the 0 to 9 pandigitals
listOfNums = rearrangements('0123456789')
# If the first digit is 0 it is not a 10 digit number
# listOfNums = [numStr for numStr in listOfNums if numStr[0] != "0"]

# What primes to test what positions divisibility by
testDict = {1:2, 2:3, 3:5, 4:7, 5:11, 6:13, 7:17}

ansList = []
# Loop over the pandigitals and check the properties
for numStr in listOfNums:
    if all([int(numStr[i:i+3])%testDict[i] == 0 for i in range(1, 8)]):
        ansList.append(int(numStr))
        
print ansList
print sum(num for num in ansList)