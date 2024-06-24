class Metodos():
    @classmethod
    def insert(self,db,producto):
        try:
            cur=db.cursor()
            cur.execute("INSERT INTO productos(image) VALUES(%s)",(producto,))
            db.commit()
            return "ingresado"
        except Exception as e:
            print(e)
            return "Ocurrio un error al insertar"
    @classmethod
    def select(self,db,producto):
        try:
            cur=db.cursor()
            cur.execute("SELECT * FROM productos WHERE image LIKE %s",(f"{producto}%",))
            resu=cur.fetchall()
            return (resu)
        except Exception as e:
            print(e)
            return "Ocurrio un error al seleccionar"
