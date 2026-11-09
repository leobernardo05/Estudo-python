# import os 

# lista_arquivos = os.listdir("arquivos")
# print(lista_arquivos)

# for nome_arquivo in lista_arquivos:
#     if "txt" in nome_arquivo:
#         if "22" in nome_arquivo:
#             os.rename(f"arquivos/{nome_arquivo}", "arquivos/abr22.txt")


import requests 

link = " https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL"

resposta = requests.get(link)
print(resposta)
dic_resposta = (resposta.json())

for moeda in dic_resposta:
    dic_conversao_moeda = dic_resposta[moeda]
    valor_moeda = dic_conversao_moeda["bid"]
    print(moeda, valor_moeda) 