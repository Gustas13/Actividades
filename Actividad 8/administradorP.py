from  particula import Particula
import json
#Aristas
from pprint import pprint, pformat

class AdministradorP:
    def __init__(self):
        self.__particulas = []
        self.grafo = dict()
    
    def agregar_final(self, particula:Particula):
        self.__particulas.append(particula)

    def agregar_inicio(self, particula:Particula):
        self.__particulas.insert(0, particula)

    def mostrar(self):
        for particula in self.__particulas:
            print(particula)
        
    def __str__(self):
        return "".join (str(particula) + '\n' for particula in self.__particulas)

    def __len__(self):
        return len(self.__particulas)

    def __iter__(self):
        self.cont = 0
        return self

    def __next__(self):
        if self.cont < len (self.__particulas):
            particula = self.__particulas[self.cont]
            self.cont += 1
            return particula

        else:    
            raise StopIteration
        

    def guardar (self, ubicacion):
        try:
            with open(ubicacion, 'w') as archivo:
                lista = [particula.to_dict() for particula in self.__particulas]
                print (lista)
                json.dump(lista, archivo, indent=5)
                #archivo.write(str(self)) 
                return 1

        except:
                return 0
    
    def abrir(self, ubicacion):
        try:
            with open(ubicacion, 'r') as archivo:
                lista = json.load(archivo)
                self.__particulas = [Particula(**particula) for particula in lista]
            return 1
        except:
            return 0 
    
    #Sort
    def ordenarVel(self):
        self.__particulas.sort()

    #Lambda
    def ordenarDist(self):
        self.__particulas.sort(key=lambda particula:particula.distancia, reverse=True)

    def ordenarId(self):
        self.__particulas.sort(key=lambda particula:particula.id)
    
    #Aristas      
     
    def RecuperarAris(self):
        self.grafo.clear()
        for particula in self.__particulas: 
            origen = str(particula.origen_x) +', ' + str(particula.origen_y).upper()
            destino = (str(particula.destino_x) +', ' + str(particula.destino_y)).upper()
            peso = int(particula.distancia)
            arista_o_d = (destino, peso)
            arista_d_o = (origen, peso)
            if origen in self.grafo:
               self.grafo[origen].append(arista_o_d)
            else:
               self.grafo[origen] = [arista_o_d]
            if destino in self.grafo:
              self.grafo[destino].append(arista_d_o)
            else:
               self.grafo[destino] = [arista_d_o]

        a = str(pformat(self.grafo, width=40, indent=1)+'\n')
        print(a)
        return a
            

             
     
        