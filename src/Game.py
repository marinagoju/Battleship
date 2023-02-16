from utils import Jugador
from const import barcos, barcosNum

class Game: 
    turno = True # si es true el turno es del jugador, si no de la máquina

    def __init__(self, jugador: Jugador, maquina: Jugador): # Tipo el argumento para que quede fijo
        self.jugador = jugador  
        self.maquina = maquina 

    def jugar (self):
        tamTablero = 10 # ambos tienen el mismo tamaöo de tablero
        print("Generando tableros y desplegando la flota...")

        self.jugador.initTablero()
        self.maquina.initTablero()
        for i, v in barcosNum.items():    
            self.jugador.colocarBarcos(i,v)
            self.maquina.colocarBarcos(i,v)

        self.jugador.mostrarTablero()
        
        #disparar a j1
        #feedback =  self.grumete.getDisparo()

        if self.turno: 
            #logica para el jugador
            #preguntar coordenadas
            #disparar
            #mostrar feedback
            #si tocado repetir turno - fin de partida
            #si agua turno = false
            print("es tu turno", self.jugador.nombre)
        else:
            #logica para la maquina
            #generar coordenadas aleatoriiamente sin repetir
            #disparar
            #mostrar feedback
            #si tocado repetir turno - fin de partida
            #si agua turno = false


            

        print("disparo a ", "B",2, self.jugador.getDisparo("B",2))