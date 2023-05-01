from clase import Registro,Manejador
import csv
if __name__ == '__main__':
    lista=Manejador()
    archivo = open('temp.csv')
    reader = csv.reader(archivo,delimiter=',')
    for fila in reader:
        lista.cargar(fila)
    lista.mostrar()