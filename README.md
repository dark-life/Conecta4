#Conecta 4

###Heuristica.

Empezamos a hacer una heuristica totalmente aleatoria para la dificultad facil. De esta forma en caso de que el oponente se estrese con las otras dificultades puede jugar en facil y sentirse bien consigo mismo.

```python
def heuristicRT(state):
	return randint(-2500, 2500)
```
Para la dificultad normal, mejoramos la heuristica previa utilizando el utility. De esta forma, si la maquina puede ganar, gana y en caso de que el oponente pueda ganar, bloquea. Dentro de la aleatoriedad hace jugadas buenas y puede hacer pasar un mal momento al oponente.
```python
def heuristicRP(state):
	if state.utility == 1:
		return infinity
	if state.utility == -1:
		return -infinity
	return randint(-2500, 2500)
```
Para la ultima dificultad (dificil) ya empezamos a plantear una heuristica que escogiese el mejor estado posible. Haciendo la diferencia entre el coste de la maquina y el humano, podemos observar quien tiene la ventaja. En caso de que sea positivo, la maquina tendra ventaja y en caso contrario sera el humano quien la tenga.

```python
def heuristicN(state):
	if state.utility == 1:
		return infinity
	if state.utility == -1:
		return -infinity
	return coste(state, 'X') -  coste(state, 'O')
```

En esta funcion, llamamos a los metodos (modificados) del tic tac toe.

```python
def coste(state, player):
	"""If X wins with this move, return 1; if O return -1; else return 0"""
	cost = 0
	list_legalmoves = legal_moves(state)
	for move in list_legalmoves:
		cost += k_in_row(state.board, move, player, (0, 1)) #arriba
		cost += k_in_row(state.board, move, player, (1, 0)) #derecha
		cost += k_in_row(state.board, move, player, (1, 1)) #arriba-der
		cost += k_in_row(state.board, move, player, (1, -1)) #abajo-der
	return cost

```
Con esto obtenemos los posibles movimientos a realizar.
```python
def legal_moves(state):
        "Legal moves are any square not yet taken."
        return [(x, y) for (x, y) in state.moves
                if y == 1 or (x, y-1) in state.board]
```
Aqui miramos en horizontal, vertical y posibles diagonales. En caso de encontrar una ficha nuestra sumamos 100 al valor a devolver y tambien aumentamos en 1 una variable que nos dice cuantas fichas tenemos alineadas para asi saber los posible cuatro en raya que tenemos. Damos prioridad al bloqueo de nuestro adversario humano.
```python
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
```

###Dificultades.
Aqui escogemos las dificultades .
```python
def selectDifficulty(state, game):
    print "Seleccione dificultad: "
    print "1. Facil   ||   2. Medio   ||   3. Dificil"
    dificultad = raw_input("Dificultad: ")
    if dificultad == '1':
        return heu.heuristicRT
    else:
        if dificultad == '2':
            return heu.heuristicRP
        else:
            return heu.heuristicN
```
Seleccionamos el jugador que jugara primero. 

```python
def selectPlayer():
    print "Seleccione el jugador que va primero: "
    print "1. Maquina   ||   2. Humano"
    player = raw_input("Jugador: ")
    if player == '1':
        return 'X'
    else:
        return 'O'

```
Modificamos el constructor del conecta 4 para asi pasarle el jugador escogido. Poniendo como valor por defecto a la maquina.
``` python
"""Conecta 4"""
def __init__(self, h=7, v=6, k=4, player='X'):
        TicTacToe.__init__(self, h, v, k, player)
"""Tic Tac Toe"""
def __init__(self, h=3, v=3, k=3, player='X'):
        update(self, h=h, v=v, k=k)
        moves = [(x, y) for x in range(1, h+1)
                 for y in range(1, v+1)]
        self.initial = Struct(to_move=player, utility=0, board={}, moves=moves)
```
```python
def humanVsMachine():
    player = selectPlayer()
    game = games.ConnectFour(h=7, v=6, k=4, player=player)
    state = game.initial
    heu = selectDifficulty(state, game)
    while True:
        print "Jugador a mover:", game.to_move(state)
        game.display(state)

        if player == 'O':
            x = checkValidMove()
            y = -1
            legal_moves = game.legal_moves(state)
            for lm in legal_moves:
                if lm[0] == x:
                    y = lm[1]
            state = game.make_move((x, y), state)
            player = 'X'
        else:
            print "Thinking..."
            move = games.alphabeta_search(state, game, d=5, cutoff_test=None, eval_fn=heu)
            state = game.make_move(move, state)
            player = 'O'
        print "-------------------"
        if game.terminal_test(state):
            game.display(state)
            print "Final de la partida"
            break        
```
