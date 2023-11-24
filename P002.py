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
        self.tarefas.append((self.id_counter, Tarefa(descricao)))
        self.id_counter += 1

    def marcar_tarefa_como_finalizada(self, tarefa_id):
        for _, tarefa in self.tarefas:
            if tarefa_id == _:
                tarefa.finalizada = True

    def mostrar_tarefas(self):
        print("Lista de Tarefas:")
        for id_tarefa, tarefa in self.tarefas:
            box = "[x]" if tarefa.finalizada else "[ ]"
            print(f"{id_tarefa}. {tarefa.descricao} {box}")

# Exemplo de uso
lista_tarefas = ListaDeTarefas()
lista_tarefas.adicionar_tarefa("Preparar a marmita")
lista_tarefas.adicionar_tarefa("Arrumar a mochila")
lista_tarefas.adicionar_tarefa("Fechar as janelas")

lista_tarefas.marcar_tarefa_como_finalizada(2)

lista_tarefas.mostrar_tarefas()
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

# Exemplo de uso
lista_tarefas = ListaDeTarefas()
descricao_tarefa = input("Digite a descrição da tarefa: ")
lista_tarefas.adicionar_tarefa(descricao_tarefa)

# Mostrar a lista de tarefas
lista_tarefas.mostrar_tarefas()
