# for i in range(10):
#     print(i)
#     print("inscreva-se no canal")

lista_precos = [1500, 1000, 800, 2000]

taxa_imposto = 0.1

for preco in lista_precos:
    imposto = preco * taxa_imposto
    print(f"Preco do produto {preco}, imposto é de {imposto}")

# Exemplos
# produtos de até 1000 pagam 10%
# produtos acima de 1000 pagam 15% de imposto

for preco in lista_precos:
    if preco > 1000:
        taxa = 0.15
    else:
        taxa = 0.1
    imposto = taxa * preco
    print(f"preco do produto: {preco}, imposto: {imposto}")

# Exemplo 2:
# mesma regra de imposto mas eu quero conseguir calcular o total de todos os produtos

total_imposto = 0

for preco in lista_precos:
    if preco > 1000:
        taxa = 0.15
    else:
        taxa = 0.1
    imposto = taxa*preco

    total_imposto = total_imposto + imposto

    print(f"Preço do produto: {preco}, Imposto: {imposto}")
