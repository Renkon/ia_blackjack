#!/usr/bin/python3

from model.cartas import cartas  

class Reconocedor:
    def __init__(self):
        pass

    def iniciar_aumentacion(self):
        for carta, path in cartas.items():
            print(str(carta) + str(path))
