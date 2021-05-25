#!/usr/bin/python3

from model.cartas import cartas  

class Reconocedor:
    def __init__(self, aumentador):
        self.__aumentador = aumentador

    def iniciar_aumentacion(self):
        for carta, path in cartas.items():
            print("Invocando data augmentator para carta " + str(carta))
            self.__aumentador.procesar_imagen(carta, path)