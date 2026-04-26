from xml.dom.minidom import parse
import json

dom = parse("../tarefa02/imobiliaria.xml")
raiz = dom.documentElement

imoveis_xml = raiz.getElementsByTagName("imovel")

dados = {"imobiliaria": {"imovel": []}}

for imovel in imoveis_xml:
    item = {}

    item["descricao"] = imovel.getElementsByTagName("descricao")[0].firstChild.nodeValue

    prop_xml = imovel.getElementsByTagName("proprietario")[0]
    proprietario = {}

    proprietario["nome"] = prop_xml.getElementsByTagName("nome")[0].firstChild.nodeValue

    email_tag = prop_xml.getElementsByTagName("email")
    if email_tag:
        proprietario["email"] = email_tag[0].firstChild.nodeValue

    telefones_xml = prop_xml.getElementsByTagName("telefone")
    telefones = []
    for tel in telefones_xml:
        telefones.append(tel.firstChild.nodeValue)

    proprietario["telefone"] = telefones
    item["proprietario"] = proprietario

    end_xml = imovel.getElementsByTagName("endereco")[0]
    endereco = {}

    for campo in ["rua", "bairro", "cidade", "numero"]:
        tag = end_xml.getElementsByTagName(campo)
        if tag:
            endereco[campo] = tag[0].firstChild.nodeValue

    item["endereco"] = endereco

    carac_xml = imovel.getElementsByTagName("caracteristicas")[0]
    caracteristicas = {}

    caracteristicas["tamanho"] = carac_xml.getElementsByTagName("tamanho")[0].firstChild.nodeValue
    caracteristicas["numQuartos"] = int(carac_xml.getElementsByTagName("numQuartos")[0].firstChild.nodeValue)
    caracteristicas["numBanheiros"] = int(carac_xml.getElementsByTagName("numBanheiros")[0].firstChild.nodeValue)

    item["caracteristicas"] = caracteristicas

    item["valor"] = int(imovel.getElementsByTagName("valor")[0].firstChild.nodeValue)

    dados["imobiliaria"]["imovel"].append(item)

with open("imobiliaria.json", "w", encoding="utf-8") as arquivo:
    json.dump(dados, arquivo, indent=2, ensure_ascii=False)