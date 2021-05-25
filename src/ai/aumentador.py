#!/usr/bin/python3

import cv2
import matplotlib.pyplot as plt
from src.config import config
from random import shuffle
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from matplotlib.pyplot import imshow, subplots, show

class Aumentador:
    def __init__(self):
        self.__data = []

    def procesar_imagen(self, label, source):
        print("Iniciando procesamiento de " + str(source))

        image = self.__reformatear_imagen(source)

        # Hacemos un proceso de hacer un cuadrado alrededor, para tener espacio extra para aplicar rotaciones"
        images = image.reshape((1, image.shape[0], image.shape[1], 1))

        # Para mostrar la imagen que se va a procesar...
        # imshow(images[0])
        # show()

        data_generator = ImageDataGenerator(
            rotation_range=180,
            width_shift_range=0.2,
            height_shift_range=0.2,
            brightness_range=(0.5, 1.5),
            shear_range=0.5,
            zoom_range=0.8,
            fill_mode="nearest",
        )
        
        data_generator.fit(images)
        image_iterator = data_generator.flow(images)

        # Para mostrar una parte de lo que el image iterator puede generar
        # plt.figure(figsize=(8, 8))
        # for i in range(64):
        #     plt.subplot(8, 8, i+1)
        #     plt.xticks([])
        #     plt.yticks([])
        #     plt.grid(False)
        #     plt.imshow(image_iterator.next()[0].astype('int'))
        # plt.show()

        for x in range(int(config["imagenes_por_carta"] * 1.2)):
            transformed_image = image_iterator.next()[0].astype('int') / 255
            transformed_image = transformed_image.reshape((config["ancho_imagenes_a_procesar"] * config["alto_imagenes_a_procesar"]))
            self.__data.append([transformed_image, label])
        
        print("Generadas " + str(config["imagenes_por_carta"]) + " imagenes distintas para label " + str(label))
        
    def barajar_datos(self):
        shuffle(self.__data)
    
    def obtener_datos(self):
        return self.__data

    def limpiar_datos(self):
        self.__data.clear()

    def __reformatear_imagen(self, source):
        image = cv2.imread(str(source), cv2.IMREAD_GRAYSCALE)
        image = cv2.resize(image, (config["ancho_imagenes"], config["alto_imagenes"]))
        size = image.shape[:2]
        delta_w = config["ancho_imagenes_a_procesar"] - config["ancho_imagenes"]
        delta_h = config["alto_imagenes_a_procesar"] - config["alto_imagenes"]
        top, bottom = delta_h // 2, delta_h - (delta_h // 2)
        left, right = delta_w // 2, delta_w - (delta_w // 2)
        color = [255, 255, 255]
        image = cv2.copyMakeBorder(image, top, bottom, left, right, cv2.BORDER_CONSTANT, value=color)

        return image
