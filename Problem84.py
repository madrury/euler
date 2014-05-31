# The monopoly problem.  Problem statement omitted because it's really long.
# 
# If it were not for the triple-double rule, this problem would be a simple
# markov chain, and i would have used numpy or R to solve it.  Given this, it
# seems easier to build a small simulation and run it for a long time.

from random import shuffle, choice
from collections import deque, Counter

# The number of squares on the board
num_squares = 40

# Special squares
go_square = 0
jail_square = 10
gt_jail_square = 30
c1_square = 11
e3_square = 24
h2_square = 39
r1_square = 5
rw_squares = [5, 15, 25, 35]
ut_squares = [12, 28]
cc_squares = set([2, 17, 33])
ch_squares = set([7, 22, 36])

def make_deck(cards):
    '''Make, shuffle and return a deck of cards'''
    shuffle(cards)
    return deque(cards)

def draw_card(deck):
    '''Draw a card from the top and put it on the bottom'''
    card = deck.pop()
    deck.appendleft(card)
    return card

def roll_dice(sides_tuple):
    '''Roll a collection of dice and return the sum'''
    return [choice(range(1, num_sides + 1)) for num_sides in sides_tuple]

def add_to_buffer(roll, roll_buffer):
    '''Adds the current roll to a buffer keeping track of the three most recent
    rolls.
    '''
    if len(roll_buffer) != 3:
        roll_buffer.append(roll)
    else:
        roll_buffer.popleft()
	roll_buffer.append(roll)

def bad_doubles(roll_buffer):
    '''Checks if the buffer contains three consecutive doubles.'''
    if len(roll_buffer) != 3:
        return False
    else:
        return all(roll[0] == roll[1] for roll in roll_buffer)

def next_rw(current_square):
    '''Find the next reailway square.'''
    for rw_square in rw_squares:
        if rw_square > current_square: return rw_square
    else:
        return rw_squares[0]

def next_ut(current_square):
    '''Find the next utility square.'''
    for ut_square in ut_squares:
        if ut_square > current_square: return ut_square
    else:
        return ut_squares[0]

def simulate(dice_tuple, num_rounds):
    '''Simulate a game for a given choice of dice, and for a given number of
    rounds. Returns the three most commonly visited squares, as requested. 
    '''
    #-------------------------------------------------------------------------
    # Setup
    #-------------------------------------------------------------------------
    # A counter to keep track of the frequencies that squares were visited.
    ctr = Counter()
    # A buffer to keep track of the last three rolls
    roll_buffer = deque([])
    # Make the community chest and chance decks
    cc_deck = make_deck(range(16))
    ch_deck = make_deck(range(16))
    # Start at go, square zero
    current_square = go_square
    #-------------------------------------------------------------------------
    # Run the simulation
    #-------------------------------------------------------------------------
    for round in range(num_rounds):
        roll = roll_dice(dice_tuple)
	add_to_buffer(roll, roll_buffer)
	# Check if there are three consecutive doubles, this is bad.
	if bad_doubles(roll_buffer):
	    current_square = jail_square
	else:
	    current_square = (current_square + sum(roll)) % num_squares
	    # Deal with deck spaces, community chest and chance
            if current_square in ch_squares:
                ch_card = draw_card(ch_deck)
		if ch_card == 0:
		    current_square = go_square
		if ch_card == 1:
		    current_square = jail_square
		if ch_card == 2:
		    current_square = c1_square
		if ch_card == 3:
		    current_square = e3_square
		if ch_card == 4:
		    current_square = h2_square
		if ch_card == 5:
		    current_square = r1_square
		if ch_card == 6 or ch_card == 7:
		    current_square = next_rw(current_square)
		if ch_card == 8:
		    current_square = next_ut(current_square)
		if ch_card == 9:
                    current_square = (current_square - 3) % num_squares
	    # Edge case, you can land on a community chest after moving back
	    # three from chance!
	    if current_square in cc_squares:
		cc_card = draw_card(cc_deck)
		if cc_card == 0: 
		    current_square = go_square
		if cc_card == 1: 
		    current_square = jail_square
            if current_square == gt_jail_square:
		current_square = jail_square
        # We ended the round, where are we?
        ctr[current_square] += 1
    return ctr.most_common(3)
