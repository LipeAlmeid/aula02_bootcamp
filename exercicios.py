import math

# Faça um programa que peça dois numeros inteiros e imprima a divisao inteira do primeiro pelo segundo

numero_01 = int(input("Digite o primeiro numero: "))
numero_02 = int(input("Digite o segundo numero: "))

print(numero_01//numero_02)


# Escreva um programa que calcule a area de um circulo, recebendo o raio como entrada

raio_do_circulo = float(input("Digite um raio: "))
area_do_circulo = math.pi * raio_do_circulo ** 2
print(f"{area_do_circulo:.2f}")