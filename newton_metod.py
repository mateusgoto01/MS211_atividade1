import math

x0 = 1.5  #aproximação inicial
x = 0  #antiga aproximação

x_final = 0 #irá guardar a raiz
xn = 0 #guardará antiga raiz
xn2 = 0 # guardará a penultima raiz

raiz = 1.4474142712962368 # Melhor aproximação da raiz por método de newton

#funções
def fx(var):
    return (math.e ** (-var ** 2)) - math.cos(var)


def flinha(var):
    return -2 * var * (math.e ** (-var ** 2)) + math.sin(var)


def gx(var):
    return var - (fx(var) / flinha(var))


def ordem_conver(raiz, xn2, xn1, xn):
    en_next = math.fabs(raiz - xn)
    en = math.fabs(raiz - xn1)
    en_past = math.fabs(raiz - xn2)
    print(en_next)
    print(en)
    print(en_past)
    result = (math.log(en_next/en)) / (math.log(en/en_past))
    return result


#precisão requerida
e1 = 1*(10**-12)
e2 = 1*(10**-12)

k = 0  #contador de interações


while True:

    if math.fabs(fx(x0)) < e1:
        x_final = x0
        xn = x0
        break
    k = k + 1  # incrementa o contador de interações
    x = gx(x0)
    print("X0 : " + str(x0))
    print("x : " + str(x))
    if math.fabs(x - x0) < e2 or math.fabs(fx(x)) < e1:
        x_final = x
        xn = x0
        break
    xn2 = x0
    x0 = x

print(x_final)
x_final = round(x_final, 15)

print(xn)
print(xn2)
ordem = ordem_conver(raiz, xn2, xn, x_final)
ordem = math.fabs(round(ordem, 1))
print("########################")
print("valor da raiz: " + str(x_final))
print("Valor da f(x): " + str(fx(x_final)))
print("Erro  em x: " + str(math.fabs(x - x0)))
print("Numero de iterações: " + str(k))
print("Ordem de convergência: " + str(ordem))
print("########################")
