#Marcos Vinicius 
#Aplicativo de Listas To do List

import json

class Tarefa:
    def __init__(self, descricao, finalizada=False):
        self.descricao = descricao
        self.finalizada = finalizada

class ListaDeTarefas:
    def __init__(self, arquivo):
        self.arquivo = arquivo
        self.tarefas = self.carregar_tarefas()

    def salvar_tarefas(self):
        with open(self.arquivo, 'w') as arquivo_json:
            json.dump([(id_tarefa, tarefa.__dict__) for id_tarefa, tarefa in self.tarefas], arquivo_json)

    def carregar_tarefas(self):
        try:
            with open(self.arquivo, 'r') as arquivo_json:
                tarefas_json = json.load(arquivo_json)
                return [(id_tarefa, Tarefa(**tarefa)) for id_tarefa, tarefa in tarefas_json]
        except FileNotFoundError:
            return []

    def adicionar_tarefa(self, descricao):
        if not descricao or not descricao[0].isupper():
            print("Descrição inválida. A descrição deve começar com maiúscula.")
            return

        nova_tarefa = Tarefa(descricao)
        self.tarefas.append((self.gerar_id(), nova_tarefa))
        self.salvar_tarefas()
        print("Tarefa registrada!!!")

    def marcar_tarefa_como_realizada(self, tarefa_id):
        def marca_tarefa(tarefa):
            return Tarefa(tarefa.descricao, finalizada=True) if tarefa_id == tarefa.id and not tarefa.finalizada else tarefa

        self.tarefas = [(id_tarefa, marca_tarefa(tarefa)) for id_tarefa, tarefa in self.tarefas[::-1]]
        self.salvar_tarefas()
        print("Tarefa realizada!!!" if any(tarefa_id == id_tarefa and tarefa.finalizada for id_tarefa, tarefa in self.tarefas) else "Tarefa não encontrada ou já realizada.")

    def editar_tarefa(self, tarefa_id, nova_descricao):
        def edita_tarefa(tarefa):
            return Tarefa(nova_descricao, finalizada=tarefa.finalizada) if tarefa_id == tarefa.id else tarefa

        self.tarefas = [(id_tarefa, edita_tarefa(tarefa)) for id_tarefa, tarefa in self.tarefas]
        self.salvar_tarefas()
        print("Tarefa editada com sucesso!!!" if any(tarefa_id == id_tarefa for id_tarefa, tarefa in self.tarefas) else "Tarefa não encontrada.")

    def mostrar_tarefas(self):
        def formatar_tarefa(id_tarefa, tarefa):
            box = "[x]" if tarefa.finalizada else "[ ]"
            return f"{id_tarefa}. {tarefa.descricao} {box}"

        print("Lista de Tarefas:")
        for id_tarefa, tarefa in self.tarefas:
            print(formatar_tarefa(id_tarefa, tarefa))

    def listar_tarefas_finalizadas(self):
        tarefas_finalizadas = [formatar_tarefa(id_tarefa, tarefa) for id_tarefa, tarefa in self.tarefas if tarefa.finalizada]
        print("Tarefas Finalizadas:")
        for tarefa_finalizada in tarefas_finalizadas:
            print(tarefa_finalizada)

    def listar_tarefas_pendentes(self):
        tarefas_pendentes = [formatar_tarefa(id_tarefa, tarefa) for id_tarefa, tarefa in self.tarefas if not tarefa.finalizada]
        print("Tarefas Pendentes:")
        for tarefa_pendente in tarefas_pendentes:
            print(tarefa_pendente)

    def excluir_tarefa(self, tarefa_id):
        self.tarefas = [(id_tarefa, tarefa) for id_tarefa, tarefa in self.tarefas if id_tarefa != tarefa_id]
        self.salvar_tarefas()
        print("Tarefa excluída com sucesso!!!" if any(tarefa_id == id_tarefa for id_tarefa, tarefa in self.tarefas) else "Tarefa não encontrada.")

    def gerar_id(self):
        return max([id_tarefa for id_tarefa, _ in self.tarefas] + [0]) + 1

# Exemplo de uso
arquivo_tarefas = 'tarefas.json'
lista_tarefas = ListaDeTarefas(arquivo_tarefas)

while True:
    print("\n1. Adicionar Tarefa")
    print("2. Marcar Tarefa como Realizada")
    print("3. Editar Tarefa")
    print("4. Mostrar Tarefas")
    print("5. Listar Tarefas Finalizadas")
    print("6. Listar Tarefas Pendentes")
    print("7. Excluir Tarefa")
    print("0. Sair")

    escolha = input("\nEscolha uma opção: ")

    if escolha == '0':
        break
    elif escolha == '1':
        descricao = input("Digite a descrição da tarefa: ")
        lista_tarefas.adicionar_tarefa(descricao)
    elif escolha == '2':
        tarefa_id = int(input("Digite o ID da tarefa a ser marcada como realizada: "))
        lista_tarefas.marcar_tarefa_como_realizada(tarefa_id)
    elif escolha == '3':
        tarefa_id = int(input("Digite o ID da tarefa a ser editada: "))
        nova_descricao = input("Digite a nova descrição da tarefa: ")
        lista_tarefas.editar_tarefa(tarefa_id, nova_descricao)
    elif escolha == '4':
        lista_tarefas.mostrar_tarefas()
    elif escolha == '5':
        lista_tarefas.listar_tarefas_finalizadas()
    elif escolha == '6':
        lista_tarefas.listar_tarefas_pendentes()
    elif escolha == '7':
        tarefa_id = int(input("Digite o ID da tarefa a ser excluída: "))
        lista_tarefas.excluir_tarefa(tarefa_id)
    else:
        print("Opção inválida. Tente novamente.")
