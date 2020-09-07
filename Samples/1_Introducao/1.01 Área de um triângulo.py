"""
#Autor: António Brito / Carlos Bragança
#Data: 2019
#Objectivo: Calcular a Área de um triângulo sendo dados os valores
# da base e da altura.


"""
#Variáveis:
base = float()  #Base do triângulo
altura = float()  #Altura do triângulo
area = float()  #Área do triângulo


base = float(input("Base do triângulo: "))
altura = float(input("Altura do triângulo: "))
area = base * altura / 2

print("Área do triângulo = " + str(area))