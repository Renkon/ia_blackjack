#!/usr/bin/python3

from enum import IntEnum

class TipoCarta(IntEnum):
    Corazones = 1,
    Diamantes = 2,
    Picas = 3,
    Trebol = 4,

    def __str__(self):
        if self == TipoCarta.Corazones:   return "Corazones"
        elif self == TipoCarta.Diamantes: return "Diamantes"
        elif self == TipoCarta.Picas:     return "Picas"
        elif self == TipoCarta.Trebol:    return "Trebol"
        else:                             raise TypeError(self)
