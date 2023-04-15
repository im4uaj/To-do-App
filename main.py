# from functions import get_todos, write_todos
import functions
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print()
while True:
    user_action = input("Type add, show , edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:]

        todos = functions.get_todos("todos.txt")

        todos.append(todo + '\n')

        functions.write_todos(todos)

    elif user_action.startswith("show"):
        todos = functions.get_todos("todos.txt")

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}-{item}"
            print(row)

    elif user_action.startswith("edit"):

        try:
            number = int(user_action[5:])
            number = number - 1

            todos = functions.get_todos("todos.txt")

            new_todo = input("enter new todo: ")
            todos[number] = new_todo + '\n'

            functions.write_todos(todos)

        except ValueError:
            print("your command is invalid")
            continue
    elif user_action.startswith("complete"):

        todos = functions.get_todos("todos.txt")

        number = int(user_action[9:]) - 1
        print(f"todo to be removed {todos[number]}")
        todos.pop(number)

        functions.write_todos(todos)

    elif user_action.startswith('exit'):
        break
    else:
        print("command is invalid")
