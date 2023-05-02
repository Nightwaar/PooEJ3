from clase import Registro
import csv
class Manejador:    
    __lista=[]
    
    def __init__(self):
        self.__lista=[[]]
        return
    def leerarc(lista):
        archivo = open('temp.csv')
        reader = csv.reader(archivo,delimiter=',')
        for fila in reader:
            lista.cargar(fila)
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
#========================================================================================================================================================                
    def accion1(lista):
        print("Gay")
#=========================================================================================================================================================
    def accion2(self,lista):       
        for hora in self.__lista:
            temp = 0
            hora = 0
            for dia in hora:
                temp =sum(lista[[dia-1][hora]])
                hora +=1
            total = temp/hora
            print("El promedio del día {} es: {}".format(dia-1,total))
        return
    def accion3(lista):
        numdia = int(input("Ingrese el día para mostrar sus parámetros: "))
        print ("'Hora' 'Temperatura' 'Humedad' 'Presión'",sep='    ')
        hora= 0
        for i in lista:
            formato = "{:<5}|{:<10}|{:>5}|{:>10}"
            fila_formateada = formato.format(*lista)
            print("hora",fila_formateada)
            hora=sum(1)
        return