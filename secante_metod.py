from __future__ import division
import math

x0 = 1  #aproximação inicial 1
x1 = 2  #aproximação inicial 2
x = 0

x_final = 0 #irá guardar a raiz
x_array = []
raiz = 1.4474142712962368 # Melhor aproximação da raiz por método de newton

#funções
def fx(var):
    return (math.e ** (-var ** 2)) - math.cos(var)


def gx(x0, x1):
    result = (x0*fx(x1) - x1*fx(x0)) / (fx(x1) - fx(x0))
    return result


def ordem_conver(raiz, arr, len):
    en_next = math.fabs(raiz - arr[len - 1])
    en = math.fabs(raiz - arr[len - 2])
    en_past = math.fabs(raiz - arr[len - 3])

    result = (math.log(en_next/en)) / (math.log(en/en_past))
    return result


#precisão requerida
e1 = 1*(10**-12)
e2 = 1*(10**-12)

k = 0  #contador de interações

check = False

while True:
    x_array.append(round(x, 14))
    if math.fabs(fx(x1)) < e1:
        print(math.fabs(fx(x1)))
        x_final = x1
        break
    k = k + 1  # incrementa o contador de interações
    x = gx(x0, x1)
    if math.fabs(x - x1) < e2 or math.fabs(fx(x)) < e1:
        print(x)
        print(math.fabs(fx(x)))
        x_final = round(x, 15)
        break

    x0 = x1
    x1 = x

len = len(x_array)
print(x_array)
ordem = ordem_conver(raiz, x_array, len)
ordem = math.fabs(round(ordem, 2))
print("########################")
print("valor da raiz: " + str(x_final))
print("Valor da f(x): " + str(fx(x_final)))
print("Erro  em x: " + str(math.fabs(x - x1)))
print("Numero de iterações: " + str(k))
print("Ordem de convergência: " + str(ordem))
print("########################")
