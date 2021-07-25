def place_giant_board(main_board, x, y, player):
    main_board[y][x] = player



def empty_cell_board(board):
    empty_cell = []

    for y,row in enumerate(board):
        for x,case in enumerate(row):
            if case == 0:
                empty_cell.append([x,y])

    return empty_cell

def Check_empty_cell(board):
    if len(empty_cell_board(board)) == 0:
        print("égaliter/draw")

def Check_Horizontally(board, main_board, player):
    good = False
    for i in range(0,7, 3):
        for index, row in enumerate(board):
            if row[i] == row[i+1] == row[i+2] == player:
                good = True
            if good:
                place_giant_board(main_board)

def Check_Giant_Board(main_board, player):
    for row in main_board:
        row_stock = []
        for i in range(len(main_board)):
            row_stock.append(row[i])

        if row_stock.count(player) == len(row_stock):
            print(player, "You Win")
            return True

    for col in main_board:
        col_stock = []
        for i in range(len(main_board)):
            col_stock.append(col[i])

        if col_stock.count(player) == len(col_stock):
            print(player, "You Win")
            return True

    diag_1 = []
    for index in range(len(main_board)):
        diag_1.append(main_board[index][index])
    if len(diag_1) == diag_1.count(player):
        print(player, "You Win")
        return True

    diag_2 = []
    for index, reversed_index in enumerate(reversed(range(len(main_board)))):
        diag_2.append(main_board[index][reversed_index])
    if diag_2.count(player) == len(diag_2):
        print(player, "You Win")
        return True

    if len(empty_cell_board(main_board)) == 0:
        print("égaliter/draw")
        return True