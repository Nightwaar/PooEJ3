from clase import Registro
from Controlador import Manejador

if __name__ == '__main__':
    liista=Manejador()
    Manejador.leerarc(liista)
    print("Opcion 1:Mostrar la el dia y hora de menor y mayor valor")
    print("Opcion 2: Indicar la temperatura promedio mensual por cada hora")
    print("Opcion 3: Mostrar los parametros meteorológicos de un día")
    print("Opcion 4: Mostrar todo")
    opc = int(input("Ingrese opcion: "))
    while opc!=5:
        if opc == 1:
            Manejador.accion1(liista)
        elif opc ==2:
            Manejador.accion2(liista)
        elif opc == 3:
            Manejador.accion3(liista)
        elif opc ==4:
            Manejador.mostrar(liista)
        elif opc == 5:
            print("Gracias por elegirnos")
        opc = int(input("Ingrese nuevamente una opcion: "))