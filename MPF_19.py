import math

x0 = 1  #aproximação inicial
x = 0  #antiga aproximação

x_final = 0 #guarda a raiz
x_array = [] #Armazena valores anteriores x

raiz = 1.324717957244746
#funções
def fx(var):
    return (var)**3 - var - 1

def gx(var): # g(x) = phi(x)
    return (var + 1) ** (1/3)

def ordem_conver(raiz, arr, len):# Calcula ordem de convergencia -> Para MPF, espera-se que seja 1.0
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

    x_array.append(x0)
    if math.fabs(fx(x0)) < e1:# Verifica condições de parada
        x_final = x0
        break
    k = k + 1  # incrementa o contador de interações
    x = gx(x0)
    if math.fabs(x - x0) < e2 or math.fabs(fx(x)) < e1:# Verifica condições de parada
        x_final = x
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
