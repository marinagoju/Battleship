from utilsJugador import Jugador
from utilsGame import Game
from constants import barcos, barcosNum

name = input("\n\n- Capitán Sardino: Bienvenido a bordo grumete, ¿Cuál es tu nombre?:")
print(f'''
- Capitán Sardino: Muy bien {name}, a partir de ahora formarás parte de la flota de Caramarisal, arr.

Tu principal cometido aquí será guiarnos en el avistamiento de barcos enemigos para poder dispararles con la mayor precisión posible.

Pero antes de embarcarte hacia la batalla debes tener en cuenta las normas:

 · Se te solicitarán dos coordenadas para determinar la ubicación de disparo.
 · Tienes dos mapas donde podrás ver la posición de tus barcos, y las coordenadas de los disparos que ya lanzado.
 · Si el disparo ACIERTA aparecerá '-' en la ubicación.
 · Si el disparo NO ACIERTA aparecerá 'X' en la ubicación.
 · Las flotas tienen 10 barcos: 1 de 4 casillas, 2 de 3, 3 de 2 y 4 de 1 casilla. El primero que hunda los barcos del otro GANA.
 · Inserta el comando 'salir' si deseas abandonar la flota.
''')

maquina = Jugador(True, "MarIA")
jugador_grumete = Jugador(False, name)
hundir_la_flota = Game(maquina, jugador_grumete)

exit = input("- Capitán Sardino: ¿Entendido, grumete?:") # Oportunidad para salir con 'salir'/'no'
hundir_la_flota.SalirInicio(exit)


print("\n","Esa es la actitud!. Dicho esto, todos a sus puestos, ¡Arriad velas! !Alzad el ancla¡. La flota está a punto de zarpar...")


print("\n","* Generando tableros y desplegando la flota... *","\n")

jugador_grumete.initTablero() # Genera tablero del jugador
maquina.initTablero() # Genera tablero de la maquina
for i, v in barcosNum.items(): # Coloca barcos de ambos jugadores
    jugador_grumete.colocarBarcos(i,v)
    maquina.colocarBarcos(i,v)
    

hundir_la_flota.Jugar() # Ejecuta el Juego. Desarrollo más detallado en la clase Game.