from werkzeug import generate_password_hash, check_password_hash
from abc import ABC, abstractmethod

class User(ABC):
    def __init__(self, name, lastname, email, password):
        self.__password = password
        self.name = name
        self.lastname = lastname
        self.email = email
    
    def check_password(self, password):
        check_password_hash(self.password, password)
    
    @property
    def password(self):
        return self.password
    
    @password.setter 
    def password(self):
        self.password = generate_password_hash(self.password)
    