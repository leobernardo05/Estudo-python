# lista_vendas = [1000, 800, 500]
# tupla_vendas = (1000,800,500)

# print(lista_vendas[0])
# print(tupla_vendas[0])

# lista_vendas[0] = 1200
# tupla_vendas[0] = 1200 --> nn é possivel

# bonus 1: R$2 por venda feita
# bonus 2: 1% do valor de vendas

# tupla -> valores imutaveis
def calcular_bonus(lista_vendas):
    bonus1 = 2 * len(lista_vendas)
    bonus2 = 0.01 * sum(lista_vendas)
    return bonus1, bonus2

vendas = [100, 200, 400, 100] 
# unpacking da tupla -> desempacotamento
bonus1, bonus2 = calcular_bonus(vendas)

print(bonus1)
print(bonus2)

# utilização de tuplas
lista_telas = [(1090, 1080), (2140, 1080)]
for altura, largura in lista_telas:
    print(altura, largura)

vendas = {
    "Andre": [1000, 500, 800, 80, 3000, 8000],
    "Andressa": [2000, 3000, 4000, 5000, 6000],
    "Carlos": [1000, 2000, 3000, 4000, 5000],
    "Daniel": [1000, 2000, 3000, 4000, 5000]
}

# bonus de cada funcionario 
# total de bonus 1 pago aos funcionarios
# total de bonus 2 pago aos funcionarios
vendas["Andre"]
vendas["Andressa"]

total_bonus1 = 0
total_bonus2 = 0
for vendedor in vendas:
    bonus1, bonus2 = calcular_bonus(vendas[vendedor])
    print(f"Vendedor: {vendedor}. Bonus: {bonus1}. Bonus2: {bonus2}")
    total_bonus1 = total_bonus1 + bonus1
    total_bonus2 = total_bonus2 + bonus2

print("Total Bonus1:", total_bonus1)
print("Total Bonus2:", total_bonus2)
print("Total geral:", total_bonus1 + total_bonus2)