import numpy as np
from const import coord

class Jugador:
    machine = False
    tablero = []
    tablero_impactos = []   
      
    def __init__(self, maquina, lenTablero, nombre):
        self.lenTablero = lenTablero
        self.machine = maquina
        self.nombre = nombre
        self.coord = coord
        
    def initTablero(self):        
        self.tablero = np.full((self.lenTablero,self.lenTablero), " ")
        self.tablero_impactos = np.full((self.lenTablero,self.lenTablero), " ")
        print("Inicializar tablero", "de maquina?", self.machine, "\n\n\n\n\n", self.tablero,  "\n")

    def colocarBarcos(self, tamBarco, num):
        print("colocar", num , "barcos de ", tamBarco, "\n")

        def checkColision(tamBarco, x,y, orientacion):
            t = tamBarco 
            colision = False
            c1 = x
            c2 = y
            
            while t:                            
                if((self.tablero[c1+self.coord[orientacion][0]-1, c2+self.coord[orientacion][1]-1]!= " ") and #casilla libre
                #TODO bug casilla libre Left Right Up Down D1 D2 D3 D4 a lo largo del nuevo barco               
                    (((c1+self.coord[orientacion][0]-2 > -1) and (self.tablero[c1+self.coord[orientacion][0]-2, c2+self.coord[orientacion][1]-2]!= " ")) or ((c1+self.coord[orientacion][0]-1) == 0))and#D1 U-D
                    (((c1+self.coord[orientacion][0]-2 > -1) and (self.tablero[c1+self.coord[orientacion][0]-2, c2+self.coord[orientacion][1]]!= " ")) or ((c1+self.coord[orientacion][0]-1) == 0))and#D2 U-I
                    (((c1+self.coord[orientacion][0]-2 > -1) and (self.tablero[c1+self.coord[orientacion][0]+2, c2+self.coord[orientacion][1]]!= " ")) or ((c1+self.coord[orientacion][0]-1) == 0))and#D3 D-I
                    (((c1+self.coord[orientacion][0]-2 > -1) and (self.tablero[c1+self.coord[orientacion][0]+2, c2+self.coord[orientacion][1]+2]!= " ")) or ((c1+self.coord[orientacion][0]-1) == 0))and#D4 D-D
                    (((c1+self.coord[orientacion][0]-2 > -1) and (self.tablero[c1+self.coord[orientacion][0]-2, c2+self.coord[orientacion][1]-1]!= " ")) or ((c1+self.coord[orientacion][0]-1) == 0))and#Up
                    (((c1+self.coord[orientacion][0]+2 < self.lenTablero) and (self.tablero[c1+self.coord[orientacion][0]+2, c2+self.coord[orientacion][1]-1]!= " " ) or ((c1+self.coord[orientacion][1]-1) < self.lenTablero)))and#Down
                    (((c1+self.coord[orientacion][1]-2 > -1) and (self.tablero[c1+self.coord[orientacion][0], c2+self.coord[orientacion][1]-2]!= " ")) or (c1+self.coord[orientacion][1]-1) == 0)and#Left
                    (((c1+self.coord[orientacion][1] < self.lenTablero) and (self.tablero[c1+self.coord[orientacion][0], c2+self.coord[orientacion][1]]!= " ")) or (c1+self.coord[orientacion][1]) == self.lenTablero)):#Right
                        colision = True
                        break
                else:
                    c1 += self.coord[orientacion][0]
                    c2 += self.coord[orientacion][1]
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
                x = np.random.randint(self.lenTablero)
                y = np.random.randint(self.lenTablero)
              
                if ((self.tablero[x,y] == " ") and
                   ((((x+1 < self.lenTablero) and (self.tablero[x+1,y] == " ")) or (x+1 == self.lenTablero))) and
                   (((x-1 > -1) and (self.tablero[x-1,y] == " ") or (x == 0))) and
                   (((y+1 < self.lenTablero) and (self.tablero[x,y+1] == " ")) or (y + 1 == self.lenTablero)) and
                   (((y+1 < self.lenTablero) and (x+1 < self.lenTablero) and (self.tablero[x+1,y+1] == " ")) or (y+1 == self.lenTablero)) and#diagonal
                   (((y-1 > -1) and (x+1 < self.lenTablero) and (self.tablero[x+1,y-1] == " "))or (y == 0)) and
                   (((y-1 > -1) and (y-1 > -1) and (self.tablero[x-1,y-1] == " ")) or (y == 0)) and
                   (((y+1 < self.lenTablero)and (x-1 > -1) and (self.tablero[x-1,y+1] == " ")))or (y+1 == self.lenTablero)):
                        self.tablero[x,y] = tam
                        initPosition = True
               #print(self.tablero, "\n\n\n\n\n\n")
            #elegir orientacion posible            
            orientacion = aOrientacion[np.random.randint(len(aOrientacion))]
            imposible = True
            colision = False
            
            while imposible:                  
                if (((x - tam > 0) and orientacion == "N") or 
                    (((tam + x ) < self.lenTablero) and orientacion == "S") or 
                    (((self.lenTablero - y ) >= tam) and orientacion == "E") or 
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
            
            while tamBarco-1:
                t = tamBarco -1                 
                self.tablero[x+(self.coord[orientacion][0]*t), y+(t*self.coord[orientacion][1])] = tam
                tamBarco-=1            
            
            tamBarco = tam
            #print(self.tablero)               
  
    def mostrarTablero (self):
        print("Tablero del jugador ", self.nombre, " \n")
        self.imprimir_tablero(self.tablero, True, self.nombre)

    def mostrarImpactos(self):
        print("Tablero de impactos del jugador ", self.nombre, " \n")
        self.imprimir_tablero(self.tablero_impactos, False, self.nombre)

    def todosHundidos(self):        
        return len(np.where( self.tablero != "X")) == 0 

    def barcoTocado(self, x, y):
        return self.tablero[x,y] == "O" or self.tablero[x,y].isdigit()

    def incrementar_letra(letra):
            return chr(ord(letra)+1)


    def imprimir_separador_horizontal(self):
        # Imprimir un renglón dependiendo de las columnas
        for _ in range(self.lenTablero+1):
            print("+---", end="")
        print("+")


    def imprimir_fila_de_numeros(self):
        print("|   ", end="")
        for x in range(self.lenTablero):
            print(f"| {x+1} ", end="")
        print("|")

    #https://parzibyte.me/blog/2021/12/21/batalla-naval-python-programacion-juego/#Imprimiendo_tablero
    def imprimir_tablero(self,matriz, deberia_mostrar_barcos, jugador):
        print(f"Tablero del jugador {jugador}: ")
        letra = "A"
        for y in range(self.lenTablero):
            self.imprimir_separador_horizontal()
            print(f"| {letra} ", end="")
            for x in range(self.lenTablero):
                celda = matriz[y][x]
                valor_real = celda
                if not deberia_mostrar_barcos and valor_real != " " and valor_real != "-" and valor_real != "X":
                    valor_real = " "
                
               
                if valor_real.isdigit():
                    valor_real = "O"
                print(f"| {valor_real} ", end="")
            letra = chr(ord(letra)+1)
            print("|",)  # Salto de línea
        self.imprimir_separador_horizontal()
        self.imprimir_fila_de_numeros()
        self.imprimir_separador_horizontal()

    def barcoHundido(self, x, y):
        #funcion a desarrollar si tenemos tiempo - crear diccionario / clase barcos
        res = False
        tamBarco = self.tablero[x,y]
        if (tamBarco == 1):
            res = True
        else:
            #buscar en que direccion crece el barco
            res = False
            #recorrer hasta no encontrar una X
        return res

    def getIndiceLetra(self,letra):        
        return ord(letra.upper()) - 65

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
