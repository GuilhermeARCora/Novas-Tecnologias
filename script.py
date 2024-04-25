import csv

agenda = {}
lista_dados = ["nome", "telefone", "email", "data de nascimento"]

def salvar_contato():
    nome = input("Nome: ")
    if nome in agenda:
        print("Nome já adicionado.")
        return
    contato = []
    for dado in lista_dados:
        valor = input(f"{dado.capitalize()}: ")
        contato.append(valor)
    agenda[nome] = contato
    print("Contato salvo com sucesso.")

    # Salvar o novo contato no arquivo CSV
    with open('contatos.csv', 'a', newline='') as arquivo:
        writer = csv.writer(arquivo)
        writer.writerow(contato)

def alterar_contato():
    nome = input("Qual nome do contato que deseja alterar: ")
    if nome not in agenda:
        print("Contato não encontrado.")
        return
    print(agenda[nome])
    campo = input("Qual dado deseja alterar: ")
    if campo not in lista_dados:
        print("Campo inválido.")
        return
    novo_dado = input(f"Digite o novo {campo}: ")
    agenda[nome][lista_dados.index(campo)] = novo_dado
    print("Contato alterado com sucesso.")

def buscar_contato():
    nome = input("Qual contato deseja buscar: ")
    if nome in agenda:
        print(agenda[nome])
    else:
        print("Contato não encontrado.")

def listar_contatos():
    print("Lista de Contatos:")
    for nome, contato in agenda.items():
        print(nome, contato)

def excluir_contato():
    nome = input("Qual contato deseja excluir: ")
    if nome in agenda:
        del agenda[nome]
        print("Contato excluído.")
    else:
        print("Contato não encontrado.")

def salvar_em_csv():
    with open('contatos.csv', 'w', newline='') as arquivo:
        writer = csv.writer(arquivo)
        writer.writerow(lista_dados)
        for contato in agenda.values():
            writer.writerow(contato)

while True:
    print("""
    Agenda Pessoal
    1 - Salvar Contato
    2 - Alterar Contato
    3 - Buscar Contato
    4 - Listar Contatos
    5 - Excluir Contato
    6 - Salvar em CSV
    0 - Sair
    """)

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        salvar_contato()
    elif opcao == 2:
        alterar_contato()
    elif opcao == 3:
        buscar_contato()
    elif opcao == 4:
        listar_contatos()
    elif opcao == 5:
        excluir_contato()
    elif opcao == 6:
        salvar_em_csv()
    elif opcao == 0:
        break
    else:
        print("Opção inválida.")
