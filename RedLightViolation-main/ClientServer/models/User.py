class User:
    def __init__(self, idUser = None, username = None, password = None, fullname = None, email = None, tel = None):
        self.idUser = idUser
        self.username = username
        self.password = password
        self.fullname = fullname
        self.email = email
        self.tel = tel

    def get_idUser(self):
        return self.idUser
    
    def set_idUser(self, idUser):
        self.idUser = idUser
    
    def get_username(self):
        return self.username
    
    def set_username(self, username):
        self.username = username   

    def get_password(self):
        return self.password
    
    def set_password(self, password):
        self.password = password

    def get_fullname(self):
        return self.fullname
    
    def set_fullname(self, fullname):
        self.fullname = fullname
    
    def get_email(self):
        return self.email
    
    def set_email(self, email):
        self.email = email

    def get_tel(self):
        return self.tel
    
    def set_tel(self, tel):
        self.tel = tel
        