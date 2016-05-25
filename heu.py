from random import randint
from utils import *
import random 

#aleatoria
def heuristicRP(state):
	if state.utility == 1:
		return infinity
	if state.utility == -1:
		return -infinity

	return randint(-2500, 2500)

def heuristicRT(state):
	return randint(-2500, 2500)

def heuristicRIA(state):
	if state.utility == 1:
		return -infinity
	if state.utility == -1:
		return infinity

	return randint(-2500, 2500)

def heuristicN(state):
	if state.utility == 1:
		return infinity
	if state.utility == -1:
		return -infinity
	return coste(state, 'X') -  coste(state, 'O')

def coste(state, player):
	cost = 0
	list_legalmoves = legal_moves(state)
	for move in list_legalmoves:
		cost += k_in_row(state.board, move, player, (0, 1)) #arriba
		cost += k_in_row(state.board, move, player, (1, 0)) #derecha
		cost += k_in_row(state.board, move, player, (1, 1)) #arriba-der
		cost += k_in_row(state.board, move, player, (1, -1)) #abajo-der
	return cost

def legal_moves(state):
        "Legal moves are any square not yet taken."
        return [(x, y) for (x, y) in state.moves
                if y == 1 or (x, y-1) in state.board]

def k_in_row(board, move, player, (delta_x, delta_y)):
	x, y = move
	n = 0
	ac = 0
	while (board.get((x, y)) == player) or (board.get((x, y))  == None)  and x < 8 and y < 7:
		if board.get((x, y))  == None:
			n += 50
		if board.get((x, y))  == player:
			n += 100
			ac += 1
		x, y = x + delta_x, y + delta_y
	x, y = move
	while (board.get((x, y)) == player) or (board.get((x, y))  == None) and x > 0 and y > 0:
		if board.get((x, y))  == None:
			n += 50
		if board.get((x, y))  == player:
			n += 100
			ac += 1
		x, y = x - delta_x, y - delta_y
	if ac == 3:
		if player == 'X':
			n *= 6
		else:
			n *= 12
	if ac >= 4:
		if player == 'X':
			n *= 9
		else:
			n *= 18
	return n
