import pygame
from settings import *
   
def draw_grid(surface, camera, grid):
    for key,val in grid.items():
        pos = key.split(',')
        x = int(pos[0])*CELL_SIZE - camera['pos'][0]
        y = int(pos[1])*CELL_SIZE - camera['pos'][1]
        
        pygame.draw.rect(surface, WHITE, pygame.Rect((x,y), (CELL_SIZE,CELL_SIZE)), 1)
        font = small_font.render(key, True, WHITE)
        rect = font.get_rect(center=(x+CELL_SIZE//2, y+CELL_SIZE//2))
        surface.blit(font, rect) 

def get_world_pos_to_grid(pos):
    x = pos[0]//CELL_SIZE
    y = pos[1]//CELL_SIZE
    return (x,y)

def get_grid_to_world_pos(pos):
    x = pos[0]*CELL_SIZE
    y = pos[1]*CELL_SIZE
    return (x,y)

grid = {}