from modulos.interfaces import IModule
from random import randint

class BMP180(IModule):
    def __init__(self):
        self.active = True
       
    def read(self):
        return randint(0,100)
    
    def start(self):
        print("Iniciando {}".format(self.__class__))