import tkinter as tk
from tkinter import ttk,messagebox as mb,scrolledtext as st,PhotoImage
from tkinter.constants import CENTER, E, END, HORIZONTAL, N, S, W
import TablaTP
import TablaTP2
from datetime import datetime
#import os
#import base64
#import icon


""" Para convertir a .exe usando el cmd:
    1- cd "direcion" sin comillas
    2- pyinstaller --i "icono.ico" --windowed --onefile nombrearchivo.py"""

class Aplicacion:

    def __init__(self):

        self.conexion=TablaTP.tabla()
        self.conexion.crear()

        self.conexion2=TablaTP2.tabla()
        self.conexion2.crear()

        self.ventana=tk.Tk()
        self.ventana.title("Libreria")

        self.ventana.geometry("1200x470")

        self.ventana.resizable(0,0) #elimina boton maximizar

        #photo=PhotoImage(file="C:/Users/Usuario/Desktop/VsCode/Python/Modulo 2/icono.ico") #solo se usa para archivos .png o mas, no para .ico
        self.ventana.iconbitmap("C:/Users/Francisco/Desktop/VsCode/Python/Modulo 2/icono.ico") #solo para .ico

        self.cuaderno=ttk.Notebook(self.ventana)
        self.cuaderno.grid(column=0,row=0)

        #creacion del icono en archivo iconconverter.py y abajo llama al archivo creado

        #with open('tmp.ico','wb') as tmp:
        #    tmp.write(base64.b64decode(icon.Icon().img))
        #self.ventana.iconbitmap('tmp.ico')
        #os.remove('tmp.ico')

        self.Libros()
        self.Prestamos()
        self.control()
        self.botonactualizar()
        self.buscarid.set("")
        self.borrarlibro.set("")
        

        
        self.ventana.mainloop()

    def Libros(self):

        self.framelibros=ttk.Frame(self.cuaderno)
        self.cuaderno.add(self.framelibros,text="Libros")
        
    
        self.Agregarlibro()
        self.Modificarlibro()
        self.treetabla()
        self.Consulta()
        self.Eliminarlibro()

        

    def Agregarlibro(self):

        self.labelframe1=ttk.LabelFrame(self.framelibros,text="Agregar libro")
        self.labelframe1.grid(column=0,row=0)

        self.label8=ttk.Label(self.labelframe1,text="Condicion: ")
        self.label8.grid(column=0,row=8,padx=4,pady=0,sticky="nw")

        self.opcion2=tk.IntVar()

        #self.radiobutton3=ttk.Radiobutton(self.labelframe1,text="Prestamo en proceso",variable=self.opcion2,value=1)
        #self.radiobutton3.grid(column=1,row=8,padx=(0,50),pady=0,sticky="w")

        self.radiobutton4=ttk.Radiobutton(self.labelframe1,text="Disponible",variable=self.opcion2,value=2)
        self.radiobutton4.grid(column=1,row=9,padx=(0,50),pady=0,sticky="w")

        #self.radiobutton5=ttk.Radiobutton(self.labelframe1,text="Retraso",variable=self.opcion2,value=3)
        #self.radiobutton5.grid(column=1,row=10,padx=(0,50),pady=0,sticky="w")

        self.radiobutton6=ttk.Radiobutton(self.labelframe1,text="En restauracion",variable=self.opcion2,value=4)
        self.radiobutton6.grid(column=1,row=11,padx=(0,50),pady=0,sticky="w")

        self.label1=ttk.Label(self.labelframe1,text="Titulo: ")
        self.label1.grid(column=0,row=1,padx=4,pady=4,sticky="e")

        self.nombre=tk.StringVar()

        self.entry1=ttk.Entry(self.labelframe1,textvariable=self.nombre,width=25)
        self.entry1.grid(column=1,row=1,padx=4,pady=4,sticky="w")

        self.label2=ttk.Label(self.labelframe1,text="Autor: ")
        self.label2.grid(column=0,row=2,padx=4,pady=4,sticky="e")

        self.autor=tk.StringVar()

        self.entry2=ttk.Entry(self.labelframe1,textvariable=self.autor,width=25)
        self.entry2.grid(column=1,row=2,padx=4,pady=4,sticky="w")

        self.label3=ttk.Label(self.labelframe1,text="Edicion: ")
        self.label3.grid(column=0,row=3,padx=4,pady=4,sticky="e")

        self.edicion=tk.StringVar()

        self.entry3=ttk.Entry(self.labelframe1,textvariable=self.edicion,width=25)
        self.entry3.grid(column=1,row=3,padx=4,pady=4,sticky="w")

        self.label4=ttk.Label(self.labelframe1,text="Lugar de Impresion: ")
        self.label4.grid(column=0,row=4,padx=4,pady=4,sticky="e")

        self.lugar=tk.StringVar()

        self.entry4=ttk.Entry(self.labelframe1,textvariable=self.lugar,width=25)
        self.entry4.grid(column=1,row=4,padx=4,pady=4,sticky="w")

        self.label5=ttk.Label(self.labelframe1,text="Editorial: ")
        self.label5.grid(column=0,row=5,padx=4,pady=4,sticky="e")

        self.editorial=tk.StringVar()

        self.entry5=ttk.Entry(self.labelframe1,textvariable=self.editorial,width=25)
        self.entry5.grid(column=1,row=5,padx=4,pady=4,sticky="w")

        self.label6=ttk.Label(self.labelframe1,text="Traducido: ")
        self.label6.grid(column=0,row=6,padx=4,pady=4,sticky="e")

        self.opcion1=tk.IntVar()

        self.radiobutton1=ttk.Radiobutton(self.labelframe1,text="Traducido",variable=self.opcion1,value=1)
        self.radiobutton1.grid(column=1,row=6,padx=(0,50),pady=4,sticky="w")

        self.radiobutton2=ttk.Radiobutton(self.labelframe1,text="Sin traducir",variable=self.opcion1,value=2)
        self.radiobutton2.grid(column=1,row=6,padx=(80,5),pady=4,sticky="w")

        self.label7=ttk.Label(self.labelframe1,text="Cantidad de paginas: ")
        self.label7.grid(column=0,row=7,padx=4,pady=4,sticky="e")

        self.cantpag=tk.StringVar()

        self.entry6=ttk.Entry(self.labelframe1,textvariable=self.cantpag,width=6)
        self.entry6.grid(column=1,row=7,padx=4,pady=4,sticky="w")

        self.boton1=ttk.Button(self.labelframe1,text="Guardar",command=self.guardarlibro)
        self.boton1.grid(column=0,row=12,padx=4,pady=10,columnspan=2)

    def guardarlibro(self):

        if self.opcion1.get() == 1:
            self.trad1=("Si")
        else:
            self.trad1=("No")

        if self.opcion2.get() == 1:
            self.cond=("Prestamo")
        elif self.opcion2.get()==2:
            self.cond=("Disponible")
        elif self.opcion2.get()==3:
            self.cond=("Retraso")
        elif self.opcion2.get()==4:
            self.cond=("Restauracion")
        
        datos=(self.nombre.get(),self.autor.get(),self.edicion.get(),self.lugar.get(),self.editorial.get(),self.trad1,self.cantpag.get(),self.cond)
        self.conexion.alta(datos)
        mb.showinfo("Libro","El libro fue cargado exitosamente")
        self.nombre.set("")
        self.autor.set("")
        self.edicion.set("")
        self.lugar.set("")
        self.editorial.set("")
        self.opcion1.set("")
        self.cantpag.set("")
        self.opcion2.set("")
        self.trad1=""
        self.cond=""



    def Modificarlibro(self):

        self.labelframe2=ttk.LabelFrame(self.framelibros,text="Modificar libro")
        self.labelframe2.grid(column=1,row=0,sticky="nw")

        self.label9=ttk.Label(self.labelframe2,text="Ingrese id del libro a modificar: ")
        self.label9.grid(column=0,row=1,padx=4,pady=4,sticky="e")

        self.buscarid=tk.IntVar()

        self.entry7=ttk.Entry(self.labelframe2,textvariable=self.buscarid,width=6)
        self.entry7.grid(column=1,row=1,padx=4,pady=8,sticky="w")

        self.sep1=ttk.Separator(self.labelframe2,orient="horizontal")
        self.sep1.grid(column=0,row=2,columnspan=4,sticky="we")

        self.label10=ttk.Label(self.labelframe2,text="Modificar: ")
        self.label10.grid(column=0,row=3,padx=8,pady=8)

        self.label1=ttk.Label(self.labelframe2,text="Titulo: ")
        self.label1.grid(column=0,row=4,padx=4,pady=4,sticky="e")

        self.nombremod=tk.StringVar()

        self.entry1=ttk.Entry(self.labelframe2,textvariable=self.nombremod,width=25)
        self.entry1.grid(column=1,row=4,padx=4,pady=4,sticky="w")

        self.label2=ttk.Label(self.labelframe2,text="Autor: ")
        self.label2.grid(column=0,row=5,padx=4,pady=4,sticky="e")

        self.autormod=tk.StringVar()

        self.entry2=ttk.Entry(self.labelframe2,textvariable=self.autormod,width=25)
        self.entry2.grid(column=1,row=5,padx=4,pady=4,sticky="w")

        self.label3=ttk.Label(self.labelframe2,text="Edicion: ")
        self.label3.grid(column=0,row=6,padx=4,pady=4,sticky="e")

        self.edicionmod=tk.StringVar()

        self.entry3=ttk.Entry(self.labelframe2,textvariable=self.edicionmod,width=25)
        self.entry3.grid(column=1,row=6,padx=4,pady=4,sticky="w")

        self.label4=ttk.Label(self.labelframe2,text="Lugar de Impresion: ")
        self.label4.grid(column=0,row=7,padx=4,pady=4,sticky="e")

        self.lugarmod=tk.StringVar()

        self.entry4=ttk.Entry(self.labelframe2,textvariable=self.lugarmod,width=25)
        self.entry4.grid(column=1,row=7,padx=4,pady=4,sticky="w")

        self.label5=ttk.Label(self.labelframe2,text="Editorial: ")
        self.label5.grid(column=0,row=8,padx=4,pady=4,sticky="e")

        self.editorialmod=tk.StringVar()

        self.entry5=ttk.Entry(self.labelframe2,textvariable=self.editorialmod,width=25)
        self.entry5.grid(column=1,row=8,padx=4,pady=4,sticky="w")

        self.label6=ttk.Label(self.labelframe2,text="Traducido: ")
        self.label6.grid(column=0,row=9,padx=4,pady=4,sticky="e")

        self.opcion3=tk.IntVar()

        self.radiobutton1=ttk.Radiobutton(self.labelframe2,text="Traducido",variable=self.opcion3,value=1)
        self.radiobutton1.grid(column=1,row=9,padx=(0,50),pady=4,sticky="w")

        self.radiobutton2=ttk.Radiobutton(self.labelframe2,text="Sin traducir",variable=self.opcion3,value=2)
        self.radiobutton2.grid(column=1,row=9,padx=(80,5),pady=4,sticky="w")

        self.label7=ttk.Label(self.labelframe2,text="Cantidad de paginas: ")
        self.label7.grid(column=0,row=10,padx=4,pady=4,sticky="e")

        self.cantpagmod=tk.StringVar()

        self.entry6=ttk.Entry(self.labelframe2,textvariable=self.cantpagmod,width=6)
        self.entry6.grid(column=1,row=10,padx=4,pady=4,sticky="w")

        self.boton2=ttk.Button(self.labelframe2,text="Modificar",command=self.modificarboton)
        self.boton2.grid(column=0,row=11,padx=4,pady=15,columnspan=2)

        self.label13=ttk.Label(self.labelframe2,text="Modificar condicion:")
        self.label13.grid(column=3,row=3,padx=8,pady=8)

        self.opcioncond=tk.IntVar()

        #self.radiobutton7=ttk.Radiobutton(self.labelframe2,text="Prestamo en proceso",variable=self.opcioncond,value=1)
        #self.radiobutton7.grid(column=3,row=4,padx=(50,0),pady=0,sticky="w")

        self.radiobutton8=ttk.Radiobutton(self.labelframe2,text="Disponible",variable=self.opcioncond,value=2)
        self.radiobutton8.grid(column=3,row=4,padx=(50,5),pady=0,sticky="w")

        #self.radiobutton9=ttk.Radiobutton(self.labelframe2,text="Retraso",variable=self.opcioncond,value=3)
        #self.radiobutton9.grid(column=3,row=6,padx=(50,0),pady=0,sticky="w")

        self.radiobutton10=ttk.Radiobutton(self.labelframe2,text="En restauracion",variable=self.opcioncond,value=4)
        self.radiobutton10.grid(column=3,row=5,padx=(50,5),pady=0,sticky="w")

        self.boton4=ttk.Button(self.labelframe2,text="Modificar",command=self.modificarcond)
        self.boton4.grid(column=3,row=6,columnspan=2)

    def modificarboton(self):

        Qask=mb.askyesno("Modificar","Esta seguro que quiere modificar los datos del libro?")

        if self.opcion3.get()==1:
            self.trad2="Si"
        elif self.opcion3.get()==2:
            self.trad2="No"

        if Qask==True:
        
            datos=(self.nombremod.get(),self.autormod.get(),self.edicionmod.get(),self.lugarmod.get(),self.editorialmod.get(), self.trad2 ,self.cantpagmod.get(),self.buscarid.get())
            respuesta=self.conexion.consultaporcodigo((self.buscarid.get(),))
            
            if len(respuesta)==0:
                mb.showwarning("Modificar","El id que introdujo no se encuentra en la base de datos")
            else:
                self.conexion.Modificar(datos)
                self.nombremod.set("")
                self.autormod.set("")
                self.edicionmod.set("")
                self.lugarmod.set("")
                self.editorialmod.set("")
                self.opcion3.set("")
                self.cantpagmod.set("")
                self.trad2=""

    def modificarcond(self):
        Qask=mb.askyesno("Modificar","Esta seguro que quiere modificar la condicion del libro?")
        if Qask==True:

            if self.opcioncond.get() == 1:
                self.cond=("Prestamo")
            elif self.opcioncond.get()==2:
                self.cond=("Disponible")
            elif self.opcioncond.get()==3:
                self.cond=("Retraso")
            elif self.opcioncond.get()==4:
                self.cond=("Restauracion")

            dato=(self.cond,self.buscarid.get())
            respuesta=self.conexion.consultaporcodigo((self.buscarid.get(),))

            if len(respuesta)==0:
                mb.showwarning("Modificar","El id que introdujo no se encuentra en la base de datos")
            else:
                self.conexion.Modificarcond(dato)
                self.opcioncond.set("")
                self.cond=""

            
            

                   

            

    def treetabla(self):

        self.labelframe3=ttk.Frame(self.ventana)
        self.labelframe3.grid(column=3,row=0,rowspan=3)



        s = ttk.Style()
        s.configure('Treeview', rowheight=33,borderwidth=0,relief = 'flat')  #modifica el primer frame (?)
        s.layout("Treeview", [('Treeview.treearea', {'sticky': 'nswe'})])  #elimina la linea q rodea el treeview (se bugea)

        columns=("0","1","2","3","4","5","6","7","8")

        self.tree=ttk.Treeview(self.labelframe3,columns=columns)
        self.tree.grid(column=0,row=0,padx=4,pady=25,ipadx=50,columnspan=3,rowspan=8,sticky=(N,S))

        self.tree["show"]="headings"

        self.tree.heading("0",text="Id",anchor=W)
        self.tree.heading("1",text="Titulo",anchor=W)
        self.tree.heading("2",text="Autor",anchor=W)
        self.tree.heading("3",text="Edicion",anchor=W)
        self.tree.heading("4",text="Lugar de Impresion",anchor=W)
        self.tree.heading("5",text="Editorial",anchor=W)
        self.tree.heading("6",text="Traducido",anchor=W)
        self.tree.heading("7",text="Cant. de Paginas",anchor=W)
        self.tree.heading("8",text="Condicion",anchor=W)

        #TRUCAZO --> poner las columnas que se van por fuera del GUI con width=0 y minwidth=120
        #ancho del treeview lo haces con ipadx

        self.tree.column("0",minwidth=30,stretch=True,width=30)
        self.tree.column("1",minwidth=120,stretch=True,width=120)
        self.tree.column("2",minwidth=120,stretch=True,width=120)
        self.tree.column("3",width=0,stretch=True,minwidth=120)
        self.tree.column("4",width=0,stretch=True,minwidth=120)
        self.tree.column("5",width=0,stretch=True,minwidth=120)
        self.tree.column("6",width=0,stretch=True,minwidth=120)
        self.tree.column("7",width=0,stretch=True,minwidth=120)
        self.tree.column("8",width=0,stretch=True,minwidth=120)

        self.labelframe3.columnconfigure(0,weight=1)
        self.labelframe3.columnconfigure(1,weight=1)
        self.labelframe3.rowconfigure(0,weight=1)
        self.labelframe3.rowconfigure(1,weight=1)

        self.scrollbar=ttk.Scrollbar(self.labelframe3,orient=HORIZONTAL,command=self.tree.xview)
        self.scrollbar.grid(column=0,row=2,sticky="we",columnspan=2)

        self.tree.configure(xscrollcommand=self.scrollbar.set)
        #self.canvas.create_window((0,0), window=self.frame, anchor="s")

        

        self.botontree=ttk.Button(self.labelframe3,text="Actualizar",command=self.botonactualizar)
        self.botontree.grid(column=0,row=10,pady=8,columnspan=2,sticky="s")



    def botonactualizar(self):

        lista=self.conexion.consultaTotal()
        for i in self.tree.get_children():
            self.tree.delete(i)
        for i in lista:
            self.tree.insert("",END,values=i)
        self.control()

    def Consulta(self):
        self.labelframe4=ttk.LabelFrame(self.framelibros,text="Buscar Libro")
        self.labelframe4.grid(column=0,row=1,sticky="nwe")

        self.label11=ttk.Label(self.labelframe4,text="Ingrese titulo del libro: ")
        self.label11.grid(column=0,row=2,pady=4,padx=4,sticky="e")

        self.buscarlibro=tk.StringVar()

        self.entry8=ttk.Entry(self.labelframe4,textvariable=self.buscarlibro)
        self.entry8.grid(column=1,row=2,padx=4,pady=4,sticky="w")

        self.botonconsulta=ttk.Button(self.labelframe4,text="Buscar",command=self.botonconsulta)
        self.botonconsulta.grid(column=0,row=3,columnspan=2)

    def botonconsulta(self):
        
        dato=self.buscarlibro.get()
        tabla=self.conexion.consultaTotal()

        for i in self.tree.get_children():    #borra lista de datos
            self.tree.delete(i)

        for j in range(len(tabla)):             #busca por letra, no nombre completo
            if dato in tabla[j][1]:
                self.tree.insert("",END,values=tabla[j])
                
                    


    def Eliminarlibro(self):

        self.labelframe5=ttk.LabelFrame(self.framelibros,text="Eliminar libro")
        self.labelframe5.grid(column=1,row=1,sticky="nwes")

        self.label12=ttk.Label(self.labelframe5,text="Ingrese Id del libro: ")
        self.label12.grid(column=0,row=2,padx=4,pady=8,sticky="e")

        self.borrarlibro=tk.IntVar()

        self.entry9=ttk.Entry(self.labelframe5,textvariable=self.borrarlibro,width=6)
        self.entry9.grid(column=1,row=2,padx=4,pady=8,sticky="w")

        self.boton3=ttk.Button(self.labelframe5,text="Borrar",command=self.botonborrar)
        self.boton3.grid(column=3,row=2,sticky="e",padx=(50,0))

    def botonborrar(self):
           
        Qask=mb.askyesno("Borrar","Esta seguro que quiere eliminar el libro?")

        if Qask==True:
            libro=self.conexion.consultaporcodigo((self.borrarlibro.get(),))
            if len(libro)==0:
                mb.showwarning("Borrar","No existe libro con ese Id")
            else:
                dato=(self.borrarlibro.get(),)
                self.conexion.eliminar(dato)


    def Prestamos(self):

        self.framelibros2=ttk.Frame(self.cuaderno)
        self.cuaderno.add(self.framelibros2,text="Prestamos")
        self.registrar()
        self.terminarprestamo()
        self.reclamar()

    def registrar(self):

        self.labelframe6=ttk.LabelFrame(self.framelibros2,text="Registrar Prestamo")
        self.labelframe6.grid(column=0,row=0,sticky="nswe")

        self.label15=ttk.Label(self.labelframe6,text="Ingrese nombre del cliente: ")
        self.label15.grid(column=0,row=1,padx=4,pady=4,sticky="e")

        self.label16=ttk.Label(self.labelframe6,text="Ingrese telefono: ")
        self.label16.grid(column=0,row=2,padx=4,pady=4,sticky="e")

        self.label17=ttk.Label(self.labelframe6,text="Ingrese mail: ")
        self.label17.grid(column=0,row=3,padx=4,pady=4,sticky="e")

        self.label18=ttk.Label(self.labelframe6,text="Ingrese fecha de retiro (dd/mm/aaaa): ")
        self.label18.grid(column=0,row=4,padx=4,pady=4,sticky="e")

        self.label19=ttk.Label(self.labelframe6,text="Ingrese fecha de devolucion (dd/mm/aaaa): ")
        self.label19.grid(column=0,row=5,padx=4,pady=4,sticky="e")

        self.label20=ttk.Label(self.labelframe6,text="Ingrese id de libro: ")
        self.label20.grid(column=0,row=6,padx=4,pady=4,sticky="e")

        self.nombrecliente=tk.StringVar()

        self.entry14=ttk.Entry(self.labelframe6,textvariable=self.nombrecliente)
        self.entry14.grid(column=1,row=1,sticky="w",padx=4)

        self.telefono=tk.StringVar()

        self.entry15=ttk.Entry(self.labelframe6,textvariable=self.telefono)
        self.entry15.grid(column=1,row=2,sticky="w",padx=4)

        self.mail=tk.StringVar()

        self.entry16=ttk.Entry(self.labelframe6,textvariable=self.mail)
        self.entry16.grid(column=1,row=3,sticky="w",padx=4)

        self.fechaini=tk.StringVar()

        self.entry17=ttk.Entry(self.labelframe6,textvariable=self.fechaini,width=12)
        self.entry17.grid(column=1,row=4,sticky="w",padx=4)

        self.fechafin=tk.StringVar()

        self.entry18=ttk.Entry(self.labelframe6,textvariable=self.fechafin,width=12)
        self.entry18.grid(column=1,row=5,sticky="w",padx=4)

        self.idprestamo=tk.StringVar()

        self.entry19=ttk.Entry(self.labelframe6,textvariable=self.idprestamo,width=6)
        self.entry19.grid(column=1,row=6,sticky="w",padx=4)

        self.boton5=ttk.Button(self.labelframe6,text="Prestar",command=self.botonprestar)
        self.boton5.grid(column=0,row=7,padx=8,pady=8,columnspan=2)

    def botonprestar(self):

        lista=self.conexion.consultaporcodigo((self.idprestamo.get(),))
        if lista[0][8]=="Disponible":


            self.estadoprestamo="En forma"
            datos=(self.nombrecliente.get(),self.telefono.get(),self.mail.get(),self.fechaini.get(),self.fechafin.get(),self.idprestamo.get(),self.estadoprestamo)
            self.conexion2.alta(datos)
            datos2=("Prestamo",self.idprestamo.get())
            self.conexion.Modificarcond(datos2)
            mb.showinfo("Prestamo","Prestamo realizado")
        else:
            mb.showwarning("Prestamo",f"No puede realizarse la prestacion, libro en {lista[0][8]}")
    
    def terminarprestamo(self):

        self.labelframe7=ttk.LabelFrame(self.framelibros2,text="Entrega")
        self.labelframe7.grid(column=0,row=1,sticky="nsew")

        self.label21=ttk.Label(self.labelframe7,text="Ingrese id de libro: ")
        self.label21.grid(column=0,row=1,padx=4,pady=4,sticky="e")

        self.idterpres=tk.StringVar()

        self.entry20=ttk.Entry(self.labelframe7,textvariable=self.idterpres,width=6)
        self.entry20.grid(column=1,row=1,sticky="w")

        self.label22=ttk.Label(self.labelframe7,text="Se eliminara \n el registro de entrega \n una vez devuelto \n el libro")
        self.label22.grid(column=3,row=1,rowspan=3,padx=8)

        self.boton6=ttk.Button(self.labelframe7,text="Entregar",command=self.botonterpres)
        self.boton6.grid(column=0,row=2,columnspan=2,pady=8)

    def botonterpres(self):  #Modifico lista 1 y borro la prestacion de lista 2

        consulta=self.conexion.consultacondicion(self.idterpres.get(),)
        
        if consulta[0][0] == "Prestamo" or consulta[0][0] == "Retraso":

            dato=("Disponible",self.idterpres.get())
            self.conexion.Modificarcond(dato)

            dato2=(self.conexion2.consultaporid(self.idterpres.get()),) #codigo tabla 2
            if len(dato2)==0:
                mb.showinfo("Entrega","No hay registro de prestacion")
            else:

                self.conexion2.eliminarporid(self.idterpres.get(),)
                mb.showinfo("Entrega","El libro fue devuelto")
        
        else:

            mb.showwarning("Entrega","El libro no se encontraba en prestacion")

    def control(self):

        fecha=datetime.now()
        año=fecha.year
        mes=fecha.month
        dia=fecha.day
        consulta=self.conexion2.consultaTotal()
        for i in range(len(consulta)):
            dato=consulta[i][5]
            lista=dato.split(sep="/")
            codigo=self.conexion2.consultacodigo((consulta[i][0],))
            if int(lista[2]) <= año and int(lista[1]) <= mes and int(lista[0]) <= dia:

                self.conexion.Modificarcond(("Retraso",codigo[0][0]))
                 
            

    def reclamar(self):

        self.labelframe8=ttk.LabelFrame(self.framelibros2,text="Reclamo por fuera de entrega")
        self.labelframe8.grid(column=0,row=3,sticky="nswe",ipady=20)

        self.label23=ttk.Label(self.labelframe8,text="Deteccion de prestacion fuera de fecha")
        self.label23.grid(column=0,row=1,padx=4,pady=4)

        self.boton7=ttk.Button(self.labelframe8,text="Buscar",command=self.reclamarboton)
        self.boton7.grid(column=0,row=2,columnspan=2)

    def reclamarboton(self):

        lista=self.conexion.consultaTotal()
        string=""

        for j in range(len(lista)):
            if lista[j][8] == "Retraso":
                #codigolista2=self.conexion2.consultaporid((lista[j][0],))
                fila=self.conexion2.consultabotonreclamo((lista[j][0],))
                string+="La persona "+fila[0][1]+" con tel:"+fila[0][2]+" y con mail:"+fila[0][3]+" debe el libro con id: "+fila[0][6]+"\n"

        if len(string)>0:       
            mb.showinfo("Reclamo",string)  
        else:
            mb.showinfo("Reclamo","Ninguna persona debe")


app=Aplicacion()
