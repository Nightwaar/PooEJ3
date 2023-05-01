class Registro:
    __temperatura= 0
    __humedad= 0
    __presionatmosferica= 0 
    def __init__(self,temp,hum,pres):
        self.__temperatura = temp
        self.__humedad = hum
        self.__presionatmosferica = pres
    def __str__(self):
        return 'Temperatura: {},Humedad: {},Presion Atmosferica: {}'.format(self.__temperatura,self.__humedad,self.__presionatmosferica)
class Manejador:
    __lista=[]
    def __init__(self):
        self.__lista=[[]]
        return
    def cargar(self,registro):
        i=int(registro[0])
        if i>len(self.__lista):
            self.__lista.append([])
        self.__lista[i-1].append(Registro(registro[2],registro[3],registro[4]))    
    def mostrar(self):
        for dia in self.__lista:
            print("-------Dia: {}".format(self.__lista.index(dia)+1))
            for fila in dia: 
                print(fila)