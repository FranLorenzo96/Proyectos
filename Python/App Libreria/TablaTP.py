import sqlite3

class tabla:

    def abrir(self):
        conexion=sqlite3.connect("tabla.db")
        return conexion

    def crear(self):
        conexion=self.abrir()
        try:
            conexion.execute("""create table tabla (codigo integer primary key AUTOINCREMENT, 
                                titulo text , autor text, edicion text, lugar text, editorial text, traduccion text, pag text, condicion text)""")
            #print("Tabla creada")
        except sqlite3.OperationalError:
            #print("tabla ya existente")
            pass

    def alta(self,datos):
        conexion=self.abrir()
        cursor=conexion.cursor()
        sql="insert into tabla (titulo,autor,edicion,lugar,editorial,traduccion,pag,condicion) values (?,?,?,?,?,?,?,?)"
        cursor.execute(sql,datos) #solo trabaja con tuplas (,)
        conexion.commit()
        conexion.close()

    def consultacondicion(self,datos):
        try:
            conexion=self.abrir()
            cursor=conexion.cursor()
            sql="select condicion from tabla where codigo=?"
            cursor.execute(sql,datos)
            return cursor.fetchall()
        finally:
            conexion.close()

    def consultaportitulo(self,datos):
        try:
            conexion=self.abrir()
            cursor=conexion.cursor()
            sql="select * from tabla where titulo=?"
            cursor.execute(sql,datos)
            return cursor.fetchall()
        finally:
            conexion.close()

    def consultaporcodigo(self,datos):
        try:
            conexion=self.abrir()
            cursor=conexion.cursor()
            sql="select * from tabla where codigo=?"
            cursor.execute(sql,datos)
            return cursor.fetchall()
        finally:
            conexion.close()

    def consultaTotal(self):
        try:
            conexion=self.abrir()
            cursor=conexion.cursor()
            sql="select * from tabla"
            cursor.execute(sql)
            return cursor.fetchall()
        finally:
            conexion.close()

    def eliminar(self,dato):
        try:
            conexion=self.abrir()
            cursor=conexion.cursor()
            sql="delete from tabla where codigo=?"
            cursor.execute(sql,dato)
            conexion.commit() #resetea la lista
        finally:
            conexion.close()

    def Modificar(self,dato):
        try:
            conexion=self.abrir()
            cursor=conexion.cursor()
            sql="update tabla set titulo=?,autor=?,edicion=?,lugar=?,editorial=?,traduccion=?,pag=? where codigo=?"
            cursor.execute(sql,dato) #dato tupla de 8 
            conexion.commit()
        finally:
            conexion.close()

    def Modificarcond(self,dato):
        try:
            conexion=self.abrir()
            cursor=conexion.cursor()
            sql="update tabla set condicion=? where codigo=?"
            cursor.execute(sql,dato) #dato tupla de 2 
            conexion.commit()
        finally:
            conexion.close()

    def consultaparareclamo(self,datos):
        try:
            conexion=self.abrir()
            cursor=conexion.cursor()
            sql="select codigo from tabla where condicion=?"
            cursor.execute(sql,datos)
            return cursor.fetchall()
        finally:
            conexion.close()

