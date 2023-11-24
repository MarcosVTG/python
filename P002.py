#Marcos Vinicius 
#Aplicativo de Listas To do List

import json

def load_tasks():
    try:
        with open('tasks.json', 'r') as json_file:
            return json.load(json_file)
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open('tasks.json', 'w') as json_file:
        json.dump(tasks, json_file)

tasks = load_tasks()

def list_tasks():
    print("Lista de Tarefas:")
    for i, task in enumerate(tasks, start=1):
        status = "[x]" if task["completed"] else "[ ]"
        print(f"{i}. {task['description']} {status}")

def add_task():
    description = input("Digite a descrição da tarefa: ").capitalize()
    task = {"description": description, "completed": False}
    tasks.append(task)
    save_tasks(tasks)
    print("Tarefa registrada!")

def mark_task_completed():
    list_tasks()
    try:
        task_id = int(input("Digite o ID da tarefa a ser marcada como realizada: ")) - 1
        if 0 <= task_id < len(tasks):
            task = tasks.pop(task_id)
            task["completed"] = True
            tasks.insert(0, task)
            save_tasks(tasks)
            print("Tarefa marcada como realizada!")
        else:
            print("ID inválido")
    except ValueError:
        print("Digite ID válido.")

def edit_task():
    list_tasks()
    try:
        task_id = int(input("Digite o ID da tarefa a ser editada: ")) - 1
        if 0 <= task_id < len(tasks):
            new_description = input("Digite a nova descrição da tarefa: ").capitalize()
            tasks[task_id]["description"] = new_description
            save_tasks(tasks)
            print("Tarefa editada com sucesso!")
        else:
            print("ID inválido")
    except ValueError:
        print("Digite ID válido.")

def main():
    while True:
        print("\nMenu:")
        print("1. Listar tarefas")
        print("2. Registrar nova tarefa")
        print("3. Marcar tarefa como realizada")
        print("4. Editar tarefa")
        print("5. Sair")

        choice = input("Escolha uma opção: ")

        if choice == "1":
            list_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            mark_task_completed()
        elif choice == "4":
            edit_task()
        elif choice == "5":
            print("Programa encerrado")
            break
        else:
            print("Opção inválida!!")

if __name__ == "__main__":
    main()

