from xml.dom.minidom import parse

dom = parse("../tarefa01/cardapio.xml")

pratos = dom.getElementsByTagName("prato")

print("CARDÁPIO")

for prato in pratos:
    print(prato.getAttribute("id"), "-", 
          prato.getElementsByTagName("nome")[0].firstChild.nodeValue)

escolha = input("\nDigite o ID do prato: ")

for prato in pratos:
    if prato.getAttribute("id") == escolha:
        print("\nDETALHES")
        print("Nome:", prato.getElementsByTagName("nome")[0].firstChild.nodeValue)
        print("Descrição:", prato.getElementsByTagName("descricao")[0].firstChild.nodeValue)
        print("Ingredientes:")
        for ing in prato.getElementsByTagName("ingrediente"):
            print("-", ing.firstChild.nodeValue)
        preco = prato.getElementsByTagName("preco")[0]
        print("Preço:", preco.getAttribute("moeda"), preco.firstChild.nodeValue)
        print("Calorias:", prato.getElementsByTagName("calorias")[0].firstChild.nodeValue)
        print("Tempo:", prato.getElementsByTagName("tempoPreparo")[0].firstChild.nodeValue)