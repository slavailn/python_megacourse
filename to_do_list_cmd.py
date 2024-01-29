# To do list command line utility

todos = []

while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action == "add":
        todo = input("Enter a todo item: ")
        todos.append(todo)
    elif user_action == "show" or user_action == "display":
        for index, item in enumerate(todos):
            print( f"{index + 1}::{item}" )
    elif user_action == "edit":
        selected_item = input("Please, enter a number of a todo item to edit! ")
        selected_item = int(selected_item)
        new_todo = input("Please, modify a todo item: ")
        todos[selected_item - 1] = new_todo
    elif user_action == "complete":
        item_remove = int(input("Please, enter a number of a todo item to remove! "))
        print(f"Item {todos[item_remove - 1]} was removed from the list!")
        todos.pop(item_remove - 1)
    elif user_action == "exit":
        break
    else:
        print("Unknown command!")

print("Bye!")
