alunos = {}

def adicionar_aluno():
    nome = input("Informe o nome do aluno: ")
    matricula = input("Informa o número da matrícula: ")
    alunos[matricula] = nome
    print(f"O aluno {nome} com matrícula {matricula} foi adicionado com sucesso!")

def remover_aluno():
    matricula = input("Informe o número da matrícula do aluno a ser removido: ")
    if matricula in alunos:
        nome = alunos.pop(matricula)
        print(f"O aluno {nome} com matrícula {matricula} removido com sucesso!")
    else:
        print("Matrícula não encontrada em nossa base, verifique o numero digitado!")

def visualizar_alunos():
    if alunos:
        print("Lista de alunos cadastrados: ")
        for matricula, nome in alunos.items():
            print(f"Matrícula: {matricula}, Nome: {nome}")
    else:
        print("Não há alunos registrados no momento!")

while True:
    print("\nEscolha uma das opções abaixo:")
    print("1 - Adicionar aluno")
    print("2 - Remover aluno")
    print("3 - Visualizar alunos")
    print("ou")
    print("4 - Sair")

    opcao = input("Digite o número da opção desejada: ")

    if opcao == '1':
        adicionar_aluno()
    elif opcao == '2':
        remover_aluno()
    elif opcao == '3':
        visualizar_alunos()
    elif opcao == '4':
        print("Saindo do programa. Até a próxima!")
        break
    else:
        print("Escolha inválida. Por favor, escolha uma opção válida.")
