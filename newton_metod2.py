import math

x0 = 0  #aproximação inicial
x = 0  #antiga aproximação

x_final = 0 #irá guardar a raiz

#funções
def fx(var):
    return var**3 - var - 1


def flinha(var):
    return 3 * (var**2) - 1


def gx(var):
    return var - (fx(var) / flinha(var))

#precisão requerida
e1 = 10**-6
e2 = 10**-6

k = 0  #contador de interações

print("valor de x0 inicial: " + str(x0))
print(fx(1.3247179572453902))


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
        break
    x0 = x

x = round(x, 7)
print("########################")
print("valor da raiz: " + str(x_final))
print("Valor da fx: " + str(fx((x_final))))
print("Erro  em x: " + str(math.fabs(x - x0)))
print("Numero de iterações: " + str(k))
print("########################")
