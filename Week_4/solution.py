current_board = [["-","-","-"],["-","-","-"],["-","-","-"]]



def print_board(board):
    print("")
    for row in board:
        print(row)

    print("")
    print("###############")


def fillBoard (currentRow, currentCol, x_turn):  
    if(current_board[currentRow][currentCol]) == "-" and x_turn == True:
        current_board[currentRow][currentCol] = "X"

    elif(current_board[currentRow][currentCol]) == "-" and x_turn == False:
        current_board[currentRow][currentCol] = "O"

    print_board(current_board)
        
def auto_play(x_turn = True):
    for row in range(3):
        for col in range(3):
            fillBoard(row, col, x_turn)
            x_turn = not x_turn



def take_input(row_or_col):


    correct = False

    while not correct:
        print(f"Enter a {row_or_col}:")
        row_col_input = input()

        if row_col_input == "1" or row_col_input == "2" or row_col_input == "3":
            correct = True
            print(f"You have entered: {row_col_input}")
        else:
            print("You must enter 1, 2 or 3")
    
    return row_col_input

if __name__ == "__main__":
    auto_play()

