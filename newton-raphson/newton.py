import math
delta = 0.001
i = 1

def f(x):
    return x**2 - 2


def f_derivada(x):
    return (f(x + delta) - f(x)) / delta

def newton_raphson(x):
    return  x - (f(x) / f_derivada(x))

def erro(xprox, x):
    return abs(xprox - x)

def calcula(x, n):
    xprox = newton_raphson(x)
    for i in range(n):
        e  = erro(xprox, x)
        while (e  >= delta):
            i = i+1
            return xprox
raiz = calcula(1, 100)


print("Valor da raiz:  ",round(raiz,4))
print(" execuções:", i)


