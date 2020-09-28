from user import User

class Owner(User):
    user_type = "owner"
    
    def __init__(self, name, lastname, email, password):
        super().__init__(self, name, lastname, email, password)
        
        self.user_type = cls.user_type
        
newOwner = Owner('chris', 'gials', 'chris@mail.com', 'claro123')

print(newOwner.__dict___)
