# lista_vendas = [1000, 800, 500]
# tupla_vendas = (1000,800,500)

# print(lista_vendas[0])
# print(tupla_vendas[0])

# lista_vendas[0] = 1200
# tupla_vendas[0] = 1200 --> nn é possivel

# bonus 1: R$2 por venda feita
# bonus 2: 1% do valor de vendas

def calcular_bonus(lista_vendas):
    bonus1 = 2 * len(lista_vendas)
    bonus2 = 0.01 * sum(lista_vendas)
    return bonus1, bonus2

vendas = [100, 200, 400, 100] 
resultado = calcular_bonus(vendas)
print(resultado)