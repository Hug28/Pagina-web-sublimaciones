from werkzeug.security import check_password_hash
from flask_login import UserMixin

class User(UserMixin):
    def __init__(self,id,name,password) -> None:
        self.id=id
        self.name=name
        self.password=password

    @classmethod
    def chek_password(self,hashed_password,password):
        return check_password_hash(hashed_password,password)

