#!/usr/bin/python3
from model.carta import Carta
from model.tipocarta import TipoCarta
from ai.reconocedor import Reconocedor
from ai.aumentador import Aumentador

aumentador = Aumentador()
reconocedor = Reconocedor(aumentador)

reconocedor.iniciar_aumentacion()

wait = input("End")