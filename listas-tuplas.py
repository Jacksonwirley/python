pares = []
impares = []

# Pedindo ao usuário para inserir 10 valores e preencha a lista
for i in range(10):
    valor = int(input(f"Informe o {i + 1}º valor: "))
    if valor % 2 == 0:
        pares.append(valor)
    else:
        impares.append(valor)

# Criando uma tupla com os números ímpares
tupla_impares = tuple(impares)

# Calculando a quantidade de números pares e ímpares
qtd_pares = len(pares)
qtd_impares = len(impares)

# Calculando a soma de números pares e ímpares
soma_pares = sum(pares)
soma_impares = sum(impares)

print("Números Pares:", pares)
print("Números Ímpares (em uma tupla):", tupla_impares)
print("Quantidade de Números Pares:", qtd_pares)
print("Quantidade de Números Ímpares:", qtd_impares)
print("Soma de Números Pares:", soma_pares)
print("Soma de Números Ímpares:", soma_impares)
