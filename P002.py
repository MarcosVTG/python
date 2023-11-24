#Marcos Vinicius 
#Aplicativo de Listas To do List

class Tarefa:
    def __init__(self, descricao, finalizada=False):
        self.descricao = descricao
        self.finalizada = finalizada

class ListaDeTarefas:
    def __init__(self):
        self.tarefas = []
        self.id_counter = 1

    def adicionar_tarefa(self, descricao):
        if not descricao or not descricao[0].isupper():
            print("Descrição inválida. A descrição deve começar com maiúscula.")
            return

        nova_tarefa = Tarefa(descricao)
        self.tarefas.append((self.id_counter, nova_tarefa))
        self.id_counter += 1
        print("Tarefa registrada!!!")

    def marcar_tarefa_como_realizada(self, tarefa_id):
        def marca_tarefa(tarefa):
            return Tarefa(tarefa.descricao, finalizada=True) if tarefa_id == tarefa.id and not tarefa.finalizada else tarefa

        self.tarefas = [(id_tarefa, marca_tarefa(tarefa)) for id_tarefa, tarefa in self.tarefas[::-1]]
        print("Tarefa realizada!!!" if any(tarefa_id == id_tarefa and tarefa.finalizada for id_tarefa, tarefa in self.tarefas) else "Tarefa não encontrada ou já realizada.")

    def editar_tarefa(self, tarefa_id, nova_descricao):
        def edita_tarefa(tarefa):
            return Tarefa(nova_descricao, finalizada=tarefa.finalizada) if tarefa_id == tarefa.id else tarefa

        self.tarefas = [(id_tarefa, edita_tarefa(tarefa)) for id_tarefa, tarefa in self.tarefas]
        print("Tarefa editada com sucesso!!!" if any(tarefa_id == id_tarefa for id_tarefa, tarefa in self.tarefas) else "Tarefa não encontrada.")

    def mostrar_tarefas(self):
        def formatar_tarefa(id_tarefa, tarefa):
            box = "[x]" if tarefa.finalizada else "[ ]"
            return f"{id_tarefa}. {tarefa.descricao} {box}"

        print("Lista de Tarefas:")
        for id_tarefa, tarefa in self.tarefas:
            print(formatar_tarefa(id_tarefa, tarefa))

# Exemplo de uso
lista_tarefas = ListaDeTarefas()
lista_tarefas.adicionar_tarefa("Preparar a marmita")
lista_tarefas.adicionar_tarefa("Arrumar a mochila")
lista_tarefas.adicionar_tarefa("Fechar as janelas")

lista_tarefas.mostrar_tarefas()

tarefa_a_realizar = int(input("Digite o ID da tarefa a ser realizada: "))
lista_tarefas.marcar_tarefa_como_realizada(tarefa_a_realizar)

lista_tarefas.mostrar_tarefas()

tarefa_a_editar = int(input("Digite o ID da tarefa a ser editada: "))
nova_descricao = input("Digite a nova descrição da tarefa: ")
lista_tarefas.editar_tarefa(tarefa_a_editar, nova_descricao)

lista_tarefas.mostrar_tarefas()
