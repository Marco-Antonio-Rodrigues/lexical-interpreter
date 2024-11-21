from Consts import Consts
from Token import Token
from Error import Error
class Lexer:
    def __init__(self, source_code):
        self.code = source_code
        self.current = None
        self.indice, self.coluna, self.linha = -1, -1, 0
        self.__advance()
    def __advance(self):
        self.__advanceCalc(self.current)

    def __advanceCalc(self, _char=None):
        return self
    
    def makeTokens(self):
        tokens = []
        while self.current != None:
            self.current = None

        tokens.append(Token(Consts.EOF))
        return tokens, None

    def __makeNumber(self):
        return Token(Consts.FLOAT, float("2024"))

