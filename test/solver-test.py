# ------------------
# Q Table

# Q = {
#		(((1,2,3), (), ()), (1,2)): 0.6,
#		(((1,2,3), (), ()), (1,3)): 0.5,
#		(((2,3), (1), ()), (2,1)): 0.9,
#	  } 
import random
import numpy as np
from copy import deepcopy
x = ['a',2,3,4]
def makeMove(state, move):
	if move != None:
		state3 = deepcopy(state)
		# Get the pegs from and to which the moves are to be done.
		source = move[0]
		dest = move[1]
		# Get the disk from source
		disk = state3[source - 1][0]
		# Remove from source
		state3[source-1].remove(disk)
		# Move disk to destination
		state3[dest - 1].insert(0, disk)
		return state3

def validMoves(state):
	valid = []
	for i in range(3):
		if state[i] == []:
			continue
		for j in range(3):
			if state[i] != state[j]:
				# Check if j is empty. If yes, then insert [i,j].
				if len(state[j]) == 0:
					valid.append([i+1,j+1])
				# Else, check if disc in peg j is greater than disc in peg i. If yes, then insert.
				else:
					if state[j][0] > state[i][0]:
						valid.append([i+1,j+1])
	return valid

# ------------------
Q = {'a': 1, 'b': 2, 'c': 3}	
x = min(Q, key = Q.get)

def stateMoveTuple(state, move):
	stateTuple = tuple(tuple(x) for x in state)
	moveTuple = tuple(move)
	stateMoveTuple = (stateTuple, moveTuple)
	return stateMoveTuple

# ------------------

Q = { 
	  stateMoveTuple([[1,2,3],[],[]], [1,3]): 2,
	  stateMoveTuple([[1,2,3],[],[]], [1,2]): 1,
	  stateMoveTuple([[2,3], [1], []], [2,1]): 3 
	}

import random
# Epsilon Greedy
def epsilonGreedy(epsilon, Q, state):
    valid = validMoves(state)
    if np.random.uniform() < epsilon:
        # Random Move
        return random.choice(validMoves)
    else:
        # Greedy Move - get action for which the Q value is maximum.
        # Get Q values for all (state, move) pairs and store in a list.
        max = -float('inf')
        maxMove = [1,1]
        # Find the move for which the Q value is maxiumum.
        for move in valid:
        	smt = stateMoveTuple(state, move)
        	try:
        		Qval = Q[smt]
        	except KeyError:
        		continue
        	if Qval > max:
        		max = Qval
        		maxMove = move
        
        return maxMove

state = [[1,2,3],[],[]]
#print(epsilonGreedy(0, Q, state))
#print(validMoves(state))
#print(makeMove(state, [1,2]))

#l = [1,2,3]
l = [(1,2), (2,3)]
print(max(l, key=lambda x:x[0]))



