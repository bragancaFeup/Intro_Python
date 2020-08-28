""""
Autor: Bragança / Brito, A. E. S. C.
Data: 2019

# Trocar o algarismo das centenas com o das unidades num no de 3 algarismos

"""

valorInteiro = int(input("valor ="))


valorString = str(valorInteiro)
unidades = int(valorString[2])
dezenas = int(valorString[1])
centenas=int(valorString[0])

novovalor = unidades*100+dezenas*10+centenas

print(f"novo Valor = {novovalor}")

# ou


valorString = str(valorInteiro)
unidadesStr = valorString[2]
dezenasStr = valorString[1]
centenasStr=valorString[0]

novovalor = unidadesStr+dezenasStr+centenasStr

print(f"novo Valor = {novovalor}")