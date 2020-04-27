# EXERCÍCIO: escreva um algoritmo para encontrar f(x) para
# x={-0.5,0,0.5,1.5,2,2.5} e construa o gráfico de f(x) para x E [-1,3].

#      | x0   | x1  | x2
# x    | -1   | 0   | 3
# f(x) | 15   | 8   |-1


import math
import matplotlib.pyplot as plt



def lagrange(x,y, valor_x):

    pontos = len(x)
    n = pontos - 1
    tam_polinomio = n+1
    soma = 0
    for i in range(tam_polinomio):
        p = 1
        for j in range(tam_polinomio):
            if j != i:
                p *= ((valor_x - x[j]) / (x[i] - x[j]))
        soma += y[i] * p
    print('Para x = {}' .format(valor_x), ' ----> ', 'y = {}' .format(round(soma, 5)))

lagrange([-1,0,3],[15,8,-1], 3)
lagrange([-1,0,3],[15,8,-1], -0.5)
lagrange([-1,0,3],[15,8,-1], 0.0)
lagrange([-1,0,3],[15,8,-1], 0.5)
lagrange([-1,0,3],[15,8,-1], 1.5)
lagrange([-1,0,3],[15,8,-1], 2)
lagrange([-1,0,3],[15,8,-1], 2.5)



