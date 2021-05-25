#!/usr/bin/python3

from config import config
from ai.reconocedor import Reconocedor
from ai.aumentador import Aumentador

aumentador = Aumentador()
reconocedor = Reconocedor(aumentador)

datos = reconocedor.iniciar_aumentacion()
datasets = reconocedor.crear_sets(datos, config["limitador"])

wait = input("End")
