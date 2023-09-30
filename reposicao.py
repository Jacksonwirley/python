# # # # # for numero in range(2,21,2):
# # # # #     print(numero)


# # # # # soma = 0
# # # # # for numero in range(1, 101):
# # # # #     soma += numero
# # # # # print(soma)

# # # # # lista = [5,5,5,10]
# # # # # count = 0
# # # # # soma = 0
# # # # # for numero in lista:
# # # # #     soma += numero
# # # # #     count += 1
# # # # #     media = soma / count   
# # # # # print(media)

# # # # num = int (input("Digite um numero: "))
# # # # count = 0
# # # # for numero in range(1, num+1):
# # # #     if num % numero == 0:
# # # #         count += 1
# # # #    #7 print(numero)
# # # # if count == 2:
# # # #     print("Ele é Primo!")
# # # # else:
# # # #     print("Não é primo!")


# # # # palavra = input("Digite uma palavra: ")
# # # # count = 0
# # # # for letra in palavra:
# # # #     #print(letra)
# # # #     if letra in 'aeiouAEIOU':
# # # #         count += 1
# # # # print(count)


# # # soma = 0
# # # qtde_numeros = 0

# # # while True:
# # #     numero = int(input("Digite um número inteiro (ou 0 para sair): "))

# # #     if numero == 0:
# # #         break

# # #     soma += numero
# # #     qtde_numeros += 1

# # # if qtde_numeros > 0:
# # #     media = soma / qtde_numeros
# # #     print(f"Quantidade de números digitados: {qtde_numeros}")
# # #     print(f"Soma dos números: {soma}")
# # #     print(f"Média dos números: {media:.2f}")
# # # else:
# # #     print("Nenhum número foi digitado.")

# # x=0

# # while x>=0:

# #     print('Olá mundo!')

# senha_cadastrada = "123"
# email_cadastrado = "teste@gmail.com"

# while True:
#     senha_digitada = input("Digite a senha: ")
#     email_digitado = input("Digite o email: ")

#     if senha_digitada == senha_cadastrada and email_digitado == email_cadastrado:
#         print("Acesso permitido. Bem-vindo!")
#         break  
#     else:
#         print("Senha ou email incorretos. Tente novamente.")

senha_cadastrada = "123"
email_cadastrado = "teste@gmail.com"

while True:
    print("Por favor, faça login.")
    senha_digitada = input("Digite a senha: ")
    email_digitado = input("Digite o email: ")

    if senha_digitada == senha_cadastrada and email_digitado == email_cadastrado:
        print("Acesso permitido. Bem-vindo!")
        break
    else:
        print("Senha ou email incorretos. Tente novamente.")
