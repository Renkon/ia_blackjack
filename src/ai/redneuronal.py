#!/usr/bin/python3

import tensorflow as tf
from keras.utils.vis_utils import plot_model
from tensorflow.keras.layers import Input, Dense
from tensorflow.keras import Model

class RedNeuronal:
    def __init__(self, x_e, y_e, x_p, y_p, x_v, y_v):
        self.__x_e = x_e
        self.__y_e = y_e
        self.__x_p = x_p
        self.__y_p = y_p
        self.__x_v = x_v
        self.__y_v = y_v

    def crear_modelo(self, inputs, outputs, learn_rate):
        # Modelo con tres layers ocultos.
        hidden_layer_nodes = [inputs // 4, inputs // 16, inputs // 64]
        print("Se creara una RNA multiperceptrón con backpropagation")
        print("Estructura: " + str(inputs) + " | " + str(hidden_layer_nodes[0]) + " | " + str(hidden_layer_nodes[1]) + " | " + str(hidden_layer_nodes[2]) + " | " + str(outputs) + " con Softmax")

        input_layer = Input(shape=(inputs,), name="input_img")
        previous_layer = input_layer

        # Hidden layers
        for x in range(len(hidden_layer_nodes)):
            layer_name = "hidden_" + str(x + 1)
            previous_layer = Dense(hidden_layer_nodes[x], activation="sigmoid", name=layer_name)(previous_layer)

        output_layer = Dense(52, activation="softmax", name="output")(previous_layer)

        decr_gradient = tf.keras.optimizers.Adam(learning_rate=learn_rate)

        model = Model(input_layer, output_layer, name="RedNeuronalArtificial")
        model.compile(optimizer=decr_gradient, loss="categorical_crossentropy", metrics=["accuracy"])

        print("Modelo creado con " + str(len(model.layers)) + " capas")
        model.summary()

        # Por algun motivo, cuando corro con PyCharm, esto no anda, pero desde la terminal si
        # plot_model(model, show_layer_names=True, show_shapes=True)

        return model

    def entrenar(self, model, epochs):
        print("Comenzando entrenamiento...")
        history = model.fit(self.__x_e, self.__y_e, epochs=epochs, validation_data=(self.__x_p, self.__y_p))
        print("Entrenamiento finalizado...")
