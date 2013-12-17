'''
    The nth term of the sequence of triangle numbers is given by, tn = (1/2)*n*(n+1); so the first ten triangle numbers are:
        1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
    By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we form a word value. For    
    example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle number then we shall call the word a triangle word.

    Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common English words, how many are  
    triangle words?
'''

def isTriangle(num):
    '''Tests if a number is trinagular <--> 8*num + 1 is a square.'''
    testNum = 8*num + 1
    counter = 1
    square = 1
    # Is 8*num + 1 a square?
    while square <= testNum:
        square = counter**2
        if square == testNum:
            return True
        counter += 1
    return False

def letterVal(char):
    '''Get the letter value by offsetting the askii code.'''
    return ord(char) - 64

def wordVal(word):
    '''Sum up letter values to get a word value.'''
    return sum(letterVal(char) for char in word)

# Load in the file with all the words
f = open("words.txt", "r")
bigString = f.readline()
# Make a list of the words
listOfWords = bigString.split(",")
# Then strip the quote from around the word
listOfWords = [word[1:len(word) - 1] for word in listOfWords]    

ansList = []
# Loop through the list of words and calculate the word value
for word in listOfWords:
    if isTriangle(wordVal(word)):
        ansList.append(word)
        
print ansList
print len(ansList)



    