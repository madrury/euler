'''
    An irrational decimal fraction is created by concatenating the positive integers:
        0.123456789101112131415161718192021...
    It can be seen that the 12th digit of the fractional part is 1.  If dn represents the nth digit of the fractional part, find the value of the
    following expression.
       d1 * d10 * d100 * d1000 * d10000 * d100000 * d1000000
'''

def numStrings():
    num = 1
    while True:
        numStr = str(num)
        yield numStr
        num += 1
        
count = 1  # Keep count of where we are
factDict = {1: None, 10: None, 100: None, 1000: None, 10000: None, 100000: None, 1000000: None}
for numStr in numStrings():
    for digit in numStr:
        if count in factDict:
            factDict[count] = int(digit)
        count += 1
    if count > 1000000:
        break
    
print factDict

F = 1
for entry in factDict:
	F = F*factDict[entry]
	
print F