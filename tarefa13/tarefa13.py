import zeep

wsdl_url = "https://www.dataaccess.com/webservicesserver/NumberConversion.wso?WSDL"

client = zeep.Client(wsdl=wsdl_url)
numero = int(input("Digite um número inteiro:"))
resultado = client.service.NumberToWords(ubiNum=numero)

print(f"\nNúmero digitado: {numero}")
print(f"Por extenso em inglês: {resultado}")