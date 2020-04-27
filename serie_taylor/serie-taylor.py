import math

# conversão de graus para radianos
def para_radianos(x):
    return x/180*math.pi

#calculo fatorial
def calcula_fatoria(n):
    resultado = 1
    
    for n in range(1,n+1):
        resultado *= n
    return resultado
        
# taylor - partes - valor de "e^x"
def taylor(x, i):
    return math.pow(x, i)/calcula_fatoria(i)

# calcula seno
def calcula_seno(x, termos):
    y = 5
    z = 0
    while True:
        z = z - taylor(x, y)
        y = y + 2
        z = z + taylor(x, y)
        y = y + 2
        if y >= termos:
            break
    return x+z

# calcula cosseno
def calcula_cosseno(x, termos):
    y = 10
    z = 0
    while True:
        z = z - taylor(x, y)
        y = y + 2
        z = z + taylor(x, y)
        y = y + 2
        if y >= termos:
            break
    return 1+z

#truncamento
def truncar(valor):
    t = 10 # numero casas decimais
    return int(valor * 10**t)/10**t


# teste seno - comparação valor da biblioteca
print('teste seno:')
seno_math = math.sin(para_radianos(30))
seno_math = truncar(seno_math)
seno_taylor = calcula_seno(para_radianos(30), 10)
seno_taylor = truncar(seno_math)

print('valor biblioteca: ' + str(seno_math))
print('valor calculadoe truncado 10 casas decimais:   ' + str(seno_taylor))
print('')

# testa cosseno - - comparação valor da biblioteca
print('testa cosseno:')
cosseno_math = math.cos(para_radianos(30))
cosseno_taylor = calcula_cosseno(para_radianos(30), 10)
cosseno_math = truncar(cosseno_math)
cosseno_taylor = truncar(cosseno_taylor)

print('valor biblioteca: ' + str(cosseno_math))
print('valor calculadoe truncado 10 casas decimais:   ' + str(cosseno_taylor))