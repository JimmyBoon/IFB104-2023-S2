shopping_list = ["apples", "pears"]

def add_to_shopping_list(item, my_list):
    if isinstance(item, str) == False:
        print("item is not string")
        return

    my_list.append(item)
    print(my_list)

add_to_shopping_list("food", shopping_list)
