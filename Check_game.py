def valid_location(board, main_board, x, y ,box):
    if box == None or [x,y] in box:
        if board[y][x] == 0 and main_board[y//3][x//3] ==0:
            return True
    return False

def set_location(board, main_board, x, y, player, box):
    if valid_location(board, main_board, x, y ,box):
        board[y][x] = player
        return True
    return False

def get_next_box(x,y):
    #coint haut gauche
    for i in range(0,7,3):
        for j in range(0,7,3):
            if (x,y) == (i,j):
                possible_move = []
                for k in range(3):
                    for h in range(3):
                        possible_move.append([h,k])
                return possible_move

    #coint haut milleux
    for i in range(0,7,3):
        for j in range(1,8,3):
            if (x,y) == (i,j):
                possible_move = []
                for k in range(3):
                    for h in range(3,6):
                        possible_move.append([h,k])
                return possible_move

    #coint haut droite
    for i in range(0,7,3):
        for j in range(2,9,3):
            if (x,y) == (i,j):
                possible_move = []
                for k in range(3):
                    for h in range(6,9):
                        possible_move.append([h,k])
                return possible_move

    #coint milleux gauche
    for i in range(1,8,3):
        for j in range(0,7,3):
            if (x,y) == (i,j):
                possible_move = []
                for k in range(3,6):
                    for h in range(3):
                        possible_move.append([h,k])
                return possible_move

    #coint milleux milleux
    for i in range(1,8,3):
        for j in range(1,8,3):
            if (x,y) == (i,j):
                possible_move = []
                for k in range(3,6):
                    for h in range(3,6):
                        possible_move.append([h,k])
                return possible_move

    #coint milleux droite
    for i in range(1,8,3):
        for j in range(2,9,3):
            if (x,y) == (i,j):
                possible_move = []
                for k in range(3,6):
                    for h in range(6,9):
                        possible_move.append([h,k])
                return possible_move

    #coint bas gauche
    for i in range(2,9,3):
        for j in range(0,9,3):
            if (x,y) == (i,j):
                possible_move = []
                for k in range(6,9):
                    for h in range(3):
                        possible_move.append([h,k])
                return possible_move

    #coint bas milleux
    for i in range(2,9,3):
        for j in range(1,9,3):
            if (x,y) == (i,j):
                possible_move = []
                for k in range(6,9):
                    for h in range(3,6):
                        possible_move.append([h,k])
                return possible_move

    #coint bas droite
    for i in range(2,9,3):
        for j in range(2,9,3):
            if (x,y) == (i,j):
                possible_move = []
                for k in range(6,9):
                    for h in range(6,9):
                        possible_move.append([h,k])
                return possible_move


def is_empty_box(Board,box,x,y):
    empty_cell = []
    for index, value in enumerate(box):
        if Board[value[1]][value[0]] == 0:
            empty_cell.append(value)

    if len(empty_cell) == 0:
        return False

    else:
        return True


def get_possible_move(board,x,y):
    Box = get_next_box(x,y)
    return Box

def Validate_box(board, main_board, box, x, y):
    if is_empty_box(board,box,x,y) and main_board[box[0][1]//3][box[0][1]//3] == 0:
        return box
    else:
        return empty_cell_board(board)

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
    good_line = False
    for i in range(0,7, 3):
        for index, row in enumerate(board):
            if row[i] == row[i+1] == row[i+2] == player:
                good_line = True
            if good_line:
                place_giant_board(main_board, i//3, index//3, player)
                good_line = False

def Check_Vertically(board, main_board,player):
    good_col = False

    for index in range(len(board)):
        check = []
        for i,row in enumerate(board):
            check.append(row[index])

            if len(check) >=3:
                if check.count(player) == len(check):
                    good_col = True

                    if good_col:
                        place_giant_board(main_board, index//3, i//3, player)
                        good_col = False
                        check.clear()
                check.clear()

def Check_diagonals(board,  main_board,player):
    for x in range(0, 8, 3):
        stock_index = []
        for y in range(0, 8, 3):
            stock_index.append(board[y][x])
            for i in range(1, 3):
                stock_index.append(board[y+1][x+1])

            if len(stock_index) >= 3:
                if stock_index.count(player) == len(stock_index):
                    a,b = y+i, x+i
                    place_giant_board(main_board, a//3, b//3, player)
                    stock_index.clear()
                else:
                    stock_index.clear()

    for x in range(0,9,3):
        stock_negative_index = []
        for y in range(2,9,3):
            for i in range(3):
                stock_negative_index.append(board[y-i][x+i])

                if len(stock_negative_index) >= 3:
                    if stock_negative_index.count(player) == len(stock_negative_index):
                        a,b = y-i,x+i
                        stock_negative_index.clear()
                    else:
                        stock_negative_index.clear()

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

def check_game(board, main_board, player):
    Check_Horizontally(board,main_board,player)
    Check_Vertically(board,main_board,player)
    Check_diagonals(board,main_board,player)
    Check_empty_cell(board)
