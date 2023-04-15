FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """ Read the to-do text file """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_args, filepath=FILEPATH):
    """ Write update to-do list in  text file"""
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_args)


if __name__ == "__main__":
    print("hey")