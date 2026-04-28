import pygame
pygame.font.init()

WIDTH = 1200
HEIGHT = 675
CELL_SIZE = 32
LEVEL =(75*CELL_SIZE, 22*CELL_SIZE)
GRAVITY = 1

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

#debug
debug = True

#colors
BLUE = (31, 81, 255)
WHITE =(255,255,255)
TAN = (210,180,140)
BROWN = (102,66,41)
BLACK = (0,0,0)
GREEN = (57, 255, 20)
RED_A = (255,0,0,120)
BLUE_A = (0,0,255,120)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
CYAN = (0, 180, 255)
DARK_RED = (120, 0, 0)
PURPLE = (150,0,200)

#fonts
large_font = pygame.font.SysFont("arial", 45)
small_font = pygame.font.SysFont("arial", 10)