#!/usr/bin/python3

class Carta:
    def __init__(self, numero, tipo):
        self.numero = numero
        self.tipo = tipo
    
    def __str__(self):
        return str(self.numero) + " de " + str(self.tipo)

    def __hash__(self):
        return hash((self.numero, self.tipo))

    def __eq__(self, other):
        return (self.numero, self.tipo) == (other.numero, other.tipo)

    def __ne__(self, other):
        return not(self == other)
