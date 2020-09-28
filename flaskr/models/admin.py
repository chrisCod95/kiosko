from .user import User

class Admin(User):
    user_type = "admin"
    
    def __init__(self, name, lastname, email, password):
        super().__init__(self, name, lastname, email, password)
        
        self.user_type = cls.user_type