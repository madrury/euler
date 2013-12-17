'''
     Take the number 192 and multiply it by each of 1, 2, and 3:

     192 * 1 = 192
     192 * 2 = 384
     192 * 3 = 576
     By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated product of 192 and (1,2,3)

     The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645, which is the concatenated 
     product of 9 and (1,2,3,4,5).  

     What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where 
    n > 1?
'''

# The digit frequency histogram of a pandigital number
panHist = dict((i, 1) for i in range(1, 10))
panHist[0] = 0
def isPandigital(num):
    '''Oracle: determines if an integer is 1-9 pandigital.'''
    # Create a histogram of digit frequencies
    numStr = str(num)
    numHist = dict((i, 0) for i in range(0, 10))
    for char in numStr:
        numHist[int(char)] += 1
    return (numHist == panHist)

ansList = []
# The most digits we can have are 5, since there are only 9 places in the completed product
for num in range(10000):
    numStr = str(num)
    fact = 2
    while len(numStr) < 9:
        adjStr = str(num*fact)
        numStr = numStr + adjStr
        fact += 1
    print numStr, isPandigital(numStr)
    if isPandigital(numStr):
        ansList.append(int(numStr))
        
print ansList
print max(ansList)