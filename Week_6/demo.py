list_of_used_squares = []

def my_func(x, y, list_of_used_squares):

    position = (x, y)
    
    if position in list_of_used_squares:
        print("space taken")
        return False
    
    list_of_used_squares.append(position)
    return True



print(my_func(10, 22, list_of_used_squares))
print(my_func(90, 12, list_of_used_squares))
print(my_func(10, 22, list_of_used_squares))
print(list_of_used_squares)

