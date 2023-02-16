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
#disparar a j1
#feedback = j1.getDisparo()

    

print("disparo a ", "B",2, j1.getDisparo("B",2))
print("disparo a ", "C",1, j1.getDisparo("C",1))
print("disparo a ", "D",2, j1.getDisparo("D",2))
print("disparo a ", "F",3, j1.getDisparo("F",3))
print("disparo a ", "G",4, j1.getDisparo("G",4))
print("disparo a ", "H",5, j1.getDisparo("H",5))
