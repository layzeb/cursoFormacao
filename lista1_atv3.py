'''Atividade 03

Leia 3 valores, no caso, variáveis A, B e C, que são as três notas de um aluno. A seguir, calcule a média do aluno, sabendo que a nota A tem peso 2, a nota B tem peso 3 e a nota C tem peso 5. Considere que cada nota pode ir de 0 até 10.0, sempre com uma casa decimal.

Entrada

O arquivo de entrada contém 3 valores com uma casa decimal, de dupla precisão (double).

Saída

Imprima a variável MEDIA conforme exemplo abaixo, com 1 dígito após o ponto decimal e com um espaço em branco antes e depois da igualdade.'''

# -*- coding: utf-8 -*-

A = float(input())
B = float(input())
C = float(input())
pA = 2
pB = 3
pC = 5
MEDIA = ((A*pA)+(B*pB)+(C*pC))/10
print('MEDIA = {:.1f}'.format(MEDIA))
