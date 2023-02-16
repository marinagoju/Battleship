from utils import Jugador
from const import barcos, barcosNum

class Game: 
    turno = True # si es true el turno es del jugador, si no de la máquina

    def __init__(self, maquina, grumete):        
        self.maquina = maquina
        self.grumete = grumete

    def jugar (self):
        tamTablero = 10 # ambos tienen el mismo tamaöo de tablero

        self.grumete.initTablero()
        self.maquina.initTablero()
        for i, v in barcosNum.items():    
            self.grumete.colocarBarcos(i,v)
            self.maquina.colocarBarcos(i,v)

        self.grumete.mostrarTablero()
        self.maquina.mostrarTablero()
        #disparar a j1
        #feedback =  self.grumete.getDisparo()

        if self.turno: 
            #logica para el jugador
            #preguntar coordenadas
            #disparar
            #mostrar feedback
            #si tocado repetir turno - fin de partida
            #si agua turno = false
            print("es tu turno", self.grumete.nombre)
        else:
            #logica para la maquina
            #generar coordenadas aleatoriiamente sin repetir
            #disparar
            #mostrar feedback
            #si tocado repetir turno - fin de partida
            #si agua turno = false


            

        print("disparo a ", "B",2, self.grumete.getDisparo("B",2))