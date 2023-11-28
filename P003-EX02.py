import json

def reajusta_dez_porcento(empregados):
    for empregado in empregados:
        empregado['salario'] *= 1.1  # Aumenta o salário em 10%

def ler_dados_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as arquivo:
            empregados = json.load(arquivo)
        return empregados
    except FileNotFoundError:
        print(f"Arquivo '{nome_arquivo}' não encontrado. Criando uma nova lista de empregados.")
        return []
    except json.JSONDecodeError:
        print("Erro ao decodificar o arquivo JSON. Certifique-se de que o arquivo contém dados válidos.")
        return []

def salvar_dados_arquivo(nome_arquivo, empregados):
    with open(nome_arquivo, 'w') as arquivo:
        json.dump(empregados, arquivo, indent=2)

def main():
    nome_arquivo = "dados_empregados.json"
    empregados = ler_dados_arquivo(nome_arquivo)

    while True:
        print("\nMenu:")
        print("1. Adicionar empregado")
        print("2. Reajustar salários em 10%")
        print("3. Listar empregados")
        print("4. Sair")

        opcao = input("Escolha uma opção (1-4): ")

        if opcao == '1':
            nome = input("Digite o nome do empregado: ")
            sobrenome = input("Digite o sobrenome do empregado: ")
            ano_nascimento = input("Digite o ano de nascimento do empregado: ")
            rg = input("Digite o RG do empregado: ")
            ano_admissao = input("Digite o ano de admissão do empregado: ")
            salario = float(input("Digite o salário do empregado: "))

            empregado = {
                'nome': nome,
                'sobrenome': sobrenome,
                'ano_nascimento': ano_nascimento,
                'rg': rg,
                'ano_admissao': ano_admissao,
                'salario': salario
            }

            empregados.append(empregado)
            print("Empregado adicionado com sucesso!")

        elif opcao == '2':
            reajusta_dez_porcento(empregados)
            print("Salários reajustados em 10% para todos os empregados.")

        elif opcao == '3':
            print("\nLista de Empregados:")
            for empregado in empregados:
                print(f"Nome: {empregado['nome']} {empregado['sobrenome']}, Salário: R${empregado['salario']:.2f}")

        elif opcao == '4':
            salvar_dados_arquivo(nome_arquivo, empregados)
            print("Saindo do programa. Até mais!")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
