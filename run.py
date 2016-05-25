import games
import heu

def main():
    print "Que desea hacer?"
    print "1. Humano vs Humano.   ||   2. Humano vs IA.   ||   3. IA vs IA."
    option = raw_input("Opcion: ")
    if option == '1':
        humanVsHuman()
    else:
        if option == '2':
            humanVsMachine()
        else:
            print machineVsMachine()

def selectPlayer():
    print "Seleccione el jugador que va primero: "
    print "1. Maquina   ||   2. Humano"
    player = raw_input("Jugador: ")
    if player == '1':
        return 'X'
    else:
        return 'O'

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

def humanVsHuman():
    player = selectPlayer()
    game = games.ConnectFour(h=7, v=6, k=4, player=player)
    state = game.initial
    while True:
        print "Jugador a mover:", game.to_move(state)
        game.display(state)
        if player == 'O':
            col_str = raw_input("Movimiento: ")
            coor = int(str(col_str).strip())
            x = coor
            y = -1
            legal_moves = game.legal_moves(state)
            for lm in legal_moves:
                if lm[0] == x:
                    y = lm[1]
            state = game.make_move((x, y), state)
            player = 'X'
        else:
            col_str = raw_input("Movimiento: ")
            coor = int(str(col_str).strip())
            x = coor
            y = -1
            legal_moves = game.legal_moves(state)
            for lm in legal_moves:
                if lm[0] == x:
                    y = lm[1]
            state = game.make_move((x, y), state)
            player = 'O'
        print "-------------------"
        if game.terminal_test(state):
            game.display(state)
            print "Final de la partida"
            break

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

def machineVsMachine():
    game = games.ConnectFour(h=7, v=6, k=4)
    state = game.initial
    player = 'X'
    while True:
        print "Jugador a mover:", game.to_move(state)
        game.display(state)

        if player == 'O':
            print "Don't Think, Just ACT"
            move = games.alphabeta_search(state, game, d=2, cutoff_test=None, eval_fn=heu.heuristicRIA)
            state = game.make_move(move, state)
            player = 'X'
        else:
            print "Thinking..."
            move = games.alphabeta_search(state, game, d=3, cutoff_test=None, eval_fn=heu.heuristicN)
            state = game.make_move(move, state)
            player = 'O'
        print "-------------------"
        if game.terminal_test(state):
            game.display(state)
            print "Final de la partida"
            break
    

def checkValidMove():
    col_str = raw_input("Movimiento: ")
    coor = int(str(col_str).strip())
    while coor < 1 or coor > 7:
        col_str = raw_input("Movimiento incorrecto, intentelo de nuevo: ")
        coor = int(str(col_str).strip())
    return coor

if __name__ == '__main__':
    main()