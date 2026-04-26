import json
with open("../tarefa09/imobiliaria.json", "r", encoding="utf-8") as arquivo:
    dados = json.load(arquivo)

imoveis = dados["imobiliaria"]["imovel"]

print("IMOBILIÁRIA")

for i, imovel in enumerate(imoveis, start=1):
    print(i, "-", imovel["descricao"])

escolha = input("\nDigite o ID do imóvel: ")


for i, imovel in enumerate(imoveis, start=1):
    if str(i) == escolha:
        print("\nDETALHES")

        print("Descrição:", imovel["descricao"])

        print("Proprietário:")
        for chave, valor in imovel["proprietario"].items():
            print("-", chave + ":", valor)

        print("Endereço:")
        for chave, valor in imovel["endereco"].items():
            print("-", chave + ":", valor)

        print("Características:")
        for chave, valor in imovel["caracteristicas"].items():
            print("-", chave + ":", valor)

        print("Valor:", imovel["valor"])