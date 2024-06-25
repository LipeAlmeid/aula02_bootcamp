import math

# Faça um programa que peça dois numeros inteiros e imprima a divisao inteira do primeiro pelo segundo

try:
    numero_01 = int(input("Digite o primeiro numero: "))
    numero_02 = int(input("Digite o segundo numero: "))
    resultado = numero_01//numero_02
    print(resultado)
except ZeroDivisionError: 
    print("Nao pode dividir 0 por 0")
except KeyboardInterrupt: 
    print("Acho que voce nao quis iserir um numero")


# Escreva um programa que calcule a area de um circulo, recebendo o raio como entrada

raio_do_circulo = float(input("Digite um raio: "))
area_do_circulo = math.pi * raio_do_circulo ** 2
print(f"{area_do_circulo:.2f}") #faz com que formate o resultado para somente 2 casa decimais


# Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mes e o ano separadamente

data_informada = input("Insira uma data no formato dd/mm/aaaa: ")
lista_de_dia_mes_ano = data_informada.split("/")

print(f"O elemento 1 é o : {lista_de_dia_mes_ano[0]}")
print(f"O elemento 2 é o : {lista_de_dia_mes_ano[1]}")
print(f"O elemento 3 é o : {lista_de_dia_mes_ano[2]}")