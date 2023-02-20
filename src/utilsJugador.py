import numpy as np
from constants import coord, barcos, lenTablero

class Jugador:
    tablero = []
    tablero_impactos = []   
    tablero_barcos = [] # tablero para comprobar si un barco está hundido, no se visualiza
    lenTablero = 10
      
    def __init__(self, is_maquina, nombre):  # maquina -> bool   
        self.is_maquina = is_maquina
        self.nombre = nombre
       
    
        
    def initTablero(self):        
        self.tablero = np.full((lenTablero,lenTablero), " ")
        self.tablero_impactos = np.full((lenTablero,lenTablero), " ")
        self.tablero_barcos = np.full((10,10),0)     

    def colocarBarcos(self, tamBarco, num):
        print("colocando", num , "barcos de ", tamBarco, "\n")

        def checkColision(tamBarco, x,y, orientacion):
            t = tamBarco 
            colision = False
            c1 = x
            c2 = y
            
            while t:                            
                if((self.tablero[c1+coord[orientacion][0]-1, c2+coord[orientacion][1]-1]!= " ") and #casilla libre
                #TODO bug casilla libre Left Right Up Down D1 D2 D3 D4 a lo largo del nuevo barco               
                   # (((c1+coord[orientacion][0]-2 > -1) and (self.tablero[c1+coord[orientacion][0]-2, c2+coord[orientacion][1]-2]!= " ")) or ((c1+coord[orientacion][0]-1) == 0))and#D1 U-D
                   # (((c1+coord[orientacion][0]-2 > -1) and (self.tablero[c1+coord[orientacion][0]-2, c2+coord[orientacion][1]]!= " ")) or ((c1+coord[orientacion][0]-1) == 0))and#D2 U-I
                   # (((c1+coord[orientacion][0]-2 > -1) and (self.tablero[c1+coord[orientacion][0]+2, c2+coord[orientacion][1]]!= " ")) or ((c1+coord[orientacion][0]-1) == 0))and#D3 D-I
                   # (((c1+coord[orientacion][0]-2 > -1) and (self.tablero[c1+coord[orientacion][0]+2, c2+coord[orientacion][1]+2]!= " ")) or ((c1+coord[orientacion][0]-1) == 0))and#D4 D-D
                    (((c1+coord[orientacion][0]-2 > -1) and (self.tablero[c1+coord[orientacion][0]-2, c2+coord[orientacion][1]-1]!= " ")) or ((c1+coord[orientacion][0]-1) == 0))and#Up
                    (((c1+coord[orientacion][0]+2 < lenTablero) and (self.tablero[c1+coord[orientacion][0]+2, c2+coord[orientacion][1]-1]!= " " ) or ((c1+coord[orientacion][1]-1) < lenTablero)))and#Down
                    (((c1+coord[orientacion][1]-2 > -1) and (self.tablero[c1+coord[orientacion][0], c2+coord[orientacion][1]-2]!= " ")) or (c1+coord[orientacion][1]-1) == 0)and#Left
                    (((c1+coord[orientacion][1] < lenTablero) and (self.tablero[c1+coord[orientacion][0], c2+coord[orientacion][1]]!= " ")) or (c1+coord[orientacion][1]) == lenTablero)):#Right
                        colision = True
                        break
                else:
                    c1 += coord[orientacion][0]
                    c2 += coord[orientacion][1]
                if colision: 
                    break
                else:
                    t-=1           
           
                #print("checkColision ", c1, c2, orientacion, colision)
                #print(self.tablero)
               
            return colision
            
        #posicion inicial
        tam = tamBarco 
        
        while(num):
            aOrientacion = ["N","S","E","O"]        
            num -=1
            initPosition = False
            while not initPosition:
                x = np.random.randint(lenTablero)
                y = np.random.randint(lenTablero)
              
                if ((self.tablero[x,y] == " ") and
                   ((((x+1 < lenTablero) and (self.tablero[x+1,y] == " ")) or (x+1 == lenTablero))) and
                   (((x-1 > -1) and (self.tablero[x-1,y] == " ") or (x == 0))) and
                   (((y+1 < lenTablero) and (self.tablero[x,y+1] == " ")) or (y + 1 == lenTablero))):# and
                   #(((y+1 < lenTablero) and (x+1 < lenTablero) and (self.tablero[x+1,y+1] == " ")) or (y+1 == lenTablero)) and#diagonal
                   #(((y-1 > -1) and (x+1 < lenTablero) and (self.tablero[x+1,y-1] == " "))or (y == 0)) and
                   #(((y-1 > -1) and (y-1 > -1) and (self.tablero[x-1,y-1] == " ")) or (y == 0)) and
                   #(((y+1 < lenTablero)and (x-1 > -1) and (self.tablero[x-1,y+1] == " ")))or (y+1 == lenTablero)):
                        self.tablero[x,y] = str(tam) + str(num)
                        initPosition = True
             
            #elegir orientacion posible            
            orientacion = aOrientacion[np.random.randint(len(aOrientacion))]
            imposible = True
            colision = False
            
            while imposible:                  
                if (((x - tam > 0) and orientacion == "N") or 
                    (((tam + x ) < lenTablero) and orientacion == "S") or 
                    (((lenTablero - y ) >= tam) and orientacion == "E") or 
                    (((y - tam) >= 0) and orientacion == "O")
                    ):                    
                    #alguna coordenada es inicialmente valida
                    colision = checkColision(tam, x,y, orientacion)                        
                    if not colision:
                        imposible = False   
               
                if imposible and colision:                    
                    aOrientacion = ["N","S","E","O"]   
                    #new init position
                    #borrar coordenada valida
                    initPosition = False  
                    orientacion = aOrientacion[np.random.randint(len(aOrientacion))] 
                    
                elif imposible:
                    orientacion = aOrientacion[np.random.randint(len(aOrientacion))] 
                    
               
            #colocar barco
            #print("colocar barco", orientacion, x, y, tamBarco, tam)
            
            while tamBarco:
                print(tamBarco, "tambarco", tam, num )
                t = tamBarco -1                 
                self.tablero[x+(coord[orientacion][0]*t), y+(t*coord[orientacion][1])] = tam
                self.tablero_barcos[x+(coord[orientacion][0]*t), y+(t*coord[orientacion][1])] = str(tam) + str(num)
                tamBarco-=1            
            
            tamBarco = tam
        #print("tablero ", self.nombre , self.tablero,"\n", self.tablero_barcos)               
  
    def mostrarTableros(self):
        print("\n", f"            Tablero de barcos:                                           Tablero de impactos:", "\n")
        self.imprimir_tablero(self.tablero, self.tablero_impactos, True, self.nombre)

    # def mostrarImpactos(self):
    #     print(" \n", f"Tablero de impactos de {self.nombre}:", " \n")
    #     self.imprimir_tablero(self.tablero_impactos, False, self.nombre)

    def todosHundidos(self):        
        return len(np.where( self.tablero != "X")) == 0 

    def barcoTocado(self, x, y):
        return self.tablero[x,y] == "O" or self.tablero[x,y].isdigit()

    def incrementar_letra(letra):
            return chr(ord(letra)+1)


    def imprimir_fila_de_numeros(self):
        fila_de_numeros_doble = "|   "
        
        for x in range(10):
            if x == 9:
                fila_de_numeros_doble += f"| {x+1}"
            else:
                fila_de_numeros_doble += f"| {x+1} "
        fila_de_numeros_doble += "|                |   "
        for x in range(10):
            if x == 9:
                fila_de_numeros_doble += f"| {x+1}"
            else:
                fila_de_numeros_doble += f"| {x+1} "
        fila_de_numeros_doble += "|"
        print(fila_de_numeros_doble)



    def imprimir_separador_horizontal(self):
        separador_doble = ""
        for _ in range(11):
            separador_doble += "+---"
        separador_doble += "+                "
        for _ in range(11):
            separador_doble += "+---"
        separador_doble += "+"
        print(separador_doble)

## Función que imprime el tablero en paralelo generando dos strings. 
# @params: 
# matriz_barcos: Numpy.ndarray con digitos que representa los barcos. 
# matriz_impactos: Numpy.Array que representa los impactos en el contrario
# deberia_mostrar_barcos: Booleano que representa y se deberían imprimirse barcos. 
# jugador: ???

    def imprimir_tablero(self, matriz_barcos, matriz_impactos, deberia_mostrar_barcos, nombre_jugador):
      
        for (y, letra) in zip(range(10), "ABCDEFGHIJ"):
            self.imprimir_separador_horizontal()
            m_barcos_string: str = f"| {letra} "
            m_impactos_string: str = f"| {letra} "

            for x in range(10):

                celda_barco = matriz_barcos[y][x]
                celda_impactos = matriz_impactos[y][x]

                if not deberia_mostrar_barcos and celda_barco != " " and celda_barco != "-" and celda_barco != "X":
                    celda_barco = " "
               
                if celda_barco.isdigit():
                    celda_barco = "O"

                ## TODO: Revisar la doble negación Booleana, el not (not ) no está muy bonito. 
                if not (not deberia_mostrar_barcos) and celda_impactos != " " and celda_impactos != "-" and celda_impactos != "X":
                    celda_impactos = " "
                
                    
                m_barcos_string += f"| {celda_barco} "
                m_impactos_string += f"| {celda_impactos} "

            m_barcos_string += "|" 
            m_impactos_string  += "|" 

            print( m_barcos_string + "                " + m_impactos_string )
        
        self.imprimir_separador_horizontal()
        self.imprimir_fila_de_numeros()
        self.imprimir_separador_horizontal()
   
    def barcoHundido(self, x, y):           
        if (len(self.tablero_barcos[self.tablero_barcos == self.tablero_barcos[x,y]]) <= 1): 
            print("Hundido barco de " ,self.tablero[x,y], " posiciones!")
        return len(self.tablero_barcos[self.tablero_barcos == self.tablero_barcos[x,y]]) <= 1

    def getIndiceLetra(self,letra:str): #   
        return ord(letra.replace(" ", "").upper()) - 65

    def getDisparo(self, x, y): #
        res = ""
        #la X puede ser una letra de la A a la J, lo contemplamos tambien
        if isinstance(x,str):
            if(x.isdigit()):
                x = int(x)
            else:                   
                x = self.getIndiceLetra(x)
        y = int(y)
        
        
        if self.tablero[x,y] == "O" or self.tablero[x,y].isdigit():
            if self.todosHundidos():
                res =  "fin de juego"
            elif self.barcoHundido(x,y):
                res = "XX"
            elif self.barcoTocado(x,y):
               res =  "X"
         
        else:
            res =  "-"
        
        #self.setDisparo( x, y, res)
        return res 

    def setDisparo(self, x, y, res): # coordenadas de disparo y actualizacion de estas en el tablero_impacto
        self.tablero_impactos[x,y] = res
    
