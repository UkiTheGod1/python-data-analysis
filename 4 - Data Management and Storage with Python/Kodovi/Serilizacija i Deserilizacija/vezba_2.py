import os
import pickle
 
todos = []
 
if os.path.exists('todos.pkl'):
    with open('todos.pkl', 'rb') as file:
        todos = pickle.load(file)
 
running = True
 
while running:
 
    command = input("What you want to do?\nread(1)\nremove(2)\nadd(3)\nexit(4)\n")
 
    if command == '1':
        if(len(todos) == 0):
            print('\nNo todos.\n')
        else:
            print("\nAll todo's:")
            for index in range(len(todos)):
                print(f"{index+1}. {todos[index]}")
            print('\n')
    elif command == '2':
        index = input("\nEnter the number of todo you want to delete?\n")
        index = int(index) - 1
        if (0 <= index) and (index < len(todos)):
            todos.remove(todos[index])
            with open('todos.pkl', 'wb') as file:
                pickle.dump(todos, file)
            print('\nTodo removed.\n')
        else:
            print('\nTodo does not exists.\n')
    elif command == '3':
        todo = input("\nTodo:")
        todos.append(todo)
        with open('todos.pkl', 'wb') as file:
            pickle.dump(todos, file)
        print(f"\nYou have added new todo.\n")
    elif command == '4':
        running = False
    else:
        print("\nWrong command.\n")
 
print("\nGoodbye!")