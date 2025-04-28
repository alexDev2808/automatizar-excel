# Tu tarea es escribir un simple programa que simule jugar a tic-tac-toe (nombre en inglés) con el usuario. Para hacerlo más fácil, hemos decidido simplificar el juego. Aquí están nuestras reglas:

#     la maquina (por ejemplo, el programa) jugará utilizando las 'X's;
#     el usuario (por ejemplo, tu) jugarás utilizando las 'O's;
#     el primer movimiento es de la maquina - siempre coloca una 'X' en el centro del tablero;
#     todos los cuadros están numerados comenzando con el 1 (observa el ejemplo para que tengas una referencia)
#     el usuario ingresa su movimiento introduciendo el número de cuadro elegido - el número debe de ser valido, por ejemplo un valor entero mayor que 0 y menor que 10, y no puede ser un cuadro que ya esté ocupado;
#     el programa verifica si el juego ha terminado - existen cuatro posibles veredictos: el juego continua, el juego termina en empate, tu ganas, o la maquina gana;
#     la maquina responde con su movimiento y se verifica el estado del juego;
#     no se debe implementar algún tipo de inteligencia artificial - la maquina elegirá un cuadro de manera aleatoria, eso es suficiente para este juego.


def display_board(board):
    # La función acepta un parámetro el cual contiene el estado actual del tablero
    # y lo muestra en la consola.
    for f in range(len(board)):
        print("\n+-------+-------+-------+")
        for c in range(len(board[f])):
            print("   ", board[f][c],end="   ")
        
        if f == len(board) - 1:
            print("\n+-------+-------+-------+")
    

def enter_move(board):
    # La función acepta el estado actual del tablero y pregunta al usuario acerca de su movimiento,  
    # verifica la entrada y actualiza el tablero acorde a la decisión del usuario.
    pass

def make_list_of_free_fields(board):
    # La función examina el tablero y construye una lista de todos los cuadros vacíos.
    # La lista esta compuesta por tuplas, cada tupla es un par de números que indican la fila y columna.
    pass

def victory_for(board, sign):
    # La función analiza el estatus del tablero para verificar si
    # el jugador que utiliza las 'O's o las 'X's ha ganado el juego.
    pass

def draw_move(board):
    # La función dibuja el movimiento de la máquina y actualiza el tablero.
    pass




#########################################################################################################################

# Crear tablero
tablero = []
coordenadas = []
celda = 1

for c in range(3):
    coordenada = []
    fila = []
    for f in range(3):
        coordenada.append((c,f))
        fila.append(celda)
        celda += 1
    coordenadas.append(coordenada) 
    tablero.append(fila)

entrada = int(input("Ingresa tu eleccion: "))

