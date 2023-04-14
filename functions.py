FILEPATH = "todos.txt"

#def get_todos - reads the todos.txt - this function returns a value
def get_todos(filepath=FILEPATH):
    """ Read a text file and return the list of
    to-do items.
    """
    with open(filepath, 'r') as file:
        todos_local = file.readlines()
    return todos_local

#def write_todos - writes the todos.txt - this function DOES something but does not return
def write_todos(todos_arg, filepath=FILEPATH):
    """ Write the to-do items list in the txt file"""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


if __name__ == "__main__":
    print("Hello")
    print(get_todos())