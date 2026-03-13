print("Sistema de Clínica Veterinária iniciado!")

pets = []

def cadastrar_pet():
    nome = input("Nome do pet: ")
    especie = input("Espécie: ")
    idade = input("Idade: ")

    pet = {
        "nome": nome,
        "especie": especie,
        "idade": idade
    }

    pets.append(pet)
    print("Pet cadastrado com sucesso!\n")


def listar_pets():
    if not pets:
        print("Nenhum pet cadastrado.\n")
        return

    for pet in pets:
        print(f"Nome: {pet['nome']} | Espécie: {pet['especie']} | Idade: {pet['idade']}")
    print()


def buscar_pet():
    nome_busca = input("Digite o nome do pet: ")
    for pet in pets:
        if pet["nome"].lower() == nome_busca.lower():
            print(f"Encontrado: {pet}")
            return
    print("Pet não encontrado.\n")


def remover_pet():
    nome_remover = input("Digite o nome do pet que deseja remover: ")
    for pet in pets:
        if pet["nome"].lower() == nome_remover.lower():
            pets.remove(pet)
            print("Pet removido com sucesso!\n")
            return
    print("Pet não encontrado.\n")


def menu():
    while True:
        print("1 - Cadastrar pet")
        print("2 - Listar pets")
        print("3 - Buscar pet")
        print("4 - Remover pet")
        print("5 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_pet()
        elif opcao == "2":
            listar_pets()
        elif opcao == "3":
            buscar_pet()
        elif opcao == "4":
            remover_pet()
        elif opcao == "5":
            print("Encerrando sistema...")
            break
        else:
            print("Opção inválida!\n")


menu()
