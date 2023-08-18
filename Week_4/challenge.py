# Challenge:
# Create a stupid automatic tic tac toe player.
# If x_turn is true, then it is the x players go.
# put an "X" in the next available spot.
# Otherwise, it is the o players go.
# put an "O" in the next available spot.
#
# Should print like this when done:
# ['X', 'O', 'X']
# ['O', 'X', 'O']
# ['X', 'O', 'X']
# 
# Use: loops, if/else, functions and modules.

current_board = [["-","-","-"],["-","-","-"],["-","-","-"]]

x_turn = True

for row in current_board:
    print(row)

print("#################")

if(current_board[0][0]) == "-" and x_turn:
    current_board[0][0] = "X"


for row in current_board:
    print(row)
