from enum import Enum

class TipoCarta(Enum):
    Corazones = 1,
    Picas = 2,
    Diamantes = 3,
    Trebol = 4,

    def __str__(self):
        if (self == TipoCarta.Corazones):   return "Corazones"
        elif (self == TipoCarta.Picas):     return "Picas"
        elif (self == TipoCarta.Diamantes): return "Diamantes"
        elif (self == TipoCarta.Trebol):    return "Trebol"
        else:                               raise TypeError(self)