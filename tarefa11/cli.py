import users_wrapper as users


def menu():
    print("\n=== CRUD USERS JSONPLACEHOLDER ===")
    print("1 - Listar usuários")
    print("2 - Ler usuário por ID")
    print("3 - Criar usuário")
    print("4 - Atualizar usuário")
    print("5 - Deletar usuário")
    print("0 - Sair")


def main():
    while True:
        menu()
        option = input("Escolha uma opção: ")

        if option == "1":
            users_list = users.list()
            for u in users_list:
                print(u["id"], u["name"])

        elif option == "2":
            user_id = input("ID do usuário: ")
            user = users.read(user_id)
            print(user)

        elif option == "3":
            name = input("Nome: ")
            username = input("Username: ")
            email = input("Email: ")

            new_user = {
                "name": name,
                "username": username,
                "email": email
            }

            result = users.create(new_user)
            print("Criado:", result)

        elif option == "4":
            user_id = input("ID para atualizar: ")
            name = input("Novo nome: ")
            email = input("Novo email: ")

            updated_user = {
                "name": name,
                "email": email
            }

            result = users.update(user_id, updated_user)
            print("Atualizado:", result)

        elif option == "5":
            user_id = input("ID para deletar: ")
            success = users.delete(user_id)

            print("Deletado com sucesso!" if success else "Erro ao deletar")

        elif option == "0":
            print("Saindo...")
            break

        else:
            print("Opção inválida!")


if __name__ == "__main__":
    main()