while True:
    user_action = input("Type add, show, edit, complete or extit: ")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("Enter a todo: ") + "\n"
            file = open("todos.txt", "r")
            todos = file.readlines()

            todos.append(todo)
            
            file = open("todos.txt", "w") ##aqui abre o arquivo em modo de escrita
            file.writelines(todos) ##aqui escreve a lista no arquivo
        case 'show':
                for index, item in enumerate(todos):
                        row = f"{index + 1}-{item}"
                        print(row)
        case 'edit':
                number = int(input("Number of the todo to edit:"))
                number = number - 1 ##aqui é para refletir exatamente o indice partido de 1
                new_todo = input("Enter a new todo:") 
                todos[number] = new_todo
        case 'complete':
                number = int(input("Number of the todo to complete:"))
                todos.pop(number - 1)
        case 'exit':
                break


print("Bye!")
    

    