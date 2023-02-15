from utils import Jugador
from const import barcos
#class Game ?? : 



tamTablero = 10 # ambos tienen el mismo tamaöo de tablero
j1 = Jugador(False, tamTablero, "Aída")
ordena = Jugador(True, tamTablero, "PC")

j1.initTablero()
ordena.initTablero()
for i, v in barcos.items():
    print(i,v)
    j1.colocarBarcos(i,v)
    ordena.colocarBarcos(i,v)

j1.mostrarTablero()
ordena.mostrarTablero()
