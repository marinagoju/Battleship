from utils import Jugador
from const import barcos, barcosNum
import numpy as np

class Game: 
    turno = True # si es true el turno es del jugador, si no de la máquina
    fin = False

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
        while not self.fin:
            if self.turno: 
                #logica para el jugador
                #preguntar coordenadas
                #disparar
                #mostrar feedback
                #si tocado repetir turno - fin de partida
                #si agua turno = false
                print("es tu turno", self.grumete.nombre)
                x = input("elige fila")
                y = input("elige columna")

                res = self.grumete.getDisparo(x,y)     
                if res == "-":#si es agua
                    jugamos = False
                    self.turno = False
                elif res == "fin de juego":
                    jugamos = False
                    fin = True
                else:
                    self.turno = True

                
            else:
                #logica para la maquina
                #generar coordenadas aleatoriiamente sin repetir (si no hay nada en el tablero de impactos)
                jugamos = True
                while jugamos:
                    x = np.random.randint(10)
                    y = np.random.randint(10)
                    while self.maquina.tablero_impactos[x,y] != " ":
                        x = np.random.randint(10)
                        y = np.random.randint(10)
                    #disparar
                    #mostrar feedback
                    
                    res = self.maquina.getDisparo(x,y)     
                    if res == "-":#si es agua
                        jugamos = False
                        self.turno = True
                    elif res == "fin de juego":
                        jugamos = False
                        fin = True
                    else:
                        self.turno = True
                    
                    #si tocado repetir turno - fin de partida
                    #si agua turno = false
                    print("disparo a ", x,y, self.grumete.getDisparo(x,y))

                

       