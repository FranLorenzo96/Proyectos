
import os

def validarnumfloat():
    while True:
        try:
            num=float(input("Ingrese numero: "))
            break
        except:
            print("Valor ingresado no valido")
    return num

def validarnumint():
    while True:
        try:
            num=int(input("Ingrese numero: "))
            break
        except:
            print("Valor ingresado no valido")
    return num

def validarlegajo(lista):
    global legajo
    for k in range(len(lista)):
                while lista[k][2]==legajo:
                    print("Ya existe un legajo con ese numero, ingrese otro")
                    legajo=validarnumint()

def tomarterc(elem):
    return elem[2]

def opcionsalir():
    print("Ingrese 1 si quiere volver al menu")
    opcion=validarnumint()
    while opcion!=1:
        print("Ingrese 1 si quiere volver al menu")
        opcion=validarnumint()





opcion=0
lista=[]
while opcion!=7:
    os.system("cls")
    i=0
    j=0
    k=0
    print("---------------")
    print("")
    print("1. Cargar datos para nuevos socios")
    print("2. Mostrar datos de todos los clientes")
    print("3. Modificar estado de un socio")
    print("4. Dar de baja a un socio")
    print("5. Ver recaudacion actual")
    print("6. Ver recaudacion mensual y anual")
    print("7. Salir")
    print("")
    print("---------------")

    print("Ingrese la opcion a elegir")
    
    opcion=validarnumint()
    while opcion<0 or opcion>7: 
        print("El valor ingresado no es una opcion")
        opcion=validarnumint()
    
    if opcion==1:
        os.system("cls")
        print("Ingrese la cantidad de personas a la que se cargara datos: ")
        n=validarnumint()
        for i in range(n):
            os.system("cls")
            print("")
            nombre=input("Ingrese nombre de la persona: ")
            apellido=input("Ingrese apellido de la persona: ")
            print("Ingrese numero de legajo")

            legajo=validarnumint()
            validarlegajo(lista)

            print("Ingrese numero de telefono sin guiones ni espacios")
            tel=validarnumint()
            mail=input("Ingrese mail: ")
            print("Ingrese situacion de la persona")
            print("Ingrese 1 si el socio pago la ultima cuota, ingrese 2 si no")
            situacion=validarnumint()
            while situacion!=1 and situacion!=2:
                print("El valor ingresado no es valido, intente de nuevo")
                situacion=validarnumint()
            if situacion==1:
                situacion=True
            else:
                situacion=False
            print("Ingrese condicion de socio")
            print("Ingrese 1 si el socio tiene una suscripcion Estandar, 2 si tiene una suscripcion Premium: ")
            condicion=validarnumint()
            while condicion!=1 and condicion!=2:
                print("El valor ingresado no es valido, intente de nuevo: ")
                condicion=validarnumint()
            if condicion==1:
                condicion=False
            else:
                condicion=True
            lista.append([nombre,apellido,legajo,tel,mail,situacion,condicion])
    elif opcion==2:
        
        listaord=sorted(lista,key=tomarterc)
        os.system("cls")
        print("")
        print("Cantidad de socios: ",len(listaord))
        print("")
        print("Datos de todos los socios ordenados por N° de legajo")
        print("")
        for j in range(len(listaord)):
            
            print("--------")
            print("a. Nombre:",listaord[j][0],"-- Apellido:",listaord[j][1])
            print("b. Legajo: ",listaord[j][2])
            print("c. Telefono: ",listaord[j][3])
            print("d. Mail: ",listaord[j][4])
            if listaord[j][5]==True:
                Sit="Al dia con las cuotas"
            else:
                Sit="No esta al dia con las cuotas"
            print("e. Situacion actual: ",Sit)
            
            print("--------")
        print("")
        
        opcionsalir()
        os.system("cls")
    elif opcion==3:
        os.system("cls")
        print("")
        print("Ingrese n°legajo del socio a cambiar su condicion")
        socio=validarnumint()
        try:
            for k in range(len(lista)):
                if lista[k][2]==socio:
                    break
                
                
            if lista[k][6]==True:
                estado="Premium"
            else:
                estado="Estandar"
            print(lista[k][0],lista[k][1],"es socio/a",estado,"del club.¿Desea cambiar esta condicion?")
            print("1. Si")
            print("2. No")
            opcion31=validarnumint()
            while opcion31<0 and opcion31>2:
                print("El valor ingresado no es una opcion")
                opcion31=validarnumint()
            if opcion31==1:
                print("Ingrese 1 si quiere que el socio pase a condicion Estandar, ingrese 2 si quiere que pase el socio a condicion Premium")
                eleccion=validarnumint()
                while eleccion<0 and eleccion>2:
                    print("El valor ingresado no es una opcion")
                    eleccion=validarnumint()
                if eleccion==1:
                    lista[k][6]=False
                    print(f"El socio {lista[k][0]}{lista[k][1]} ahora es Estandar")
                else:
                    lista[k][6]=True
                    print(f"El socio {lista[k][0]}{lista[k][1]} ahora es Premium")
                opcionsalir()
        except:
           print("No se encontro un socio con ese numero de legajo")
           opcionsalir()
        
    elif opcion==4:
        os.system("cls")
        print("Ingrese legajo del socio a eliminar del sistema")
        socio1=validarnumint()
        try:
            os.system("cls")
            for i in range(len(lista)):
                if lista[i][2]==socio1:
                    break
            print("¿Desea eliminar al socio",lista[i][0],lista[i][1],"?")
            print("1. Si")
            print("2. No")
            opcion41=validarnumint()
            while opcion41<0 and opcion41>2:
                print("El valor ingresado no es una opcion")
                opcion41=validarnumint()
            if opcion41==1:
                os.system("cls")
                eliminado=lista.pop(i)
                print("El socio",eliminado[0],eliminado[1],"fue eliminado del sistema")
                opcionsalir()
            else:
                pass
        except:
            print("No se encontro un socio con ese numero de legajo")
            opcionsalir()
    elif opcion==5:
        os.system("cls")
        sumap=0
        sumapfaltante=0
        sumae=0
        sumaefaltante=0
        npremium=0
        npremiumfaltante=0
        nestandar=0
        nestandarfaltante=0
        for j in range(len(lista)):
            if lista[j][6]==True:    #Si es premium 
                    
                
                if lista[j][5]==True:   #si pago
                    npremium+=1
                    sumap+=5800
                else:
                    npremiumfaltante+=1
                    sumapfaltante+=5800
            else:
                
                if lista[j][5]==True:
                    nestandar+=1
                    sumae+=1800
                else:
                    nestandarfaltante+=1
                    sumaefaltante+=1800
        print("---------Informe de recaudacion actual---------")
        print("")
        print(f"El club cuenta con {npremium} socios Premium al dia y {nestandar} socios Estandar al dia")
        print(f"Recaudacion total: {sumap+sumae}")
        print("")
        print(f"El club cuenta con {npremiumfaltante} socios Premium con deuda y {nestandarfaltante} socios Estandar con deuda")
        print(f"Recaudacion faltante: {sumaefaltante+sumapfaltante}")
        print("")
        opcionsalir()
    elif opcion==6:
        os.system("cls")
        npremium=0
        sumap=0
        nestandar=0
        sumae=0
        for i in range(len(lista)):
            if lista[i][6]==True:
                npremium+=1
                sumap+=5800
            else:
                nestandar+=1
                sumae+=1800        


        print("Ingrese el objetivo de recaudacion anual: ")
        objetivo=validarnumint()
        os.system("cls")

        print("-----Informe de Recaudacion-----")
        print("-----Informacion de socios-----")
        print("Premium:")
        print("Los socios premium tienen un abono mensual de $5800")
        print(f"El club cuenta con {npremium} socios en condicion Premium")
        print(f"El club recauda ${sumap} con sus socios en condicion premium")
        print("Estandar:")
        print("Los socios estandar tienen un abono mensual de $1800")
        print(f"El club cuenta con {nestandar} socios en condicion estandar")
        print(f"El club recauda ${sumae} con sus socios en condicion estandar")
        print("----------------------------")
        print("Recaudacion mensual final: $",sumap+sumae)
        print("Recaudacion anual final: $",12*(sumap+sumae))
        print("----------------------------")
        print("Apreciacion final: ")

        if objetivo<=12*(sumap+sumae):
            print(f"Siendo ${objetivo} el objetivo anual de recaudacion del club y ${12*(sumap+sumae)} la recaudacion final obtenida, el objetivo anual de recaudacion se consiguio")
        else:
            print(f"Siendo ${objetivo} el objetivo anual de recaudacion del club y ${12*(sumap+sumae)} la recaudacion final obtenida, el objetivo anual de recaudacion no se logro")
        
        print("")
        opcionsalir()

    
os.system("cls")