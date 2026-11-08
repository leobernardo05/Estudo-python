lista_precos = [1500, 1000, 800, 2000]

def calcular_imposto():
    imposto_total = 0
    for preco in lista_valores:
        if preco > 1000:
            taxa = 0.1
        else:
            taxa = 0.1
        imposto = preco * taxa
        imposto_total = imposto_total + imposto
    return imposto_total

# utilização da função
calcular_imposto(lista_precos)

lista2_precos = [500, 4000, 32000, 2600, 1000]
calcular_imposto[lista2_precos]

