from utils import Jugador
from const import barcos, barcosNum
import numpy as np

class Game: 
    turno = True # Si True es el turno del jugador, si False es el turno de la máquina
    status = True # Si True esta On (encendido), si False está Off (apagado)

    def __init__(self, maquina: Jugador, jugador: Jugador): # Tipo el argumento para que quede fija la clase del objeto
        self.maquina = maquina
        self.jugador = jugador  


    def SalirInicio(self,exit_word:str): # Filtro input inicial para salir
        if exit_word.replace(" ","").upper() == "SALIR" or exit_word.replace(" ","").upper() =="NO":
            x2 = input("¿Estás seguro? Si sales abandonarás el barco (si/no):") # Doble check

            if x2.replace(" ","").upper() == "SALIR" or x2.replace(" ","").upper() =="SI": 
                print("\n","Esperábamos más de ti, grumete, pero se ve que no tenías la valía necesaria.","\n")
                quit()

    def GetIndiceLetra(self,x:str): # Función de utilidad para adquirir el indice de la letra.

        for i, v in enumerate(["A","B","C","D","E","F","G","H","I","J"]):
            if v == x.replace(" ","").upper():
                return i 

    def GetIndiceNumero(self,y:str): # Función de utilidad para adquirir el indice de la letra.

        for i, v in enumerate(["1","2","3","4","5","6","7","8","9","10"]):
            if v == y.replace(" ","").upper():
                return i

    def AskCoordx(self): # Filtro input de la coordenada x (str)
        loop = True
        while loop:

            x = input("Coordenada del eje x (A a J):")

            if x.replace(" ","").upper() == "SALIR": # Opcion para salir
                x2 = input("¿Estás seguro? Si sales abandonarás el barco (si/no):") # Doble check

                if x2.replace(" ","").upper() == "salir" or x2.replace(" ","").upper() =="SI": 
                    print("\n","Esperábamos más de ti, grumete, pero se ve que no tenías la valía necesaria.","\n")
                    loop = False
                    quit()
    
                else:
                    continue

            elif x.replace(" ","").upper() in ["1","2","3","4","5","6","7","8","9","10"]: # Opcion de que se pueda introducir un numero en eje y

                loop = False
                return int(x)-1
                

            elif x.replace(" ","").upper() in ["A","B","C","D","E","F","G","H","I","J"]:

                loop = False
                return self.GetIndiceLetra(x)

            else:
                print("\n","Coordenada Inválida. Prueba una letra de la A a la J.""\n",)


                
    def AskCoordy(self): # Filtro input de la coordenada y (int)
        loop = True
        while loop:

            y = input("Coordenada del eje y (1 al 10):")

            if y.replace(" ","").upper() == "SALIR": # Opcion para salir
                y2 = input("¿Estás seguro? Si sales abandonarás el barco (si/no):") # Doble check

                if y2.replace(" ","").upper() == "SALIR" or y2.replace(" ","").upper() =="SI": 
                    print("\n","- Capitán Sardino: Esperábamos más de ti, grumete, pero se ve que no tenías la valía necesaria.","\n")
                    loop = False
                    quit()
    
                else:
                    continue

            elif y.replace(" ","").upper() in ["1","2","3","4","5","6","7","8","9","10"]:
                loop = False
                return self.GetIndiceNumero(y)
                
            else:
                print("\n","Coordenada Inválida. Prueba un número entero entre 1 y 10.""\n",)
    
    # def CheckCoord(self,x,y): # Funcion de check Si dispara a la misma coordenada
    #     while self.jugador.tablero_impactos[x][y] != " ": 
    #         print("\n","-Capitán Sardino: MERLUZO! Ya hemos disparado a esa coordenada.","\n",)
    #         x = self.AskCoordx()
    #         y = self.AskCoordy()

   

    def Jugar(self): # FUNCIÓN QUE EJECUTA EL DESARROLLO DEL JUEGO
        
        while self.status: #  while True
            if self.turno:  
                # TURNO/LOGICA DEL JUGADOR: 
                # 1. coordenadas? > disparo
                # 2. feedback despues del impacto > jugador.getDisparo()
                # 3. si agua: turno = False ; si impacta: continue or status = False
                
                print("\n", f"--------------------------------------------TURNO de {self.jugador.nombre}----------------------------------------------") 
                self.jugador.mostrarTableros() # Muestra tablero al inicio del turno
                print("\n","- Capitán Sardino: Y bien grummete, ¿hacia donde disparamos?","\n")
                x = self.AskCoordx()
                y = self.AskCoordy()
                #self.CheckCoord(x,y)
                while self.jugador.tablero_impactos[x][y] != " " : # Check si dispara a la misma coordenada
                    print("\n","-Capitán Sardino: MERLUZO! Ya hemos disparado a esa coordenada.","\n",)
                    x = self.AskCoordx()
                    y = self.AskCoordy()

                print("\n","* Disparando a la flota enemiga...*")

                res = self.jugador.getDisparo(x,y)    # Reemplaza coordenada y actualiza tablero_impactos jugador

                if res == "-": # Si dispara en agua
                    self.maquina.tablero[x][y] = res # Actualiza esa coordenada en el tablero de barcos de la maquina
                    self.turno = False
                    print("\n","* Fallo *                                 - Capitán Sardino: Fallamos!, arr. Más al loro grumete!")
                
                elif res == "fin de juego": # Si todo los barcos de maquina se hunden
                    self.maquina.tablero[x][y] = res # Actualiza esa coordenada en el tablero de barcos de la maquina
                    self.status = False
                    print("\n","* Impacto *")
                    print("\n","* Barco tocado y hundido *                - Capitan Sardino: HurraAaAa! Hemos vencido!")
                    print("\n","Victoria magistral. Todos los barcos de la flota enemiga han sido derrotados.")
                    break
                else: # Si impacta en un barco de maquina
                    self.maquina.tablero[x][y] = "X" # Actualiza esa coordenada en el tablero de barcos de la maquina
                    print("\n","* Impacto *                              - Capitan Sardino: por las barbas de Neptuno. Buen disparo!") 
                    continue

            else:
                # TURNO/LOGICA DE LA MAQUINA: 
                # 1. coordenadas aleatorias sin repetir (verifica que no haya nada en la coordenada de tablero_impactos) > disparo
                # 2. feedback despues del impacto > jugador.getDisparo()
                # 3. si agua: turno = False ; si impacta: continue or status = False -> Y actualiza tablero


                print("\n",f"--------------------------------------------TURNO de {self.maquina.nombre}----------------------------------------------")

                while self.turno == False: 
                    x = np.random.randint(10)
                    y = np.random.randint(10)
                    while self.maquina.tablero_impactos[x][y] != " ": # Check de no disparar a la misma coordenada
                        x = np.random.randint(10)
                        y = np.random.randint(10)
                    
                    print("\n","* Barco enemigo disparando... *")

                    res = self.maquina.getDisparo(x,y)  # Reemplaza coordenada en tablero_barcos del jugador

                    if res == "-": # Si dispara en agua
                        self.jugador.tablero[x][y] = res # Actualiza esa coordenada en el tablero de barcos del jugador
                        self.turno = True
                        print("\n","* Fallo *                                 - Capitán Sardino: Eso estuvo cerca.")
                       
                    elif res == "fin de juego":  # Si todos los barcos del jugador se hunden
                        self.jugador.tablero[x][y] = res # Actualiza esa coordenada en el tablero de barcos del jugador
                        self.status = False
                        print("\n","* Impacto *")
                        print("\n","* Barco tocado y hundido *                - Capitán Sardino: Gluglugluglu...")
                        print("\n","Derrota aplastante. Todos los barcos de tu flota se han ido a pique...")
                        break
                    else: # Si impacta en barco de jugador
                        self.jugador.tablero[x][y] = "X" # Actualiza esa coordenada en el tablero de barcos del jugador
                        print("\n","* Impacto *                               - Capitán Sardino: Ouch!")
                        continue
                    