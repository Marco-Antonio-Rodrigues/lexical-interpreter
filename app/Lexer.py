from app.Consts import Consts
from app.Token import Token
from app.Error import Error

class Lexer:
    def __init__(self, source_code):
        self.code = source_code
        self.current = None
        self.indice, self.coluna, self.linha = -1, -1, 0
        self.__advance()
        
    def __advance(self):
        self.__advanceCalc()
        self.current = self.code[self.indice] if self.indice < len(self.code) else None
        

    def __advanceCalc(self):
        self.indice += 1
        self.coluna += 1 
        if self.current == '\n':
            self.linha += 1
            self.coluna = 0
        return self
    
    def makeTokens(self):
        tokens = []
        while self.current != None:
            if self.current in ' \t':
                self.__advance()
            elif self.current == Consts.PLUS:
                tokens.append(Token(Consts.PLUS))
                self.__advance()
            elif self.current == Consts.MINUS:
                tokens.append(Token(Consts.MINUS))
                self.__advance()
            elif self.current in Consts.DIGITOS:
                tokens.append(self.__makeNumber())
            elif self.current in Consts.LETRAS + Consts.UNDER:
                tokens.append(self.__makeId())
            elif self.current == '"':
                tokens.append(self.__makeString())
            
            else: #erro
                self.__advance()
                return [], Error(f"{Error.lexerError}: lex-symbol '{self.current}' fail!")

        tokens.append(Token(Consts.EOF))
        return tokens, None

    def __makeNumber(self):
        strNum = ''
        conta_ponto = 0
        while self.current != None and self.current in Consts.DIGITOS + '.':
            if self.current == '.':
                if conta_ponto >= 1: break
                conta_ponto += 1
            strNum += self.current
            self.__advance()
        if conta_ponto == 0:
            return Token(Consts.INT, int(strNum))
        self.__advance()
        return Token(Consts.FLOAT, float(strNum))
    
    def __makeId(self):
        lexema = ''
        while self.current != None and self.current in Consts.LETRAS_DIGITOS+Consts.UNDER:
            lexema += self.current
            self.__advance()
        tokType = Consts.KEY if lexema in Consts.KEYS else Consts.ID
        return Token(tokType, lexema)
    
    def __makeString(self):
        stri = ''
        lookhead = False
        self.__advance()
        while self.current != None and self.current != '"' or lookhead:
            if lookhead:
                stri = stri + self.current
                lookhead = False
            elif self.current == '\\':
                lookhead = True
            else:
                stri = stri + self.current
            self.__advance()
        self.__advance()
        return Token(Consts.STRING, stri)
        