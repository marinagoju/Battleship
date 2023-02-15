from utils import Jugador
from const import barcos, barcosNum


tamTablero = 10 # ambos tienen el mismo tamaöo de tablero
j1 = Jugador(False, tamTablero, "Aída\n")
ordena = Jugador(True, tamTablero, "PC\n")

j1.initTablero()
ordena.initTablero()
for i, v in barcosNum.items():    
    j1.colocarBarcos(i,v)
    ordena.colocarBarcos(i,v)

j1.mostrarTablero()
ordena.mostrarTablero()
