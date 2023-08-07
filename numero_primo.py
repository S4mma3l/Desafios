#!/usr/bin/env python3

# Numero Primo


def numero_primo():
    for numero in range(1, 101):
        if numero >= 2:
            es_divisible = False

            for indice in range(2, numero):
                if numero % indice == 0:
                    es_divisible = True
                    break
            if not es_divisible:
                print(numero)

    return True


numero_primo()
