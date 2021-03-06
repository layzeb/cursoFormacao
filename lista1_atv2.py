'''Atividade 02

A fórmula para calcular a área de uma circunferência é: area = π * raio². Considerando para este problema que π = 3.14159:

Efetue o cálculo da área, elevando o valor de Raio ao quadrado e multiplicando por π.
Entrada

A entrada contém um valor de ponto flutuante (dupla precisão), no caso, a variável raio.

Saída

Apresentar a mensagem "A=" seguido pelo valor da variável area, conforme exemplo abaixo, com 4 casas após o ponto decimal.'''

# -*- coding: utf-8 -*-

raio = float(input())
area = 3.14159*(raio*raio)
print('A={:.4f}'.format(area))

