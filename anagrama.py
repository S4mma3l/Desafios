#!/usr/bin/env python3

# un anagrama
print("Verificar palabra si son o no Angramas")
palabra_uno = input("Indica la palabra 1= ")
palabra_dos = input("Indica la plabra 2= ")


def es_anagrama(palabra_uno, palabra_dos):
    if palabra_uno.lower() == palabra_dos.lower():
        return False
    return sorted(palabra_uno.lower()) == sorted(palabra_dos.lower())


print(es_anagrama(palabra_uno, palabra_dos))
