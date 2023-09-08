explored = {}

position = (10, 10)
objectLeft = "Left"
objectRight = "Right"

explored.update({position : objectLeft})

explored.update({(8,6):objectRight})

new_position = (10,10)

safe_to_move = False

for key in explored:
    if key == new_position:
        print("I can not move here")
    else:
        safe_to_move = True

if safe_to_move:            
    explored.update({new_position : objectRight})
        


print(explored)