# Function to represent the state (of the pegs)
# state = [[1,2,3], [2,3,4], []]
from copy import deepcopy
def printState(state):
	statenew = deepcopy(state)
	for i in statenew:
		if len(i) == 0:
			i.insert(0, ' ')
			i.insert(0, ' ')
			i.insert(0, ' ')
		elif len(i) == 1:
			i.insert(0, ' ')
			i.insert(0, ' ')
		elif len(i) == 2:
			i.insert(0, ' ')

	for i in list(zip(*statenew)):
		for j in i:
			print(j, end=' ')
		print()
	print('-----')
# Function which returns valid moves from a state
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

# Function to apply a move to a state and return the new state.
def makeMove(state, move):
	if move != None:
		state2 = deepcopy(state)
		# Get the pegs from and to which the moves are to be done.
		source = move[0]
		dest = move[1]
		# Get the disk from source
		disk = state2[source - 1][0]
		# Remove from source
		state2[source-1].remove(disk)
		# Move disk to destination
		state2[dest - 1].insert(0, disk)
		return state2

# Function to check if the goal state has been reached.
def isGoalState(state):
	if state == [[], [], [1,2,3]]:
		return True
	else:
		return False

# Function which converts lists to tuples.
def stateMoveTuple(state, move):
	stateTuple = tuple(tuple(x) for x in state)
	moveTuple = tuple(move)
	stateMoveTuple = (stateTuple, moveTuple)
	return stateMoveTuple

import pprint
import random
# Epsilon Greedy
def epsilonGreedy(epsilon, Q, state):
    valid = validMoves(state)
    qlist = []
    if np.random.uniform() < epsilon:
        # Random Move
        return random.choice(valid)
    else:
        # Greedy Move - get action for which the Q value is maximum.
        # Get Q values for all (state, move) pairs and store in a list.
        for move in valid:
        	smt = stateMoveTuple(state, move)
        	Qval = Q.get(smt, -1)
        	qlist.append((Qval, move))
        maxMove = max(qlist, key=lambda x:x[0])
        return maxMove[1]

import numpy as np

# Function for training Q for Towers of Hanoi.
def trainQ(nRepetitions, learningRate, epsilonDecayFactor, validMovesF, makeMoveF):
	epsilon = 1.0
	Q = {}
	stepsToGoal = []
	for nGames in range(nRepetitions):
	    print("we're at rep: ", nGames)
	    # Decay epsilon
	    epsilon *= epsilonDecayFactor

	    # Start state for ToH
	    s = [[1,2,3], [], []]

	    # Play a game till solution occurs for ToH.
	    done = False
	    step = 0
	    while not done:        
	        step += 1
	        

	        # Choose a move.
	        move = epsilonGreedy(epsilon, Q, s)

	       
	        # Apply the move on a copy of state.
	        sNew = deepcopy(s)
	        sNew = makeMoveF(sNew, move)

	        if stateMoveTuple(s, move) not in Q:
	            Q[stateMoveTuple(s, move)] = -1  # initial Q value for new board,move

            # If the goal state is reached, then update Q(s, move) += rho*(0 - Q(s, move)) and break game (inner loop).
	            
	        if isGoalState(sNew):
	            Q[stateMoveTuple(s, move)] += learningRate * (0 - Q[stateMoveTuple(s, move)])
	            done = True
	            
	        else:
	            if step > 1:
	                Q[stateMoveTuple(sOld,moveOld)] += learningRate * (-1 + Q[stateMoveTuple(s,move)] - Q[stateMoveTuple(sOld,moveOld)])
	            sOld, moveOld = s, move # remember board and move to Q(board,move) can be updated after next steps
	            s = sNew
	    stepsToGoal.append(step)

	return Q, stepsToGoal


if __name__ == '__main__':

    nRepetitions = 50
    learningRate = 0.5
    epsilonDecayFactor = 0.7
    Q, stepsToGoal = trainQ(nRepetitions, learningRate, epsilonDecayFactor, validMoves, makeMove)
    print(stepsToGoal)
    #print(validMoves([[], [1,2], [3]]))
    #print(epsilonGreedy(0, ))