import pygame
import os
import random
from board import New_Board
from window import draw_board, draw_piece, draw_giant_piece
from Check_game import set_location,check_game,get_possible_move,Validate_box,Check_Giant_Board

pygame.font.init()

Size_Width, Size_Height = 810,810
Giant_Square = Size_Width//3
Square = Giant_Square//3

Window = pygame.display.set_mode((Size_Width,Size_Height))
pygame.display.set_caption("test de jeu")
Clock = pygame.time.Clock()

Cross = pygame.transform.scale(pygame.image.load(os.path.join("Assets",'croix.png')), (Square, Square))
Circle = pygame.transform.scale(pygame.image.load(os.path.join("Assets",'cible.png')), (Square, Square))
Giant_Cross = pygame.transform.scale(pygame.image.load(os.path.join("Assets",'croix.png')), (Giant_Square, Giant_Square))
Giant_Circle = pygame.transform.scale(pygame.image.load(os.path.join("Assets",'cible.png')), (Giant_Square, Giant_Square))

Background = (0,0,0)
Color_Lige = (255,255,255)
Color_Lige_2 = (255,0,0)

Board = New_Board()

def update_window(Window, main_board, small_board):
    pygame.display.update()
    draw_piece(Window, small_board, Square, Cross,Circle)
    draw_board(Window, Color_Lige, Color_Lige_2, Size_Width, Size_Height, Giant_Square, Square)
    draw_giant_piece(Window,main_board,Giant_Square,Giant_Cross,Giant_Circle)

def main():

    run = True
    game_over = False

    main_board = Board.create_board()
    small_board = Board.giant_board()

    box = None
    Player_1 = 1
    Player_2 = -1
    turn = random.choices([1,-1])

    while run:
        #les FPS
        Clock.tick(60)

        update_window(Window, main_board, small_board)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
                run = False
            #nouvelle partie
            if event.type == pygame.KEYDOWN and game_over:
                if event.key == pygame.K_SPACE and game_over:
                    game_over = False
            #clicer sur les cases
            if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
                if pygame.mouse.get_pressed()[0]:
                    position = pygame.mouse.get_pos()

                    if set_location(small_board,main_board,position[0]//(Square),position[1]//(Square),turn, box):

                        check_game(small_board,main_board,turn)
                        new_box = get_possible_move(small_board,position[0]//(Square),position[1]//(Square))

                        box = Validate_box(small_board, main_board, new_box, position[0]//(Square),position[1]//(Square))

                        if Check_Giant_Board(main_board,turn):
                            game_over = True

                        if turn == Player_1:
                            turn = Player_2
                        else:
                            turn = Player_1



main()