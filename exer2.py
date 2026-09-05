# #1
# def verificacao(email):
#     if "@" in email and ".com" in email:
#         print("E-mail verificado com sucesso!...")
#     elif "@" not in email:
#         print("Erro de verificação de e-mail... Não contém "@" ")
#     else: 
#         print("Erro, tente novamente!")



# ver = verificacao("ellen@gmail.com")


# #2
# print("horários de entrada e saída: ")
# entrada = int(input("Digite o horário da entrada:"))
# saida = int(input("Digite o horário de saída: "))

# trabalho = entrada + saida
# if trabalho < 8:
#     print("Não bateu carga horária!")
# elif trabalho >= 8:
#     print("Carga horário atingida com sucesso!")
# else: 
#     print("Erro, tente novamente")


# #3 Geração de Relatórios
vendas = []

def media():
    while True:
    
        venda = int(input(":"))
        if venda == -1:
            break
        vendas.append(venda)



media()

quantidade = len(vendas)
operacao = (sum(vendas) / quantidade) 

print(vendas)

print(f"A media é {operacao}")


if operacao >= 1000:
    print("Sucesso")
else:
    print("Error")


