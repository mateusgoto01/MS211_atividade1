import math

x0 = 1.5  #aproximação inicial
x = 0  #antiga aproximação

x_final = 0 #irá guardar a raiz
x_ant = 0 #guardará antiga raiz
x_suc = 0 # guardará a proxima raiz
#funções
def fx(var):
    return (math.e ** (-var ** 2)) - math.cos(var)


def flinha(var):
    return -2 * var * (math.e ** (-var ** 2)) + math.sin(var)


def gx(var):
    return var - (fx(var) / flinha(var))

#precisão requerida
e1 = 1*(10**-4)
e2 = 1*(10**-4)

k = 0  #contador de interações

print("valor de x0 inicial: " + str(x0))
check = False

while True:
    print("Valor de x0: " + str(x0))
    print("Valor da função fx: " + str(fx(x0)))
    if math.fabs(fx(x0)) < e1:
        print(math.fabs(fx(x0)))
        x_final = x0
        break
    k = k + 1  # incrementa o contador de interações
    x = gx(x0)
    print("Valor de x: " + str(x))

    if math.fabs(x - x0) < e2 or math.fabs(fx(x)) < e1:
        print(x)
        print(math.fabs(fx(x)))
        x_final = x
        break
    x0 = x

print("########################")
print("valor da raiz: " + str(x_final))
print("Valor da fx: " + str(fx(x_final)))
print("Erro  em x: "+ str(math.fabs(x - x0)))
print("Numero de iterações: " + str(k))
print("########################")
