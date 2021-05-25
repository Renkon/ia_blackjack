#!/usr/bin/python3
from model.carta import Carta
from model.tipocarta import TipoCarta
from ai.reconocedor import Reconocedor
from ai.aumentador import Aumentador

aumentador = Aumentador()
reconocedor = Reconocedor(aumentador)

datos = reconocedor.iniciar_aumentacion()
datasets = reconocedor.crear_sets(datos, 50000)

wait = input("End")