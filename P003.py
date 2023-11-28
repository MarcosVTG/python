class Produto:
    def __init__(self, codigo, nome, preco):
        self.codigo = codigo
        self.nome = nome
        self.preco = preco


class Supermercado:
    def __init__(self):
        self.produtos = {}

    def inserir_produto(self, codigo, nome, preco):
        if not codigo.isdigit() or len(codigo) != 13:
            print("Erro: Código inválido. Deve conter 13 dígitos numéricos.")
            return

        if not nome[0].isupper():
            print("Erro: O nome do produto deve começar com uma letra maiúscula.")
            return

        if not isinstance(preco, float):
            print("Erro: Preço inválido. Deve ser um número decimal.")
            return

        produto = Produto(codigo, nome, preco)
        self.produtos[codigo] = produto
        print(f"Produto '{produto.nome}' cadastrado com sucesso!")

    def excluir_produto(self, codigo):
        if codigo in self.produtos:
            produto = self.produtos.pop(codigo)
            print(f"Produto '{produto.nome}' com código {codigo} excluído.")
        else:
            print(f"Erro: Produto com código {codigo} não encontrado.")

    def listar_produtos(self):
        print("\nLista de Produtos:")
        for produto in self.produtos.values():
            print(f"Código: {produto.codigo}, Nome: {produto.nome}, Preço: R${produto.preco:.2f}")

    def consultar_preco(self, codigo):
        if codigo in self.produtos:
            produto = self.produtos[codigo]
            print(f"O preço do produto '{produto.nome}' é R${produto.preco:.2f}.")
        else:
            print(f"Erro: Produto com código {codigo} não encontrado.")


def exibir_menu():
    print("\nMenu:")
    print("1. Inserir novo produto")
    print("2. Excluir produto cadastrado")
    print("3. Listar todos os produtos")
    print("4. Consultar preço de um produto")
    print("5. Sair")


def obter_opcao():
    return input("Escolha uma opção (1-5): ")


def main():
    supermercado = Supermercado()

    while True:
        exibir_menu()
        opcao = obter_opcao()

        if opcao == '1':
            codigo = input("Digite o código do produto: ")
            nome = input("Digite o nome do produto: ")
            try:
                preco = float(input("Digite o preço do produto: "))
                supermercado.inserir_produto(codigo, nome, preco)
            except ValueError:
                print("Erro: Preço inválido. Deve ser um número decimal.")
        elif opcao == '2':
            codigo = input("Digite o código do produto a ser excluído: ")
            supermercado.excluir_produto(codigo)
        elif opcao == '3':
            supermercado.listar_produtos()
        elif opcao == '4':
            codigo = input("Digite o código do produto para consultar o preço: ")
            supermercado.consultar_preco(codigo)
        elif opcao == '5':
            print("Saindo do programa. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
