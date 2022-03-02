import pygame

cellSize = 20
board = Surface((cellSize * 8, cellSize * 8))
board.fill((255, 255, 255))
for x in range(0, 8, 2):
    for y in range(0, 8, 2):
        pygame.draw.rect(board, (0,0,0), (x*size, y*size, size, size))