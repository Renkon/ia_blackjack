#!/usr/bin/python3

class RedNeuronal:
    def __init__(self, x_e, y_e, x_p, y_p):
        self.__x_e = x_e
        self.__y_e = y_e
        self.__x_p = x_p
        self.__y_p = y_p

    def crear_modelo(self, inputs, outputs, epochs):
        # Modelo con tres layers ocultos.
        hidden1 = inputs // 4
        hidden2 = inputs // 16
        hidden3 = inputs // 64
        print("Se creara una RNA multiperceptrón con backpropagation")
        print("Estructura: " + str(inputs) + " | " + str(hidden1) + " | " + str(hidden2) + " | " + str(hidden3) + " | " + str(outputs) + " con Softmax")
