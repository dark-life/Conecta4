#Conecta 4

###Heuristica.

Empezamos a hacer una heuristica totalmente aleatoria para la dificultad facil. De esta forma en caso de que el oponente se estrese con las otras dificultades puede jugar en facil y sentirse bien consigo mismo.

```python
def heuristicRT(state):
	return randint(-2500, 2500)
```
Para la dificultad normal, mejoramos la heuristica previa utilizando el utility. De esta forma, si la maquina puede ganar, gana y en caso de que el oponente pueda ganar, bloquea. Dentro de la aleatoriedad hace jugadas buenas y puede estresar al oponente.
```python
def heuristicRP(state):
	if state.utility == 1:
		return infinity
	if state.utility == -1:
		return -infinity
	return randint(-2500, 2500)
```


```python
def heuristicRT(state):
	return randint(-2500, 2500)
```

coste

```python
def heuristicRT(state):
	return randint(-2500, 2500)
```

legal
```python
def heuristicRT(state):
	return randint(-2500, 2500)
```

k in a row

```python
def heuristicRT(state):
	return randint(-2500, 2500)
```

