#!/usr/bin/env python3

# Secuencia de fibonacci


def fibonacci():
    prim = 0
    seco = 1

    for numeros in range(0, 50):
        print(prim)

        fib = prim + seco
        prim = seco
        seco = fib


fibonacci()


# sqrt para calcular raices cuadradas
from math import sqrt


def fib(n):
    if n < 2:
        return n
    else:
        u = (1 + sqrt(5)) / 2
        j = (u**n - (1 - u) ** n) / sqrt(5)
        # round nos permite redondear numeros flotantes
        return round(j)


print(fib(9))
