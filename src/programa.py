#!/usr/bin/python3

from src.config import config
from src.ai.reconocedor import Reconocedor
from src.ai.aumentador import Aumentador

aumentador = Aumentador()
reconocedor = Reconocedor(aumentador)

datos = reconocedor.iniciar_aumentacion()
x_e, y_e, x_p, y_p = reconocedor.crear_sets(datos, config["limitador"])

reconocedor.procesar_sets(
    x_e,
    y_e,
    x_p,
    y_p,
    config["ancho_imagenes_a_procesar"] * config["alto_imagenes_a_procesar"],
    52,
    config["epochs"],
    config["tasa_aprendizaje"])
