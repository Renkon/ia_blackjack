#!/usr/bin/python3
import pathlib
import numpy as np
from threading import Thread
from sklearn.model_selection import train_test_split

from src.model.carta import Carta
from src.model.cartas import cartas
from src.ai.redneuronal import RedNeuronal


class Reconocedor:
    def __init__(self, aumentador):
        self.__aumentador = aumentador

    def iniciar_aumentacion(self):
        self.__aumentador.preparar_procesamiento(pathlib.Path(__file__).parent.parent / "imagenes")

        # Primera etapa: populamos con el augmentator imagenes para cada carta.
        for carta, path in cartas.items():
            print("Invocando data augmentator para carta " + str(carta))
            self.__aumentador.procesar_imagen(int(Carta.to_number(carta)), path)

        # Segunda etapa, shuffleamos
        print("Shuffleando lista de datos")
        self.__aumentador.barajar_datos()

        # Tercer etapa, obtener los datos
        print("Finalizando proceso de data augmentation")
        datos = self.__aumentador.obtener_datos()

        # Pero antes de retornarlo, hacemos un cleanup para que no se nos muera la ram
        self.__aumentador.limpiar_datos()

        return datos

    def crear_sets(self, datos, cantidad):
        print("Creando sets de datos")
        print("Usando en total " + str(len(datos)) + " imagenes")
        print("Usando " + str(cantidad) + " imagenes para entrenamiento")
        print("Usando " + str(int(cantidad * 0.1)) + " imagenes para pruebas")
        print("Usando " + str(int(cantidad * 0.1)) + " imagenes para validacion")

        # Cuarta etapa, separarlo en un set de entrenamiento, y otro de test.
        entrenamiento = datos[:cantidad]
        pruebas = datos[cantidad:int(cantidad * 1.1)]
        validaciones = datos[int(cantidad * 1.1):]

        x_entrenamiento = []
        y_entrenamiento = []
        x_pruebas = []
        y_pruebas = []
        x_validaciones = []
        y_validaciones = []

        # Poblamos los arrays asociados a entrenamiento
        for x in entrenamiento:
            x_entrenamiento.append(x[0])
            y_entrenamiento.append(x[1])

        # Poblamos los arrays asociados a pruebas
        for x in pruebas:
            x_pruebas.append(x[0])
            y_pruebas.append(x[1])

        # Poblamos los arrays asociados a validaciones
        for x in validaciones:
            x_validaciones.append(x[0])
            y_validaciones.append(x[1])

        # Transformamos en arrays de NumPy
        x_entrenamiento = np.array(x_entrenamiento)
        y_entrenamiento = np.array(y_entrenamiento)
        x_pruebas = np.array(x_pruebas)
        y_pruebas = np.array(y_pruebas)
        x_validaciones = np.array(x_validaciones)
        y_validaciones = np.array(y_validaciones)

        # Y finalmente retornamos los 6 arrays en una tupla.
        return x_entrenamiento, y_entrenamiento, x_pruebas, y_pruebas, x_validaciones, y_validaciones

    def procesar_sets(self, x_e, y_e, x_p, y_p, x_v, y_v, inputs, outputs, epochs, learn_rate):
        red = RedNeuronal(x_e, y_e, x_p, y_p, x_v, y_v)
        modelo = red.crear_modelo(inputs, outputs, learn_rate)
        red.entrenar(modelo, epochs)
