#!/usr/bin/python3

import numpy as np
from threading import Thread
from src.model.cartas import cartas
from src.ai.redneuronal import RedNeuronal


class Reconocedor:
    def __init__(self, aumentador):
        self.__aumentador = aumentador

    def iniciar_aumentacion(self):
        # Primera etapa: populamos con el augmentator imagenes para cada carta.
        for carta, path in cartas.items():
            print("Invocando data augmentator para carta " + str(carta))
            self.__aumentador.procesar_imagen(carta, path)

        # Segunda etapa, shuffleamos
        print("Shuffleando lista de datos")
        self.__aumentador.barajar_datos()

        # Tercer etapa, obtener los datos
        print("Finalizando proceso de data augmentation")
        return self.__aumentador.obtener_datos()

    def crear_sets(self, datos, limitador):
        print("Creando sets de datos")
        print("Usando en total " + str(len(datos)) + " imagenes")
        print("Usando " + str(limitador) + " imagenes para entrenamiento")
        print("Usando " + str(len(datos) - limitador) + " imagenes para pruebas")
        # Cuarta etapa, separarlo en un set de entrenamiento, y otro de test.
        entrenamiento = datos[:limitador]
        pruebas = datos[limitador:]

        x_entrenamiento = []
        y_entrenamiento = []
        x_pruebas = []
        y_pruebas = []

        # Poblamos los arrays asociados a entrenamiento
        for x in entrenamiento:
            x_entrenamiento.append(x[0])
            y_entrenamiento.append(x[1])
        
        # Poblamos los arrays asociados a pruebas
        for x in pruebas:
            x_pruebas.append(x[0])
            y_pruebas.append(x[1])
        
        # Transformamos en arrays de NumPy
        x_entrenamiento = np.array(x_entrenamiento)
        y_entrenamiento = np.array(y_entrenamiento)
        x_pruebas = np.array(x_pruebas)
        y_pruebas = np.array(y_pruebas)

        # Y finalmente retornamos los 4 arrays en una tupla.
        return x_entrenamiento, y_entrenamiento, x_pruebas, y_pruebas

    def procesar_sets(self, x_e, y_e, x_p, y_p, inputs, outputs, epochs):
        red = RedNeuronal(x_e, y_e, x_p, y_p)
        red.crear_modelo(inputs, outputs, epochs)