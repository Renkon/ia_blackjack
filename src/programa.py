#!/usr/bin/python3

from src.config import config
from src.ai.reconocedor import Reconocedor
from src.ai.aumentador import Aumentador

aumentador = Aumentador()
reconocedor = Reconocedor(aumentador)

datos = reconocedor.iniciar_aumentacion()
x_entrenamiento, y_entrenamiento, x_pruebas, y_pruebas, mapa_clases = reconocedor.crear_sets()

reconocedor.procesar_sets(
    x_entrenamiento,
    y_entrenamiento,
    x_pruebas,
    y_pruebas,
    mapa_clases,
    config["ancho_imagenes_a_procesar"] * config["alto_imagenes_a_procesar"] * 3,
    52,
    config["epochs"],
    config["tasa_aprendizaje"])
