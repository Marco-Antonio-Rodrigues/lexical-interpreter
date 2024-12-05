from app.Consts import Consts
from app.Error import Error

""" i é int
 E-> iK
 K -> +iK
 K -> 
"""
class RecDescendente:
    def __init__(self, toks):
        self.tokens = toks
        self.id = -1
        self.current = None
        self.txt = ''
    def start(self): 
        return "OK:", None
