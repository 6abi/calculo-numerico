import math
# a = float(input("Digite o valor de a: "))
# b = float(input("Digite o valor de b: "))
# e = float(input("Digite o valor da precisão(e): "))

# def passa_funcoes(opcoes):
#     switcher={
#         1: 'f1',
#         2: 'f2',
#         3: 'f3',
#         4: 'f4',
#         5: 'f5',
#                 }
#     return switcher.get(opcoes,"Invalid ")

def f1(x):
    return (x**2 + 0.96*x - 2.08)

def verifica_intervalo(a,b):
    y = False
    if f1(a) * f1(b) < 0:
        y = True
    return y
    
def calcula_raiz(a, b, e):
    i_meio = 0

    if (verifica_intervalo(a,b)) == True:
        while (math.fabs(b-a)/2 >= e):
            i_meio = (a+b)/2
            if f1(i_meio) == 0:
                print("************************")
                print("Valor da raiz: ", round(i_meio, 5))
                print("************************")
                break
            elif f1(a) * f1(i_meio) < 0:
                b = i_meio
            else: 
                a = i_meio
        print("************************")
        print("Valor da raiz: ", round(i_meio, 5))
        print("************************")
        
    else:
        print("************************")       
        print("Intervalo não existe")
        print("************************")
           
# #valores
calcula_raiz(1,6, 0.01)
calcula_raiz(-4,0, 0.01)




