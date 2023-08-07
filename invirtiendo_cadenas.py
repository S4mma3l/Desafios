#!/usr/bin/env python3

# Programa para invertir cadenas


def reverso(texto):
    texto_long = len(texto)
    texto_reverso = ""
    for index in range(0, texto_long):
        texto_reverso += texto[texto_long - index - 1]

    return texto_reverso


print(reverso("Hola Mundo"))
