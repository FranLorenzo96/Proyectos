import os
from pickle import dump,load
from msvcrt import getch as m

class Persona:
    def __init__(self):
        self.nombre=input("Ingrese nombre: ")
        self.apellido=input("Ingrese apellido: ")
        self.dni=int(input("Ingrese DNI: "))
        self.edad=int(input("Ingrese edad: "))
    def __str__(self):
        info="Nombre: "+self.nombre+"\nApellido: "+self.apellido+"\nDNI: "+str(self.dni)+"\nEdad: "+str(self.edad)
        return info

class Docente(Persona):
    def __init__(self):
        super().__init__()
        self.especialidad=input("Especialidad del docente: ")
    def getEspecialidad(self):
        return "\nEspecialidad del docente: "+self.especialidad
    def setEspecialidad(self,nuevaEspecialidad):
        self.especialidad=nuevaEspecialidad
    def __str__(self) -> str:
        info=super().__str__()
        info+=self.getEspecialidad()+"\n"
        return info

class Estudiante(Persona):
    def __init__(self):
        super().__init__()
        opcion=input("El estudiante tiene Actividad extracurricular? (y/n)")
        if opcion=="y":
            opcion2=input("Que actividad curricular realiza? (EdFisica,Teatro,Musica)")
            if opcion2=="EdFisica" or opcion2=="edfisica" or opcion2=="Edfisica":
                self.actividadextra=EdFisica()
            elif opcion2== "Teatro" or opcion2=="teatro":
                self.actividadextra=Teatro()
            elif opcion2=="Musica" or opcion2=="musica":
                self.actividadextra=Musica()
        elif opcion=="n":
            self.actividadextra=None
            pass
    def __str__(self):
        info=super().__str__()
        if self.actividadextra==None:
            pass
        else:
            info+=self.actividadextra.__str__()
        return info

    def calcularCosto(self):
        if self.actividadextra==None:
            self.costoEstudiante=1500
        else:
            self.costoEstudiante=1500+self.actividadextra.getCosto()
        return self.costoEstudiante
    
    def checkAct(self):
        if self.actividadextra==None:
            return False
        else:
            return True

class ActividadExtracurricular:
    def __init__(self,actividad,cantHoras,costo):
        self.actividad=actividad
        self.cantHoras=cantHoras
        self.costo=costo
    def __str__(self):
        return "\nActividad Extracurricular: "+self.actividad+"\nCantidad Horas: "+str(self.cantHoras)+"\nCosto de Actividad Extracurricular: "+str(self.costo)+"\n"
    def getCosto(self):
        return self.costo
    def getcantidadHoras(self):
        return self.cantHoras

class EdFisica(ActividadExtracurricular):
    def __init__(self):
        super().__init__("Educacion Fisica", 4 , 700)

class Teatro(ActividadExtracurricular):
    def __init__(self):
        super().__init__("Teatro",6, 1000)

class Musica(ActividadExtracurricular):
    def __init__(self):
        super().__init__("Musica", 4, 800)

class Curso:
    def __init__(self):
        self.año=int(input("Ingrese año del curso: "))
        self.profesores=[]
        self.estudiantes=[]
        n=int(input("Ingrese cantidad de profesores en el curso: "))
        for i in range(n):
            self.profesores.append(Docente())
        m=int(input("Ingrese cantidad de alumnos en el curso: "))
        for m in range(m):
            self.estudiantes.append(Estudiante())
    def __str__(self):
        info="Curso "+str(self.año)+"°\n"
        info+="Recaudacion: "+str(self.Recaudacion())
        info+="\n:Profesores:\n"
        for i in self.profesores:
            info+=i.__str__()
        info+="\n:Estudiantes:\n"
        for j in self.estudiantes:
            info+=j.__str__()
        return info
    def getAño(self):
        return self.año
    def Recaudacion(self):
        rec=0
        for i in self.estudiantes:
            rec+=i.calcularCosto()
        return rec
    def agregarDocente(self):
        self.profesores.append(Docente())
    def agregarEstudiante (self):
        self.estudiantes.append(Estudiante())
    def getDocentes(self):
        info="\nCurso "+str(self.año)+"°\n"
        for i in self.profesores:
            info+=i.__str__()
        return info
    def getAlumnos(self):
        info="\nCurso "+str(self.año)+"°\n"
        for i in self.estudiantes:
            info+=i.__str__()
        return info
    def getAlumnosAct(self):
        info=""
        for i in self.estudiantes:
            if i.checkAct():
                info+=i.__str__()
        return info
    def getAlumnosNoAct(self):
        info=""
        for i in self.estudiantes:
            if not i.checkAct():
                info+=i.__str__()
        return info

            

class GestionAcademica:
    def __init__(self):
        self.cargar()
        opcion=None
        if len(self.cursos)<1:
            while opcion!=2 and len(self.cursos)<1:
                os.system("cls")
                print('\033[H\033[J', end='')
                print(":::Menu:::")
                print("")
                print("Eliga una opcion: ")
                print("1- Cargar Datos de cursos")
                print("2- Salir")
                opcion=int(input("Eliga opcion: "))
                if opcion==1:
                    os.system("cls")
                    print('\033[H\033[J', end='')
                    n=int(input("Ingrese la cantidad de cursos a cargar: "))
                    for i in range(n):
                        self.agregarCurso()
                    opcion=None
                    os.system("cls")
                    print('\033[H\033[J', end='')
                    self.guardar()
                    print("Presione cualquier tecla para continuar...")
                    m()
        elif len(self.cursos)>=1:
            opcion=None
            while opcion!=5:
                os.system("cls")
                print('\033[H\033[J', end='')
                print(":::Menu:::")
                print("")
                print("Eliga una opcion: ")
                print("1- Cargar Datos de cursos")
                print("2- Mostrar Todos los Cursos")
                print("3- Buscar")
                print("4-Recaudacion total")
                print("5- Salir")
                opcion=int(input("\nIngrese opcion: "))
                if opcion==1:
                    os.system("cls")
                    print('\033[H\033[J', end='')
                    n=int(input("Ingrese la cantidad de cursos a cargar: "))
                    for i in range(n):
                        self.agregarCurso()
                    opcion=None
                    os.system("cls")
                    print('\033[H\033[J', end='')
                    self.guardar()
                    print("Presione cualquier tecla para continuar...")
                    m()
                elif opcion==2:
                    os.system("cls")
                    print('\033[H\033[J', end='')
                    print("\n\n:::Cursos:::\n")
                    for i in self.cursos:
                        print(i.__str__())
                    opcion==None
                    print("Presione cualquier tecla para continuar...")
                    m()
                elif opcion==3:
                    opcion2=None
                    while opcion2!=6:
                        os.system("cls")
                        print('\033[H\033[J', end='')
                        print(":::Menu:::\n")
                        print("Eliga una opcion:")
                        print("1-Mostrar todos los docentes")
                        print("2-Mostrar todos los alumnos")
                        print("3-Mostrar docentes y estudiantes de un curso")
                        print("4-Mostrar estudiantes que realizan actividad extracurricular")
                        print("5-Mostrar estudiantes que NO realizan actividad extracurricular")
                        print("6-Volver\n")
                        opcion2=int(input("Eliga una opcion: "))
                        if opcion2==1:
                            os.system("cls")
                            print('\033[H\033[J', end='') 
                            print(":::Plantel docente:::\n")
                            doc=""
                            for i in self.cursos:
                                doc+=i.getDocentes()
                            print(doc)
                            print("\nPresione cualquier tecla para continuar...")
                            m()
                        elif opcion2==2:
                            os.system("cls")
                            print('\033[H\033[J', end='')
                            print(":::Estudiantes:::\n")
                            est=""
                            for i in self.cursos:
                                est+=i.getAlumnos()
                                print(est)
                            print("\nPresione calquier tecla para continuar...")
                            m()
                        elif opcion2==3:
                            os.system("cls")
                            print('\033[H\033[J', end='')
                            k=int(input("Ingrese curso a buscar: "))
                            for i in self.cursos:
                                if i.getAño()==k:
                                    print(i.getDocentes())
                                    print(i.getAlumnos())
                            print("\nPresione cualquier tecla para continuar...")
                            m()
                        elif opcion2==4:
                            os.system("cls")
                            print('\033[H\033[J', end='')
                            print("Alumnos con Actividad Extracurricular\n")
                            for i in self.cursos:
                                print(i.getAlumnosAct())
                            print("\nPresione cualquier tecla para continuar...")
                            m()
                        elif opcion2==5:
                            os.system("cls")
                            print('\033[H\033[J', end='')
                            print("Alumnos sin Actividad Extracurricular")
                            for i in self.cursos:
                                print(i.getAlumnosNoAct())
                            print("\nPresione cualquier tecla para continuar...")
                            m()
                elif opcion==4:
                    os.system("cls")
                    print('\033[H\033[J', end='')
                    print("Recaudacion Total: ")
                    recaud=0
                    for i in self.cursos:
                        recaud+=i.Recaudacion()
                    print(str(recaud))
                    print("\nPresione cualquier tecla para continuar...")
                    m()   

    def agregarCurso(self):
        self.cursos.append(Curso())
    def calcularRecaudacionCurso(self):
        rec=0
        if len(self.cursos)<1:
            pass
        else:
            n=int(input("Ingrese año del curso: "))
            for i in self.cursos:
                if i.getAño()==n:
                    rec=i.Recaudacion()
        return float(rec)
    def guardar(self):
        with open("Instituto.dat","wb") as archivo:
            dump(self.cursos,archivo)
        print("Datos guardados.")
    def cargar(self):
        try:
            with open("Instituto.dat","rb") as archivo:
                self.cursos=load(archivo)
        except:
            self.cursos=[]

app=GestionAcademica()