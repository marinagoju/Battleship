import numpy as np
from const import coord

class Barco:    
    
      
    def __init__(self, size, inicio, orientacion):
        self.size = size
        self.inico = inicio
        self.orientacion = orientacion
        for i in range(self.size):
            self.barco[i] = self.size
 
    def getDisparo(self, x, y):
        res = ""
        #la X puede ser una letra de la A a la J, lo contemplamos tambien
        if isinstance(x,str):
            x = self.getIndiceLetra(x)
       
        #TODO confiamos en que el jugador no dispara de nuevo en una casilla
        
        if self.tablero[x,y] == "O" or self.tablero[x,y].isdigit():
            if self.todosHundidos():
                res =  "fin de juego"
            elif self.barcoTocado(x,y):
                res =  "X"
            elif self.barcoHundido(x,y):
                res = "XX"
         
        else:
            res =  "-"
        
        self.setDisparo( x, y, res)
        return res 

    def setDisparo(self, x, y, res):
        self.tablero_impactos[x,y] = res
        self.mostrarTablero()
        self.mostrarImpactos()
