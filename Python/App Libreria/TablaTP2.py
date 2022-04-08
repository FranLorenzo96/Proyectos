import sqlite3

class tabla:

    def abrir(self):
        conexion=sqlite3.connect("tabla2.db")
        return conexion

    def crear(self):
        conexion=self.abrir()
        try:
            conexion.execute("""create table tabla2 (codigo integer primary key AUTOINCREMENT, 
                                nombre text , tel text, mail text, fechaini text, fechafin text, libroid text,estado text)""")
            #print("Tabla creada")
        except sqlite3.OperationalError:
            #print("tabla ya existente")
            pass

    def alta(self,datos):
        conexion=self.abrir()
        cursor=conexion.cursor()
        sql="insert into tabla2 (nombre,tel,mail,fechaini,fechafin,libroid,estado) values (?,?,?,?,?,?,?)"
        cursor.execute(sql,datos) #solo trabaja con tuplas (,)
        conexion.commit()
        conexion.close()

    def eliminarporid(self,dato):
        try:
            conexion=self.abrir()
            cursor=conexion.cursor()
            sql="delete from tabla2 where libroid=?"
            cursor.execute(sql,dato)
            conexion.commit() #resetea la lista
        finally:
            conexion.close()

    def consultaporid(self,datos):
        try:
            conexion=self.abrir()
            cursor=conexion.cursor()
            sql="select codigo from tabla2 where libroid=?"
            cursor.execute(sql,datos)
            return cursor.fetchall()
        finally:
            conexion.close()
    
    def consultaTotal(self):
        try:
            conexion=self.abrir()
            cursor=conexion.cursor()
            sql="select * from tabla2"
            cursor.execute(sql)
            return cursor.fetchall()
        finally:
            conexion.close()

    def consultacodigo(self,datos):
        try:
            conexion=self.abrir()
            cursor=conexion.cursor()
            sql="select libroid from tabla2 where codigo=?"
            cursor.execute(sql,datos)
            return cursor.fetchall()
        finally:
            conexion.close()

    def consultabotonreclamo(self,datos):
        try:
            conexion=self.abrir()
            cursor=conexion.cursor()
            sql="select * from tabla2 where libroid=?"
            cursor.execute(sql,datos)
            return cursor.fetchall()
        finally:
            conexion.close()




