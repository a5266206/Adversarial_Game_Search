import copy

def getValidMove(p, x, y, state):
	m = []
	left = 0
	if p == "Star":
		if x == 0:
			return m
		if x == 1 and y != 0 and state[x-1][y-1][0] != 'C':
			m.append([x-1,y-1])
		if x == 1 and state[x-1][y+1][0] != 'C':
			m.append([x-1,y+1])
		if x == 2 and state[x-1][y-1] == '0':
			m.append([x-1,y-1])
			left = 1
		elif x == 2 and y-2 >= 0 and state[x-1][y-1][0] == 'C' and state[x-2][y-2][0] != 'C':
			m.append([x-2,y-2])
		if x == 2 and y < 7 and state[x-1][y+1] == '0':
			m.append([x-1,y+1])
		elif x == 2 and y+2 <= 7 and state[x-1][y+1] == 'C' and state[x-2][y+2][0] != 'C' and left != 1:
			m.append([x-2,y+2])
		elif x == 2 and y+2 <= 7 and state[x-1][y+1] == 'C' and state[x-2][y+2][0] != 'C' and left == 1:
			m.pop()
			m.append([x-2,y+2])
			m.append([x-1,y-1])
		if x > 2 and y-1 >= 0 and state[x-1][y-1] == '0':
			m.append([x-1,y-1])
			left = 1
		elif x > 2 and y-2 >= 0 and state[x-1][y-1][0] == 'C' and state[x-2][y-2] == '0':
			m.append([x-2,y-2]) 
		if x > 2 and y+1 <= 7 and state[x-1][y+1] == '0':
			m.append([x-1,y+1])
		elif x > 2 and y+2 <= 7 and state[x-1][y+1][0] == 'C' and state[x-2][y+2] == '0' and left != 1:
			m.append([x-2,y+2])
		elif x > 2 and y+2 <= 7 and state[x-1][y+1][0] == 'C' and state[x-2][y+2] == '0' and left == 1:
			m.pop()
			m.append([x-2,y+2])
			m.append([x-1,y-1])	
	elif p == "Circle":
		if x == 7:
			return m
		if x == 6 and state[x+1][y-1][0] != 'S':
			m.append([x+1,y-1])
		if x == 6 and y != 7 and state[x+1][y+1][0] != 'S':
			m.append([x+1,y+1])
		if x == 5 and y != 0 and state[x+1][y-1] == '0':
			m.append([x+1,y-1])
		elif x == 5 and y-2 >= 0 and state[x+1][y-1][0] == 'S' and state[x+2][y-2][0] != 'S':
			m.append([x+2,y-2])
			left = 1
		if x == 5 and state[x+1][y+1] == '0' and left != 1:
			m.append([x+1,y+1])
		elif x == 5 and state[x+1][y+1] == '0' and left == 1:
			m.pop()
			m.append([x+1,y+1])
			m.append([x+2,y-2])	
		elif x == 5 and y+2 <= 7 and state[x+1][y+1] == 'S' and state[x+2][y+2][0] != 'S':
			m.append([x+2,y+2])
		if x < 5 and y-1 >= 0 and state[x+1][y-1] == '0':
			m.append([x+1,y-1])
		elif x < 5 and y-2 >= 0 and state[x+1][y-1][0] == 'S' and state[x+2][y-2] == '0':
			m.append([x+2,y-2])
			left = 1 
		if x < 5 and y+1 <= 7 and state[x+1][y+1] == '0' and left != 1:
			m.append([x+1,y+1])
		elif x < 5 and y+1 <= 7 and state[x+1][y+1] == '0' and left == 1:
			m.pop()
			m.append([x+1,y+1])
			m.append([x+2,y-2])
		elif x < 5 and y+2 <= 7 and state[x+1][y+1][0] == 'S' and state[x+2][y+2] == '0':
			m.append([x+2,y+2])
	return m

def getAllValidMove(state, player):
	legalMove = []
	initPosition = []
	finalPosition = []
	for i in range(0,8):
		for j in range(0,8):
			if state[i][j][0] == player[0]:
				initPosition.append([i,j])
	for i in range(0, len(initPosition)):
		finalPosition.append(getValidMove(player, initPosition[i][0], initPosition[i][1], state))
		temp = []
		if(len(finalPosition[i]) != 0):
			for j in range(0, len(finalPosition[i])):
				temp.append(initPosition[i])
				temp.append(finalPosition[i][j])
				legalMove.append(temp)
				temp = []
	return legalMove

def getNextState(state, move, player):
	nextState = copy.deepcopy(state)
	nextState[move[0][0]][move[0][1]] = '0'
	if nextState[move[1][0]][move[1][1]] == '0':
		nextState[move[1][0]][move[1][1]] = player[0] + '1'
	else:
		nextState[move[1][0]][move[1][1]] = player[0] + str(int(nextState[move[1][0]][move[1][1]][1])+1)
	if abs(move[1][0] - move[0][0]) > 1:
		x = (move[0][0] + move[1][0])/2
		y = (move[0][1] + move[1][1])/2
		nextState[x][y] = '0'
	return nextState

def isTerminal(state, numPass, depth):
	numS = 0
	numC = 0
	for i in range(0,8):
		for j in range(0,8):
			if state[i][j][0] == 'S':
				numS = numS + 1
			elif state[i][j][0] == 'C':
				numC = numC + 1
	if numPass == 2:
		return True
	elif depth == 0:
		return True
	elif numS == 0 or numC == 0:
		return True
	else:
		return False

def getUtility(state, player, weight):
	utility = 0
	if player == "Star":
		opp = 'C'
		for i in range(0,8):
			for j in range(0,8):
				if state[i][j][0] == player[0]:
					utility = utility + int(state[i][j][1])*weight[7-i]
				elif state[i][j][0] == opp:
					utility = utility - int(state[i][j][1])*weight[i]
	elif player == "Circle":
		opp = 'S'
		for i in range(0,8):
			for j in range(0,8):
				if state[i][j][0] == player[0]:
					utility = utility + int(state[i][j][1])*weight[i]
				elif state[i][j][0] == opp:
					utility = utility - int(state[i][j][1])*weight[7-i]
	return utility

def printPosition(move):
	if move[0] == 0:
		po = "H"
	elif move[0] == 1:
		po = "G"
	elif move[0] == 2:
		po = "F"
	elif move[0] == 3:
		po = "E"
	elif move[0] == 4:
		po = "D"
	elif move[0] == 5:
		po = "C"
	elif move[0] == 6:
		po = "B"
	elif move[0] == 7:
		po = "A"
	po = po + str(move[1]+1)
	return po

numNodes = []
def minPlay(state, player, opponent, depth, weight, numPass, numNodes, firstDepth):
	numNodes.append([0])
	if isTerminal(state, numPass, depth):
		return getUtility(state, player, weight)
	minValue = float('inf')
	nextMoves = getAllValidMove(state, opponent)
	if len(nextMoves) == 0:
		numPass = numPass + 1
		depth = depth -1
		minValue = min(minValue, maxPlay(state, player, opponent, depth, weight, numPass, numNodes, firstDepth))
	else:
		numPass = 0
		depth = depth - 1
	for s in range(0, len(nextMoves)):
		childState = getNextState(state, nextMoves[s], opponent)
		minValue = min(minValue, maxPlay(childState, player, opponent, depth, weight, numPass, numNodes, firstDepth))
	return minValue

maxNextMove = []
def maxPlay(state, player, opponent, depth, weight, numPass, numNodes, firstDepth):
	numNodes.append([0])
	if isTerminal(state, numPass, depth):
		return getUtility(state, player, weight)
	maxValue = float('-inf')
	nextMoves = getAllValidMove(state, player)
	if len(nextMoves) == 0:
		numPass = numPass + 1
		depth = depth - 1
		minNodeValue = minPlay(state, player, opponent, depth, weight, numPass, numNodes, firstDepth)
		maxValue = max(maxValue, minNodeValue)
	else:
		numPass = 0
		depth = depth - 1
	for s in range(0, len(nextMoves)):
		childState = getNextState(state, nextMoves[s], player)
		minNodeValue = minPlay(childState, player, opponent, depth, weight, numPass, numNodes, firstDepth)
		if depth == firstDepth and minNodeValue > maxValue:
			maxNextMove.append(nextMoves[s])
		maxValue = max(maxValue, minNodeValue)
	return maxValue

def minimaxSearch(p, depth, state, rowVal):
	firstDepth = depth - 1
	if p == "Star":
		op = "Circle"
	elif p == "Circle":
		op = "Star"
	farsighted_Utilty = maxPlay(state, p, op, depth, rowVal, 0, numNodes, firstDepth)
	if len(maxNextMove) == 0:
		nextState = state
	else:
		nextState = getNextState(state, maxNextMove[len(maxNextMove)-1], p)
	myopic_Utility = getUtility(nextState, p, rowVal)
	return maxNextMove, myopic_Utility, farsighted_Utilty, len(numNodes)

def maxNode(state, player, opponent, depth, weight, numPass, numNodes, alpha, beta):
	numNodes.append([0])
	if isTerminal(state, numPass, depth):
		return getUtility(state, player, weight)
	maxValue = float('-inf')
	nextMoves = getAllValidMove(state, player)
	if len(nextMoves) == 0:
		numPass = numPass + 1
		depth = depth - 1
		minNodeValue = minNode(state, player, opponent, depth, weight, numPass, numNodes, alpha, beta)
		maxValue = max(maxValue, minNodeValue)
		if maxValue >= beta:
			return maxValue
		alpha = max(alpha, maxValue)
	else:
		numPass = 0
		depth = depth - 1
	for s in range(0, len(nextMoves)):
		childState = getNextState(state, nextMoves[s], player)
		minNodeValue = minNode(childState, player, opponent, depth, weight, numPass, numNodes, alpha, beta)
		maxValue = max(maxValue, minNodeValue)
		if maxValue >= beta:
			return maxValue
		alpha = max(alpha, maxValue)
	return maxValue

def minNode(state, player, opponent, depth, weight, numPass, numNodes, alpha, beta):
	numNodes.append([0])
	if isTerminal(state, numPass, depth):
		return getUtility(state, player, weight)
	minValue = float('inf')
	nextMoves = getAllValidMove(state, opponent)
	if len(nextMoves) == 0:
		numPass = numPass + 1
		depth = depth -1
		minValue = min(minValue, maxNode(state, player, opponent, depth, weight, numPass, numNodes, alpha, beta))
		if minValue <= alpha:
			return minValue
		beta = min(beta, minValue)
	else:
		numPass = 0
		depth = depth - 1
	for s in range(0, len(nextMoves)):
		childState = getNextState(state, nextMoves[s], opponent)
		minValue = min(minValue, maxNode(childState, player, opponent, depth, weight, numPass, numNodes, alpha, beta))
		if minValue <= alpha:
			return minValue
		beta = min(beta, minValue)
	return minValue

def alphabetaSearch(p, depth, state, rowVal):
	alpha = float('-inf')
	beta = float('inf')
	maxUtility = float('-inf')
	depth = depth - 1
	numPass = 0
	if p == "Star":
		op = "Circle"
	elif p == "Circle":
		op = "Star"
	nextMoves = getAllValidMove(state, p)
	if len(nextMoves) == 0:
		numPass = numPass + 1
		nextMoves.append([-1,-1])
	nextMoveState = []
	nextMove = []
	for m in nextMoves:
		if m == [-1,-1]:
			childState = state
		else:
			childState = getNextState(state, m, p)
		utility = minNode(childState, p, op, depth, rowVal, numPass, numNodes, alpha, beta)
		if utility > maxUtility:
			maxUtility = utility
			alpha = maxUtility
			nextMove.append(m)
	if nextMove == [[-1,-1]]:
		nextState = state
		nextMove = []
	else:
		nextState = getNextState(state, nextMove[0], p)
	myopic_Utility = getUtility(nextState, p, rowVal)
	return nextMove, myopic_Utility, maxUtility, len(numNodes)+1

def main():
	f = open("input.txt", "r")
	content = f.read().splitlines()
	f.close()
	player = content[0]
	algorithm = content[1]
	depthLimit = int(content[2])
	initState = []
	for x in range(3,11):
		inputRow = content[x]
		curRow = []
		head = 0
		for y in range(0,len(content[x])):
			if content[x][y] == ',':
				curRow.append(content[x][head:y])
				head = y+1
		curRow.append(content[x][head:])
		initState.append(curRow)
	rowValue = []
	h = 0
	for i in range(0,len(content[11])):
		if content[11][i] == ',':
			rowValue.append(int(content[11][h:i]))
			h = i+1
	rowValue.append(int(content[11][h:]))
	output = []
	if algorithm == "MINIMAX":
		output = minimaxSearch(player, depthLimit, initState, rowValue)
	elif algorithm == "ALPHABETA":
		output = alphabetaSearch(player, depthLimit, initState, rowValue)
	if len(output[0]) == 0:
		next_move = "pass"
	else:
		next_move = printPosition(output[0][len(maxNextMove)-1][0])
		next_move = next_move + "-" + printPosition(output[0][len(maxNextMove)-1][1])
	f = open("output.txt", "w")
	f.write(next_move+"\n")
	f.write(str(output[1])+"\n")
	f.write(str(output[2])+"\n")
	f.write(str(output[3]))
	f.close()

main()
