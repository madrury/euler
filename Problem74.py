digit_factorials = {0: 1, 1: 1, 2: 2, 3: 6, 4: 24,
                    5: 120, 6: 720, 7: 5040,
		    8: 40320, 9: 362880}

cycle_lengths = {}

def next(n):
    return sum(digit_factorials[int(c)] for c in str(n))

N = 1000000

for i in range(1, N+1):
    len_counter = 0
    state = i
    chain = [i]
    while i not in cycle_lengths:
        state = next(state)
	len_counter += 1
	if state in cycle_lengths:
	    cycle_lengths[i] = len_counter + cycle_lengths[state]
        elif state in chain:
	    cycle_lengths[i] = len_counter
	# Fallthrough
	chain.append(state)

print sum(1 for x in cycle_lengths if cycle_lengths[x] == 60)	       
