def rearrangements(string):
    '''Returns a list containing all the rearangements of a string.'''
    # Stop condition: a one charecter strings only rearrangement is itself
    if len(string) == 1:
        return [string]
    # Otherwise pull off the first charecter, and insert in every place in 
    # every rearrangement of the resulting shorter string
    else:
        holderList = []
	# Pull off the first charecter
        firstChar, lastChars = string[0], string[1:] 
	# Loop over all the rarrangements of the substring          
	for rerange in rearrangements(lastChars): 
	    # Loop over every place in the rearrangement to insert the missing charecter  
            for i in range(len(rerange) + 1):   
	        # Insert the missing charecter
                holderList.append(''.join([rerange[:i], firstChar, rerange[i:]]))   
        return holderList

def make_histogram(s):
    from collections import Counter
    hist = Counter()
    for char in s:
        hist[char] += 1
    return hist

def is_rearrangement(this, that):
    return make_histogram(this) == make_histogram(that)

def rotations(string):
    '''Returns a list of rotations of a string'''
    ansList = []
    for i in range(len(string)):
        ansList.append(''.join([string[i:], string[:i]]))
    return ansList
