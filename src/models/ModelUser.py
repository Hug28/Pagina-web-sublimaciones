from .User import User

class ModelUser():
    @classmethod
    def login(self,db,user):
        try:
            cur=db.cursor()
            cur.execute("SELECT id,name,password FROM login WHERE name = %s ",(user.name,))
            resu=cur.fetchone()
            if resu !=None:
                user=User(resu[0],resu[1],User.chek_password(resu[2],user.password))
                return user
            else:
                return None

        except Exception as e:
            print("error")
            raise Exception(e)
        
    @classmethod
    def get_by_id(self,db,id):
        try:
            cur=db.cursor()
            cur.execute("SELECT id,name FROM login WHERE id = %s ",(id,))
            resu=cur.fetchone()
            if resu !=None:
                return User(resu[0],None,resu[1])   
            else:
                return None

        except Exception as e:
            print("error")
            raise Exception(e)
        
