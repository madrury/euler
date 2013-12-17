# Read in the cipher
F = open('cipher1.txt')
L = F.readline().strip()
L = L.split(',')
# Get the numerical ascii values of the targets
ciph = [int(c) for c in L]

# Length of the message
l = len(L)
# Number of times to repeat decoder string
repeats = l / 3
extra = l % 3

# Generate a list of three element decoder strings codes
alph = 'abcdefghijklmnopqrstuvwxyz'
decoders = []
for c1 in alph:
	for c2 in alph:
		for c3 in alph:
			decoders.append(c1 + c2 + c3)
		
# Take a three character decoder string and convert is to a ascii list with the same 
# length as the message to be decoded	
def toFullDecoder(decoderStr):
	decoder = []
	for i in range(repeats):
		for char in decoderStr:
			decoder.append(ord(char))
	for i in range(extra):
		decoder.append(ord(decoderStr[i]))
	return decoder
	
# Count the occurrences of sublists in a list
def countOccur(subLst, lst):
	lnLst = len(lst)
	lnSubLst = len(subLst)
	cnt = 0
	for i in range(lnLst - lnSubLst + 1):
		if all(lst[i + j] == subLst[j] for j in range(lnSubLst)):
			cnt += 1
	return cnt 
	
# Common english words
commWords = {'the': [ord('t'), ord('h'), ord('e')],
             'The': [ord('T'), ord('h'), ord('w')],
             'an': [ord('a'), ord('n')],
             'An': [ord('A'), ord('n')],
             'of': [ord('o'), ord('f')],
             'Of': [ord('O'), ord('f')],
             'be': [ord('b'), ord('e')],
             'Be': [ord('B'), ord('e')],
             'to': [ord('t'), ord('o')],
             'To': [ord('T'), ord('o')],
             'and': [ord('a'), ord('n'), ord('d')],
             'And': [ord('A'), ord('n'), ord('d')]}
             
# Now solve the problem
ans = 'aaa'
maxMatches = 0
# Check all the three digit decoders 
for dec in decoders:
	fullDec = toFullDecoder(dec)
	# Now create the full decoded message
	decoded = []
	for i in range(l):
		decoded.append(ciph[i] ^ fullDec[i])  # XOR with full decoder digit
	# Now check for the common english words
	matches = 0
	for word in commWords:
		matches += countOccur(commWords[word], decoded)
	print dec, matches
	# Now see if we've done better
	if matches > maxMatches:
		ans = dec
		maxMatches = matches
		
print 'The decoder string is ', ans
print 'Which results in', maxMatches, 'matches to common english words'

decoded = []
fullDec = toFullDecoder(ans)
for i in range(l):
	decoded.append(ciph[i] ^ fullDec[i])  # XOR with full decoder digit
	
decodedMsg = ''.join([chr(n) for n in decoded])
print decodedMsg
print 'The sum of the ascii values is ', sum(decoded)

			


