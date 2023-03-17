from functions import get_todos, write_todos
import time

now = time.strftime('%b %d, %Y %M:%H:%S')
print('It is', now)
while True:

    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:]  # removes 'add' from user input and obtains todo

        todos = get_todos()
        todos.append(todo + '\n')  # adds new user todo to any previously existing todos stored in the 'todos' list obj

        write_todos(todos)

    elif user_action.startswith("show"):

        todos = get_todos()

        if not todos:  # checks if todo list is empty
            print('No todos available')
        else:
            # todos = [x.strip('\n') for x in todos]  # this removes the extra \n produced by file.readlines()
            print("This is your todo list:")
            for index, todo in enumerate(todos):
                todo = todo.strip('\n')  # this removes the extra \n produced by file.readlines()
                print(f'{index + 1}. {todo.capitalize()}')  # outputs the user's todos in a numbered list form

    elif user_action.startswith("edit"):

        todos = get_todos()

        if not todos:  # checks if todo list is empty
            print('No todos available')
        else:
            try:
                print("This is your todo list: ")  # shows user their current todo list
                for index, todo in enumerate(todos):
                    todo = todo.strip('\n')
                    print(f'{index + 1}. {todo.capitalize()}')

                number = int(input('Enter the number of the todo to edit: '))

                edited_todo = input('What would you like to put instead?\n')
                todos[number - 1] = edited_todo + '\n'  # replaces selected to do with edited version

                write_todos(todos)

                print(f'Edit successful: \'{edited_todo.capitalize()}\'')  # shows edit was successful
            except ValueError:
                print("Please input the number of the todo to edit: ")
                continue

    elif user_action.startswith("complete"):

        todos = get_todos()

        if not todos:  # checks if todo list is empty
            print('No todos available')
        else:
            try:
                completed_todo_index = int(input("Enter the number of the todo to mark complete: "))
                index = completed_todo_index - 1
                todo_to_remove = todos[index].strip('\n')
                todos.pop(index)

                write_todos(todos)

                print(f"Todo '{todo_to_remove.capitalize()}' completed. Great job!")
            except IndexError:
                print('You don\'t have that many todos in your list')
                continue

    elif user_action.startswith("exit"):
        break
    else:  # provides a case for if user inputs something other than add, show or exit
        print('You entered an unknown command')
