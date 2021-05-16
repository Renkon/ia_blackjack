class Carta:
    def __init__(self, numero, tipo):
        self.numero = numero
        self.tipo = tipo
    
    def getNumero(self):
        return self.numero
    
    def getTipo(self):
        return self.tipo
    
    def __str__(self):
        return str(self.numero) + " de " + str(self.tipo)