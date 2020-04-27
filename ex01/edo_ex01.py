# Um corpo esférico cai de uma altura h e sofre a ação da força peso e da força de arrasto aerodinâmico.
# Considere que o ar passa pelo corpo com fluxo laminar (baixa velocidade relativa). Descreva as possibilidades
# se o corpo cair com velocidade inicial , v0, maior, menor e igual à velocidade limite.
# Considere: m = 1kg, b=0.2 kg2/s 𝑔=9.8𝑚.𝑠−2. Utilize o método de Euler para integrar a EDO.


import math
import numpy as np
import matplotlib.pyplot as plt

#consts
m = 1.0
b = 0.2
g = 9.81
h = 0.01

def f(v):
    return v + ((-b)*v**2/m - g)*h

def velocidade_terminal():
    v_terminal = math.sqrt(m * g / b)
    return v_terminal
#
def vel_inicial():
    v_inicial = float(input('Digite a velocidade inicial(m/s): '))
    return velocidade(v_inicial)

def status_v(v_terminal, v_inicial):
    if v_inicial > v_terminal:
        print("Velocidade inicial MAIOR do que a velocidade terminal")
    elif v_inicial < v_terminal:
        print("Velocidade inicial MENOR do que a velocidade terminal")
    elif  v_inicial == v_terminal:
        print("Velocidade inicial IGUAL do que a velocidade terminal")

def velocidade(v_inicial):
    n = 0
    tempo = 0.00
    velocidade = np.empty(1000)
    v = velocidade_terminal()
    velocidade[n] = v_inicial
    n = 1
    dado_x = []
    dado_y = []

    dado_x.append(tempo)
    dado_y.append(v_inicial)

    if velocidade[0] < 0.0:
        print("Digite um valor maior do que zero!")
        return vel_inicial()

    status_v(v,v_inicial)

    while n < 1000:
        if velocidade[n -1] < 0.0:
            break
        velocidade[n] = f(velocidade[n - 1])
        tempo = round(n*h,3)
        dado_x.append(tempo)
        dado_y.append(velocidade[n])
        print("Tempo: {}s ----------" .format(tempo), " Velocidade: {} m/s" .format(round(velocidade[n],4)))
        n += 1


    print("____________________________________________")
    print("Vinicial do corpo esférico = {} m/s" . format(v_inicial))
    status_v(v,v_inicial)
    print("Tempo para velocidade ser igual a zero: {}s" .format(tempo))

    for i in range(1000):
        plot_grafico = grafico(dado_x,dado_y)

        return plot_grafico


def grafico(x,y):
    print("\nCriando o gráfico da Velocidade x Tempo...\n")
    plt.title("VELOCIDADE X TEMPO - OBJETO CÍRCULAR")
    plt.ylabel('Velocidade(m/s)')
    plt.xlabel('tempo')
    plt.plot(x,y, color = 'orange')
    plt.grid(True)
    fig = plt.gcf()
    plt.savefig('grafico_ex01_edo.png', format='png')
    plt.show()
    print("Grafico criado, arquivo: grafico_ex01_edo.png ")
