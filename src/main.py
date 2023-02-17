from utils import Jugador
from Game import Game
from const import barcos, barcosNum

name = input("\n\n"" - Capitán Sardino: Bienvenido a bordo grumete, ¿Cuál es tu nombre?:")
print("\n",f"- Capitán Sardino: Muy bien {name}, a partir de ahora formarás parte de la flota de Caramarisal, arr.\n\nTu principal cometido aquí será guiarnos en el avistamiento de barcos enemigos para poder dispararles con la mayor precisión posible.\n")
print("""Antes de embarcarte hacia la batalla debes tener en cuenta las normas:

 - La batalla tiene lugar en un área de superficie 10x10.
 - Se te solicitarán dos coordenadas para determinar la ubicación de disparo.
 - Si el disparo ACIERTA aparecerá este simbolo en el mapa 'X'.
 - Si el disparo NO ACIERTA aparecerá '*'.
 - Las flotas constan de 4 barcos de 1 de eslora, 3 de 2 de eslora, 2 de 3 de eslora y 4 de 1 de eslora. El primero que hunda los barcos del otro GANA.
 - Inserta el comando 'salir' si deseas abandonar la flota.
""")

maquina = Jugador(True, "MarIA")
jugador_grumete = Jugador(False, name)
hundir_la_flota = Game(maquina, jugador_grumete)


input2 = input("- Capitán Sardino: ¿Entendido, grumete?:") # Oportunidad de salir
hundir_la_flota.salir(input2)


print("\n","Esa es la actitud!. Dicho esto, todos a sus puestos, ¡Arriad velas! !Alzad el ancla¡. La flota está a punto de zarpar...","\n")

hundir_la_flota.jugar() # Ejecuta el Juego. Desarrollo más detallado en la clase Game.

