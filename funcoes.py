lista_precos = [1500, 1000, 800, 2000]

def definir_taxa_imposto(preco):
    if preco > 1500:
        taxa = 0.2
    elif preco > 1000:
        taxa = 0.15
    else:
        taxa = 0.1
    return taxa

# função calcular imposto
def calcular_imposto(lista_valores):
    imposto_total = 0
    for preco in lista_valores:
        taxa = definir_taxa_imposto(preco)
        imposto = preco * taxa
        imposto_total = imposto_total + imposto
    return imposto_total

# utilização da função
imposto_lista1 = calcular_imposto(lista_precos)
print(imposto_lista1)

lista2_precos = [500, 4000, 32000, 2600, 1000]
imposto_lista2 = calcular_imposto(lista2_precos)
print(imposto_lista2)

