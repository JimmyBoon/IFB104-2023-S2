# number = 8

# match number == 8:
#     case True:
#         print("the number is eight is also good")
#     case False:
#         print("the number is not eight which is good")
#     case _:
#         print(f"the number is {number} which is not so good")


# if number == 8:
#     print("the number is one is also good")
# else:
#     print(f"the number is {number} which is not so good")


# direction = "South"



def process_direction(direction):
    assert isinstance(direction,str), "Direction needs to be a string"

    position_x = 0
    position_y = 0

    match direction:
        case "North":
            position_y += 1
        case "South":
            position_y -= 1
        case "East":
            position_x += 1
        case "West":
            position_x -= 1
        case _:
            assert False, "Error reading direction"

    return position_x, position_y


print(process_direction(32))

