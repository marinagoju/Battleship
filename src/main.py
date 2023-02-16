from utils import Jugador
from Game import Game
from const import barcos, barcosNum

name = input("-Capitán Sardino: Bienvenido a bordo grumete, ¿Cuál es tu nombre?:")
print(f"-Capitán Sardino: Muy bien {name}, a partir de ahora formarás parte de la flota de Caramarisal, arr.\n\n Tu principal cometido aquí será guiarnos en el avistamiento de barcos enemigos para poder dispararles con la mayor precisión posible.\n")
print(" Antes de embarcarte hacia la batalla debes tener en cuenta que:\n - La batalla tiene lugar en un área de superficie 10x10.\n - Se te solicitarán dos coordenadas del 0 al 9 para determinar la ubicación del disparo. \n - Si el disparo acierta aparecerá este simbolo en el mapa 'X'.\n - Si el disparo no acierta aparecerá '*'.\n - Inserta el comando 'salir' si deseas abandonar la flota.\n\n Dicho esto, todos a sus puestos, ¡Arriad velas! !Alzad el ancla¡. La flota está a punto de zarpar...")


maquina = Jugador(True, "MarIA")
grumete = Jugador(False, name)
hundir_la_flota = Game(maquina, grumete)

hundir_la_flota.jugar() # Reinicia mapas/tableros y coloca los barcos
