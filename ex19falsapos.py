import math
import numpy as np

a = 1  # guarda o limite do intervalo inferior
b = 2  # guarda o limite do intervalo superior

x_final = 0  # irá guardar a raiz
xn = 0  # guardará antiga raiz
ordem = 0

raiz = 1.324717957244746  # Melhor aproximação da raiz por método de newton


# funções
def fx(var):
    return (var**3) - var - 1


def gx(a, b):
    return ((a*fx(b))-(b*fx(a)))/(fx(b)-fx(a))

def pnmais1(alfa,xnmais1,xn,xnmenos1):
    enmais1 = math.fabs(alfa-xnmais1)
    en = math.fabs(alfa-xn)
    enmenos1 = math.fabs(alfa-xnmenos1)
    return (np.log(enmais1/en))/(np.log(en/enmenos1))

# precisão requerida
e1 = 1 * (10 ** -12)
e2 = 1 * (10 ** -12)

k = 0  # contador de interações

while True:
    k += 1
    xn = x_final
    x_final = gx(a, b)
    if math.fabs(x_final-a) < e1 or math.fabs(b-x_final) < e2:
        break
    if (fx(a) * fx(x_final)) < 0:
        b = x_final
    elif fx(x_final) == 0:
        break
    else:
        a = x_final
    ordem = pnmais1(raiz,gx(a,b),x_final,xn)
    print("Ordem de convergencia:",math.fabs(ordem))

print("########################")
print(f"valor da raiz: {(x_final)} ")
print("Valor da f(x):",(fx(x_final)))
print("Erro  em x:" ,(math.fabs(raiz - x_final)))
print("Numero de iterações:",(k))
print("Ordem de convergência:",math.fabs(ordem))
print("########################")
