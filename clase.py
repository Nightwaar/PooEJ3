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