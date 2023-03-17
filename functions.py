FILEPATH = 'todos.txt'


# this fxn prevents previously entered todos in the filepath from being overwritten by storing them in the 'todos'
# list obj
def get_todos(filepath=FILEPATH):
    """
    Reads a text file and returns a list of
    the to-do items.

    :param filepath:
    :return: todos_local,
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


# this fxn writes the 'todos' list obj to the filepath parameter
def write_todos(todos_arg, filepath=FILEPATH):
    """
    Writes the to-do items list to the text file.

    :param todos_arg:
    :param filepath:
    :return: None
    """
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)
