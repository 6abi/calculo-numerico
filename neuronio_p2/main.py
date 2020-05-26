#Modelo de Hodgkin-Huxley
#
# Algoritmo para calcular a corrente que
# percorre um neurônio, descrevendo como potenciais de ação
#são iniciados neles
#
#base de estudos usadas:
#https://pt.wikipedia.org/wiki/Modelo_de_Hodgkin-Huxley
#https://physoc.onlinelibrary.wiley.com/doi/epdf/10.1113/jphysiol.1952.sp004764
#https://www.youtube.com/watch?v=01sHT70rI3c

import math
import matplotlib.pyplot as plt

def main():
    print("\n______________________Neurônio - Modelo de Hodgkin-Huxley_______________________________")
    print("###########################################################################################")
    print("###########################################################################################")
    print("___________________________________________________________________________________________\n")
    print("____________Digite '1' caso queira mudar o valor maximo do intervalo________________________")
    print("____________Digite '2' para calcular comm ∆t = 0.01 ms no intervalo de [0, 0.3] ms__________")
    print(("Opção: "))

    get_op()

def get_op():
    op = input()
    handleOp(op)

def handleOp(op):
    while op:
        if op == '1':
            interval = float(input("Digite o valor final de t em ms:"))
            print("Novo intervalo")
            print("____________Cálculo para o valore de ∆t = 0.01 ms no intervalo de [0, {}]_____________\n".format(interval))
        elif op == '2':
            interval = 0.3
        else:
            print("Digite uma das opções, '1' ou '2' !")
            return  get_op()
        calculusCurrentVolt(interval)
        return op

def alphaN(v, h):
    return (h * (v - 10)) / (math.exp((v - 10) / 10) - 1)

def betaN(v, h):
    return 0.125 * math.exp( v/ 80)

def alphaM(v, h):
    return (h * (v - 25)) / (math.exp((v - 25) / 10) - 1)

def betaM(v, h):
    return h * math.exp(v/18)

def alphaH(v, h):
    return 0.07 * math.exp(v/20)

def betaH(v):
    return 1 / (math.exp( (v-30) / 10) + 1)

def derivedN(n, v, t):
    alpha_n = (alphaN(v, 0.01)) * (1 - n)
    beta_n = (betaN(v, 0.125) * n)
    return n + t * (alpha_n - beta_n)

def derivedM(m, v, t):
    aplha_m = (alphaM(v, 0.1) * (1 - m) )
    beta_m = (betaM(v, 4) * m)
    return m + t * (aplha_m - beta_m)

def derivedH(h, v, t):
    aplha_h = (alphaH(v, 0.07) * (1 - h))
    beta_h = (betaH(v) * h)
    return h + t * (aplha_h - beta_h)


#############################################################


def calculusCurrentVolt(interval):
    #values for convertion
    milli = math.pow(10,-3)
    micro =math.pow(10,-6)
    t = 0.01 * 10**(-3)


    gK = 3.60
    gNa = 12.0
    gL = 0.03
#millivot mV
    vK = -77 * milli
    vNa = 50 * milli #mV455
    vL = -54.402 *  milli

    n0 = 0.3176
    m0 = 0.0529
    h0 = 0.5961

    auxN = n0
    auxM = m0
    auxH = h0

    v0 = -65.002  *  milli
    t0 = 0 #segundos


    dT = 0.01 *  milli #ms
    Cm = 1 * micro
    gama = dT/Cm

    tensao = []
    tempo = []
    tempo.append(t0)
    tensao.append(v0)

    pN = gK * (n0**4) * (tensao[0] - vK)
    pM = gNa * (m0**3) * h0 * (tensao[0] - vNa)
    pL = gL * (tensao[0] - vL)

    aux = tensao[0] - (pN + pM + pL) * gama
    tensao.append(aux)
    tempo.append(t0+dT)

    #print(tensao[1])

    M = [m0]
    M.append(m0)
    N = [n0]
    N.append(n0)
    H = [n0]
    H.append(h0)

    i = 0.0
    c = 1

    if interval != 0.3:
        parada = interval * milli
    else:
        parada = 0.3 * milli

    while i <= parada:
        auxN = derivedN(auxN,tensao[c],t)
        N.append(auxN)
        auxM = derivedM(auxM,tensao[c],t)
        M.append(auxM)
        auxH = derivedH(auxM,tensao[c],t)
        H.append(auxH)

        pN = gK * (auxN**4) * (tensao[c] - vK)
        pM = gNa * (auxM**3) * auxH * (tensao[c] - vNa)
        pL = gL * (tensao[c] - vL)

        aux = tensao[0] - (pN + pM + pL) * gama
        tensao.append(aux)

        c += 1
        i = i + dT
        tempo.append(i)
    print("Cálculo para o valore de ∆t = 0.01ms no intervalo de [0,{}] ms".format(interval))
    graphic(tempo,tensao)


def graphic(time, tension):

    plt.ioff()
    print("\nCriando gráfico...")
    fig = plt.figure(figsize=(14, 12))
    plt.title('Gráfico Modelo Hodgkin-Huxley')
    plt.grid(True)
    plt.plot(time,tension,label='V(t) V')
    plt.xlabel('tempo - t(ms)')
    plt.ylabel('valores  das tensões(V(t))')
    plt.legend()
    fig.savefig("H-H.png")
    print("Grafico criado, arquivo: H-H.png ")
    print("--Finished the program!--")
    plt.show()

if __name__ == "__main__":
    main()

