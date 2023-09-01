

print(bool(None))
print(bool(False))
print(bool(0))
print(bool(0.0))
print(bool([]))
print(bool({}))
print(bool(()))
print(bool(''))
print(bool(range(0)))
print(bool(set()))

my_list = [10,222,22,33,111]

number1 = 88
number2 = 99

if number1 in my_list:
    print("Hello 88")
elif number2 in my_list:
    print("Hello 99")
else:
    print("Nothin in the list that i like")

directions = ["E", "W", "A", "S", "N", "N", "N", "E", "E"]
current_position = (0,0)
places_travelled = []

for direction in directions:
    match direction:
        case "N":
            position_x = current_position[0]
            position_y = current_position[1] + 1
            current_position = (position_x, position_y)
            print(f"Move North to position: {current_position}")
        case "E":
            position_x = current_position[0] + 1
            position_y = current_position[1]
            current_position = (position_x, position_y)
            print(f"Move East to position: {current_position}")
        case "S":
            position_x = current_position[0]
            position_y = current_position[1] - 1
            current_position = (position_x, position_y)
            print(f"Move South to position: {current_position}")
        case "W":    
            position_x = current_position[0] - 1
            position_y = current_position[1]
            current_position = (position_x, position_y)  
            print(f"Move West to position: {current_position}")
        case _:
            print("I dont know which way to go")
    
    places_travelled.append(current_position)

print(places_travelled)

