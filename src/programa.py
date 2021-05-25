#!/usr/bin/python3
from model.carta import Carta
from model.tipocarta import TipoCarta
from ai.reconocedor import Reconocedor

carta = Carta(3, TipoCarta.Diamantes)

print(str(carta))

Reconocedor().iniciar_aumentacion()
