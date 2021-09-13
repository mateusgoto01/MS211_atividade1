import math

x0 = 0   #aproximação inicial
x = 0   #antiga aproximação

x_final = 0  #irá guardar a raiz
x_array = []
raiz = 1.324717957244746
#funções
def fx(var):
    return var**3 - var - 1


def flinha(var):
    return 3 * (var**2) - 1


def gx(var):
    return var - fx(var) / flinha(var)

def ordem_conver(raiz, arr, len):
    en_next = math.fabs(raiz - arr[len - 1])
    en = math.fabs(raiz - arr[len - 2])
    en_past = math.fabs(raiz - arr[len - 3])

    result = (math.log(en_next/en)) / (math.log(en/en_past))
    return result
#precisão requerida
e1 = 10**-12
e2 = 10**-12
k = 0  #contador de interações

while True:
    x_array.append(round(x0, 14))
    print("Valor de x0: " + str(x0))
    print("Valor da função fx: " + str(fx(x0)))

    if math.fabs(fx(x0)) < e1:
        x_final = round(x0, 14)
        x_array.append(round(x,14))
        break
    k = k + 1  # incrementa o contador de interações
    x = gx(x0)

    print("Valor de x: " + str(x))

    if math.fabs(x - x0) < e2 or math.fabs(fx(x)) < e1:
        x_final = round(x, 14)

        break
    x0 = x


len = len(x_array)

ordem = ordem_conver(raiz, x_array, len)
ordem = math.fabs(round(ordem, 1))

print("########################")
print("valor da raiz: " + str(x_final))
print("Valor da fx: " + str(fx(x_final)))
print("Erro  em x: " + str(math.fabs(x - x0)))
print("Numero de iterações: " + str(k))
print("Ordem de convergência: " + str(ordem))
print("########################")
