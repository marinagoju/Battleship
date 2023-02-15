import numpy as np

#class Game: 

#clase jugador
class Jugador:
    machine = False
    tablero = []
    tablero_impactos = []
    coord = {
        "N":[-1,0],
        "S":[1,0],
        "E":[0,1],
        "O":[0,-1],
    }
    
    def __init__(self, maquina, lenTablero, nombre):
        self.lenTablero = lenTablero
        self.machine = maquina
        self.nombre = nombre
       
        
    def initTablero(self):
        #Crea tablero de lenTableroxlenTablero relleno de espacio        
        self.tablero = np.full((self.lenTablero,self.lenTablero), " ")
        self.impactos = np.full((self.lenTablero,self.lenTablero), " ")
        print("Inicializar tablero", "de maquina?", self.machine, "\n", self.tablero, )

        
    

    def colocarBarcos(self, tamBarco, num):
        print("colocar", num , "barcos de ", tamBarco, "\n")

        def checkColision(tamBarco, x,y, orientacion):
            t = tamBarco 
            colision = False
            c1 = x
            c2 = y
            
            while t:            
                #TODO comprobar que ningún barco está alrededor
                if((self.tablero[c1+self.coord[orientacion][0]-1, c2+self.coord[orientacion][1]-1]!= " ") and #casilla libre
                #casilla libre Left Right Up Down D1 D2 D3 D4               
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
                        self.tablero[x,y] = "I"
                        initPosition = True
                print(self.tablero)
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
                    initPosition = False  
                    orientacion = aOrientacion[np.random.randint(len(aOrientacion))] 
                    
                elif imposible:
                    orientacion = aOrientacion[np.random.randint(len(aOrientacion))] 
                    
               
            #colocar barco
            #print("colocar barco", orientacion, x, y, tamBarco, tam)
            
            while tamBarco-1:
                t = tamBarco -1                 
                self.tablero[x+(self.coord[orientacion][0]*t), y+(t*self.coord[orientacion][1])] = "O"
                tamBarco-=1            
            
            tamBarco = tam
            print(self.tablero)               
                            

        

    def mostrarTablero (self):
        print("Tablero del jugador ", self.nombre, " \n", self.tablero)

        
    def mostrarImpactos(self):
        print("Tablero de impactos del jugador ", self.nombre, " \n", self.tablero_impactos)

    def disparar():
        #si es usuario
        #para testear input a mano
        x = 2
        y = 5
        #TODO lanzar disparo

        #TODO recibir tocado/agua

        #TODO apuntar en tablero de impactos
        #si es maquina
        #TODO generar coordenadas aleatorias 
         #TODO lanzar disparo

        #TODO recibir tocado/agua

        #TODO apuntar en tablero de impactos

       
        #TODO si hundido marcar colindantes
        print("disparar")

tamTablero = 10 # ambos tienen el mismo tamaöo de tablero
j1 = Jugador(False, tamTablero, "Aída")
ordena = Jugador(True, tamTablero, "PC")
j1.initTablero()
j1.colocarBarcos(1, 4)
j1.colocarBarcos(2,3)
j1.colocarBarcos(4,1)
j1.colocarBarcos(3,2)#2 barcos de tres

ordena.initTablero()
ordena.colocarBarcos(4,1)
ordena.colocarBarcos(3,2)
ordena.colocarBarcos(2,3)
ordena.colocarBarcos(1,4)


j1.mostrarTablero()
ordena.mostrarTablero()