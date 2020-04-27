# EXERCÍCIO: escreva um algoritmo para encontrar f(x) para
# x={-0.5,0,0.5,1.5,2,2.5} e construa o gráfico de f(x) para x E [-1,3].

#      | x0   | x1  | x2
# x    | -1   | 0   | 3
# f(x) | 15   | 8   |-1

# Bárbara Cardoso - BEC

import matplotlib.pyplot as plt
import matplotlib as mpl

def main():
    print("\n______Interpolação polinomial - Método de Lagrange____________ \n")


def lagrange(x,y, valor_x):

    pontos = len(x)
    n = pontos - 1
    tam_polinomio = n+1
    soma = 0
    resultado =[]
    for i in range(tam_polinomio):
        p = 1
        for j in range(tam_polinomio):
            if j != i:
                p *= ((valor_x - x[j]) / (x[i] - x[j]))
        soma += y[i] * p
    resultado_y = round((soma),4)
    print('Para x = {}' .format(valor_x), ' ----> ', 'y = {}' .format(resultado_y))

    return resultado_y


def passa_x():
    x_pontos = [-1, 0, 3]
    return x_pontos

def passa_y():
    y_pontos = [15, 8, -1]
    return y_pontos

def ponto_x():

    xi = -1.5
    p_x = []
    num_y = []
    while xi < 3:
        xi += 0.5
        p_x.append(xi)
        p = lagrange(passa_x(), passa_y(), xi)
        num_y.append(p)
    p_grafico =  grafico(p_x, num_y)
    return p_grafico

def grafico(x,y):
    print("\nCriando o gráfico...\n")
    plt.ylabel('F(x)')
    plt.xlabel('Eixo x')
    for i in range(10):
        plt.plot(x,y, 'o', color = 'red')
        plt.plot(x,y, color = 'black')
        fig = plt.gcf()
        plt.savefig('grafico_interpolacao.png', format='png')
        plt.show()
    print("Grafico criado, arquivo: grafico_interpolacao ")



main()
passa_x()
passa_y()
ponto_x()
