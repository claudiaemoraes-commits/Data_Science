import math
import numpy as np
import os
from datetime import time

# #1 
# nome = str(input("Digite seu nome: "))
# print(f'Seu nome é {nome}.')

# #2
# idade = str(input("Digite sua idade: "))
# altura = float(input("Digite sua altura: "))
# peso = float(input("Digite seu peso: "))

# print(f"Sua idade é {idade}, sua altura é {altura}, seu peso é Kg:{peso}")

# #3
# a = "Maçã"
# def mudar(a):
#     # global a -> não dá para pedir parâmetros e o global junto
#     a = "Banana"
#     return a


# print(a)
# print(mudar(a))


# #4
# PI = (3.14)
# raio = float(input("Qual o raio do círculo?: "))
# area_circ = ((raio**2) * PI ) 
# print("A área do círculo é: {}".format(area_circ))

#5
# TAXA = (15.0)
# produto = float(input("Digite o valor do produto: "))
# valor_final = ( TAXA + produto )
# print(f"O valor final do produto é {valor_final}")

# #6
# KM = (20)
# milhas = ( KM * 1.60934 )
# print(f" O valor de {KM}Km em milhas é: {milhas}.")

# #7
# nota1 = float(input("Digite a primeira nota: "))
# nota2 = float(input("Digite a segunda nota: "))
# nota3 = float(input("Digite a terceira nota: "))
# media = (nota1 + nota2 + nota3) // 3
# print(f"A média de notas do aluno é: {media}")

# #8
# peso = float(input("Digite seu peso: "))
# altura = float(input("Digite sua altura: "))
# imc = (altura * altura) / peso
# print(f"O seu IMC é: {imc:.2}")

# #9
# a = 1
# for c in range(1, 5):
#     a += 1
#     adicao = list()
#     adicao.append(a)
#     print(f"Os valores de adição é: {adicao}.")
    

# b= 5
# for c in range(5, 0, -1):
#     b -= 1
#     sub = list()
#     sub.append(b)
#     print(f"os valores da subtração é: {sub}.")


# #10
# num1 = int(input("Digite o primeiro número: "))
# num2 = int(input("Digite o segundo número: "))
# soma = (num1 + num2)
# print(f"A soma das variáveis 1 e 2 é: {soma}")

# #11
# nome = str(input("Olá, qual seu nome?: "))
# print(f"Olá {nome}!, seja muito bem-vindo(a)")

# #12
# num1 = int(input("Digite o primeiro número: "))
# num2 = int(input("Digite o segundo número: "))
# mult = (num1 * num2)
# print(f"A multiplicação dos números é: {mult}")

# #13 e 14 (Arredondamento e casas decimais)
# dado = float(input("Insira um dado com números: "))
# print(f"O dado inserido foi: {dado:.3}")

# dado = (dado // 1)
# print(f"O dado inserido em valor inteiro é {dado}")

# #15
# NUM = (1.51313)

# ### print(round(num,2)) -> vai mostar 1.51 - 2 casas decimais

# #Arredondamento
# print(math.ceil(NUM)) #2
# print(math.floor(NUM)) #1

# #16
# PI = (3.1415)
# print(f"O truncamento de PI em duas casas decimais é: {PI:.3}")

# #17
# y = (16.8)
# x = (19.5)
# divisao = ( x / y )
# print(f"A divisão foi: {divisao:.3}")

# #18 **
# numero = float(input("Digite um valor a ser truncado: "))
# print(math.trunc(numero))
# numero = int(numero)


# #19, 20, 21
# a = np.array([10, 3, 6 ,4])
# print(f"O número maior da lista é: {a.max()}. ")
# print(f"A somatória dos valores da lista é: {a.sum()} ")


# for c in range(0, 1):
#     #for i, k in enumerate(a):
#     a = (a * 2)
#     print(f"Cada valor de uma lista multiplicado por 2 é: {a}")


# #22, 23
# m1 = np.array([2, 3, 4])
# print(m1)
# print(f"A soma dos elementos é: {m1.sum()}.")

# #24
# m1 = np.array([2, 9, 6])
# m2 = np.array([7, 3, 1])
# print(m1*m2)

# #25, 26, 27 
# x = 2
# def imprimir():
#     global x
#     print(f"O valor atual de x é: {x}.")
#     x = 15
#     return print(f"O novo valor de x é {x}.")


# print(imprimir())

# #28
# def soma(a, b):
#     soma = a + b
#     return print(f"A somatória dos valores foi: {soma}.")


# a = int(input("Digite um valor: "))
# b = int(input("Digite outro valor: "))
# print(soma(a, b))

# #**29
# def par(a, b):
#     if a % 2 == 0 and b % 2 == 0:
#         print(f" O número digitado é par: {a}, {b}")
#     elif a != 0  and b != 0:
#         print(f"O número digitado não é par: {a}, {b}")
#     else:
#         print("Tente novamente...")

# n1 = par(6, 8)
# n2 = par(19, 5)


# #30
# def area(base, altura):
#     area = (base * altura) // 2
#     print(f"A área do triângulo é: {area}")


# valores = area(12, 5)


# #31 verifique se o arquivo existe
# print("Verificação de existência de arquivos")

# if os.path.exists('teste.py'):
#     print("O arquivo foi encontrado e ele existe!")
# else:
#     print("O arquivo não foi encontrado, e ele não exite!")


# #32 Crie e escreva em novo arquivo
# with open('teste.txt', 'a', encoding='utf-8') as arquivo:
#     arquivo.write("Foi criado um novo arquivo com sucesso! ")
#     arquivo.write("Aqui será contado o número de linhas utilizada!.")
#     arquivo.write("A área calculada do triâgulo, é dada pela fórmula (b x h) / 2 !")



# #33 Leia um arquivo linha a linha
# #34 Conte linhas de um arquivo em texto
# if os.path.exists('teste.txt'):
#     with open('teste.txt') as file:
#         for files in file:
#             print(f"O arquivo tem {len(files.splitlines())} linhas.")



# #35
# import csv
# with open('tste.csv', newline='') as csvfile:
#     spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
#     for row in spamreader:
#         print(', '.join(row))



# #36
# n1 = int(input("Digite um número para ser validado: "))

# if n1 >= 0:
#     print(f"O número é positivo!")
# elif n1 <= 0 :
#     print(f"O número é menor que 0!...")
# else: 
#     print("tente novamente!")



# #37
# print("Sistema de login:")
# nome = str(input("Nome usuário: "))
# senha = str(input("Senha usuário: "))

# senha = '1234'

# if senha == '1234' and nome == 'Ellen':
#     print('Login realizado com sucesso!')
# else:
#     print("Senha ou nome incorreto! Tente novamente...")




# #38
# n1 = int(input("Digite um número para ser classificado em positivo ou negativo: "))

# if n1 > 0:
#     print(f"O número {n1} é positivo!")
# elif n1 < 0:
#     print(f"O número {n1} é negativo!")
# else:
#     print("Erro tente novamente...")


# #39
# nota1 = int(input("Digite a primeira nota: "))
# nota2 = int(input("Digite a segunda nota: "))
# nota3 = int(input("Digite a terceira nota: "))

# if nota1 >= 5 and nota2 >= 5 and nota3 >= 5:
#     print(f"As notas do aluno estão acima da média! Elas são: {nota1}, {nota2}, {nota3}")
# elif nota1 < 5 and nota2 < 5 and nota3 < 5:
#     print(f"As notas do aluno estão abaixo da média!")
# else:
#     ("Erro, tente novamente...")


# #40
# idade = int(input("Digite sua idade para ser classificada: "))

# match(idade):
#     case _ if idade >= 60:
#         print("Você já está na fase da velhice!")
#     case _ if idade > 60 and idade >= 18:
#         print("Você está na fase adulta!")
#     case _ if idade < 18 and idade >= 5:
#         print("Você é uma criança!")
#     case _:
#         print("Erro, tente novamente!...")


# #41
# i = 0

# for c in range(0, 11):
#     print(f" o número {i} somado de + 1 é: ")
#     i += 1
#     print(i)

# #42
# compra = str(input("o que você está comprando? "))
# sacola = ["maçã", "banana", "uva"]
# sacola.append(compra)
# print(sacola)

# #43
# print("Tabuada")

# n = int(input("Digite um número para a tabuada: "))

# for c in range(0, 11):
#     c += 1
#     resultado = n * c
#     print(f"{n} x {c} = {resultado}")


# #44
# senha = '1234'
# while True:
#     senha = str(input("Digite a senha: "))

#     if senha != '1234':
#         print("Tente novamente!")

#     if senha == '1234':
#         break


# #**45
# n = 0
# while True:
#     for c in range(0, 5):
#         n += 1
#         print(n)

#     break


46
sair = -1

while True:
    print("Você quer continuar?")
    resp = str(input(" S/N "))

    if resp == "Ss":
        print("O programa vai continuar rodando...")

    else:
        resp == "Nn"
        print("O programa será encerrado...")
        print("Encerrado com sucesso, até mais!")
        break

    