from solution import *

# auto_play()

#get row and column from the user:
x_turn = True
play_counter = 0

while "-" in current_board[0] or "-" in current_board[1] or "-" in current_board[2]:

    if x_turn == True:
        for row in range(3):
            for col in range(3):
                if(current_board[row][col] == "-") and x_turn == True:
                    current_board[row][col] = "X"
                    print_board(current_board)
                    x_turn = False
                    play_counter += 1




    if x_turn == False:
        print("Enter a row and column you would like to play:")

        row = take_input("row")
        col = take_input("column")

        print(f"You have selected [{row}, {col}] to play")

        fillBoard(int(row) - 1, int(col) - 1, x_turn)
        x_turn = True

        play_counter += 1

    



