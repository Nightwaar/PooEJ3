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
#============================================================================================================
    def mayortemp(self):
        for dia in self.__lista:
            mayor = 0
            for hora in dia:
                if hora.mostrartemp()>mayor:
                    mayor = hora.mostrartemp()
            print("La mayor temperatura del día es: {}".format(mayor))
    def mayorhum(self):
        for dia in self.__lista:
            mayor = 0
            for hora in dia:
                if hora.mostrarhum()>mayor:
                    mayor=hora.mostrarhum()
            print("La mayor humedad del día es: {}".format(mayor))
    def mayorpres(self):
        for dia in self.__lista:
            mayor = 0
            for hora in dia:
                if hora.mostrarpres()>mayor:
                    mayor=hora.mostrarpres()
            print("La mayor presion del día es: {}".format(mayor))
    def menortemp(self):
        for dia in self.__lista:
            menor = 9999
            for hora in dia:
                if hora.mostrartemp()<menor:
                    menor=hora.mostrartemp()
            print("La menor temperatura del día es: {}".format(menor))
    def menorhum(self):
        for dia in self.__lista:
            menor = 9999
            for hora in dia:
                if hora.mostrarhum()<menor:
                    menor=hora.mostrarhum()
            print("La menor humedad del día es: {}".format(menor))
    def menorpres(self):
        for dia in self.__lista:
            menor = 9999
            for hora in dia:
                if hora.mostrarpres()<menor:
                    menor=hora.mostrarpres()
            print("La menor presion del día es: {}".format(menor))
#========================================================================================================================================================                
    def accion1(self):
        self.mayortemp()
        self.mayorhum()
        self.mayorpres()
        self.menortemp()
        self.menorhum()
        self.menorpres()
#=========================================================================================================================================================
    def accion2(self):       
        for hora in self.__lista:
            temp = 0
            con = 0
            for dia in hora:
                temp +=dia.mostrartemp()
                con +=1
            total = temp/con
            print("El promedio de la hora es: {}".format(total))
        return
#=======================================================================================================================
    def accion3(self):
        numdia = int(input("Ingrese el día para mostrar sus parámetros: "))
        print ("'Hora' 'Temperatura' 'Humedad' 'Presión'",sep='    ')
        for hora in self.__lista[numdia-1]:
            #print(hora)
            print("{}         {}        {}        {}".format(hora,hora.mostrartemp(),hora.mostrarhum(),hora.mostrarpres()))         
        return