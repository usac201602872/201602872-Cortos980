def Collatz(): # Funcion para empezar la lista
    N = int(input("Ingrese el numero N al que quiere llegar:")) #Numero N al que se quiere llegar
    Listado=[]  #Listado principal
    for i in range(2,N+1):  #Para hacer cada numero hasta llegar a N
        Listado2=[]     #Listados para llenar
        while(i>1):     #Siempre que el numero sea mayor a 1, hara las siguientes funciones
            if i%2==0:          #Si N es par, hara N/2
                Listado2.append(i)
                i = i//2
            else:               #Si N es impar, hara 3N+1
                Listado2.append(i)
                i = (i*3)+1
            if i==1:            #Al llegar a 1, pondra al final de la lista el 1
                Listado2.append(1)
        Listado.append(Listado2)
    print(Listado)

datos=[]
O = input("Escriba START para comenzar la programacion:")
if O == 'START':
    Collatz()
    col= open('collatz.txt','w')
    col.close()
else:
    print("Escribio mal, ahora se unio a Anonymous. Feliz Dia.")


