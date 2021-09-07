import math

x0 = 0  #aproximação inicial
x = 0  #antiga aproximação

x_final = 0 #irá guardar a raiz
xn = 0 #guardará antiga raiz
xn2 = 0 # guardará a penultima raiz

raiz = 1.324717957244746
#funções
def fx(var):
    return var**3 - var - 1


def flinha(var):
    return 3 * (var**2) - 1


def gx(var):
    return var - (fx(var) / flinha(var))

def ordem_conver(raiz, xn2, xn1, xn):
    en_next = math.fabs(raiz - xn)
    en = math.fabs(raiz - xn1)
    en_past = math.fabs(raiz - xn2)

    result = (math.log(en_next/en)) / (math.log(en/en_past))
    return result
#precisão requerida
e1 = 10**-12
e2 = 10**-12
k = 0  #contador de interações

while True:
    print("Valor de x0: " + str(x0))
    print("Valor da função fx: " + str(fx(x0)))

    if math.fabs(fx(x0)) < e1:
        x_final = round(x0, 7)
        break
    k = k + 1  # incrementa o contador de interações
    x = gx(x0)
    print("Valor de x: " + str(x))

    if math.fabs(x - x0) < e2 or math.fabs(fx(x)) < e1:
        x_final = round(x, 7)
        xn = x0
        break
    xn2 = x0
    x0 = x

ordem = ordem_conver(raiz, xn2, xn, x_final)
ordem = math.fabs(round(ordem, 1))
print("########################")
print("valor da raiz: " + str(x_final))
print("Valor da fx: " + str(fx(x_final)))
print("Erro  em x: " + str(math.fabs(x - x0)))
print("Numero de iterações: " + str(k))
print("Ordem de convergência: " + str(ordem))
print("########################")
