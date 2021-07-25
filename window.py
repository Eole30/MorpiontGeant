import  pygame

def draw_giant_piece(Window, main_board, Giant_Square, Giant_Cross, Giant_Circle):
    for x in range(len(main_board)):
        for y in range(len(main_board)):
            if main_board[y][x] == -1:
                Window.blit(Giant_Circle, (x*Giant_Square, y*Giant_Square))

            if main_board[y][x] == 1:
                Window.blit(Giant_Cross, (x*Giant_Square, y*Giant_Square))

def draw_piece(Window, board, Square, Cross, Circle):
    for x in range(len(board)):
        for y in range(len(board)):
            if board[y][x] == -1:
                Window.blit(Circle, (x * Square, y * Square))

            if board[y][x] == 1:
                Window.blit(Cross, (x * Square, y * Square))

def draw_board(Window, Color_line, Color_line_2, Width, Height, Giant_Square, Square):

    for move in range(0,3):
        for ab in range(0,3):
            for x in range(1,3):
                pygame.draw.line(Window, Color_line_2, (Giant_Square*move, (x*Square)+ab*Giant_Square), (Giant_Square+Giant_Square*move, (x*Square)+ab*Giant_Square), 1)

        for ba in range(0, 3):
            for x in range(1, 3):
                pygame.draw.line(Window, Color_line_2, ((x * Square) + ba * Giant_Square, Giant_Square * move), ((x * Square) + ba * Giant_Square, Giant_Square + Giant_Square * move), 1)

    for i in range(1,3):
        pygame.draw.line(Window, Color_line, (0,Giant_Square*i),(Width, Giant_Square*i),2)
        pygame.draw.line(Window, Color_line, (Giant_Square * i,0), (Giant_Square * i, Height), 2)