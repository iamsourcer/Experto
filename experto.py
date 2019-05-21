#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import readchar  # https://github.com/magmax/python-readchar
from random import choice


print('Hola, preguntame lo que quieras! >>')


letra = None
letras = []
palabras_inicio = ['Decime ', 'Adivina ']
palabra_inicio = choice(palabras_inicio)
# respuesta
i = 0
while letra != readchar.key.ENTER:
    letra = readchar.readchar()
    letras.append(letra)
    if i < len(palabra_inicio):
        print(palabra_inicio[i], flush=True, end='')
        i += 1
respuesta = ''.join(letras)

# pregunta
while letra != '?':
    letra = readchar.readchar()
    if letra == readchar.key.BACKSPACE:
        print('\b \b', flush=True, end='')
    else:
        print(letra, flush=True, end='')

print()
print(respuesta)


def input_oculto(texto):
    pass
