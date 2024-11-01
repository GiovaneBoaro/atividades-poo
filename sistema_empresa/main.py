from empresa.funcionario import Funcionario

def main():
    funcionarios = []
    
    while True:
        print("\nMenu:")
        print("1. Cadastrar novo funcionário")
        print("2. Exibir funcionários cadastrados")
        print("3. Aumentar salário de um funcionário")
        print("4. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            nome = input("Digite o nome do funcionário: ")
            salario = float(input("Digite o salário do funcionário: "))
            funcionario = Funcionario(nome, salario)
            funcionarios.append(funcionario)
            print(f"Funcionário {nome} cadastrado com sucesso!")

        elif opcao == '2':
            if funcionarios:
                for i, func in enumerate(funcionarios):
                    print(f"{i + 1}. {func.exibir_informacoes()}")
            else:
                print("Nenhum funcionário cadastrado.")

        elif opcao == '3':
            if funcionarios:
                for i, func in enumerate(funcionarios):
                    print(f"{i + 1}. {func.nome}")
                index = int(input("Escolha o número do funcionário para aumentar o salário: ")) - 1
                if 0 <= index < len(funcionarios):
                    aumento = float(input("Digite o valor do aumento: "))
                    funcionarios[index].aumentar_salario(aumento)
                    print(f"Salário de {funcionarios[index].nome} aumentado com sucesso!")
                else:
                    print("Número inválido.")
            else:
                print("Nenhum funcionário cadastrado.")

        elif opcao == '4':
            print("Saindo do sistema...")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
