import pygame
from settings import * 
from grid import *

def get_collisions(rect, radius=1):
    colliders = []
    collider_grid = grid
    
    #convert rect to cell
    top_left = get_world_pos_to_grid((rect.left, rect.top))
    bottom_right = get_world_pos_to_grid((rect.left+rect.width, rect.top+rect.height))
   
    #general - get colliders in a radius around rect
    general = []
    for x in range(top_left[0]-radius, bottom_right[0]+radius+1):
        for y in range(top_left[1]-radius, bottom_right[1]+radius+1):
            collider = collider_grid.get(f"{x},{y}")
            if collider is not None and collider not in general:
                general.append(collider)
   
    #specific - check each of the colliders from general
    for collider in general:
        if rect.colliderect(collider) and collider not in colliders:
            colliders.append(collider)
    
    return colliders

def add_collider_to_grid(pos, size, grid):
    #pos and size are tuples in cell coordinates

    rect = pygame.Rect(get_grid_to_world_pos(pos), (size[0]*CELL_SIZE, size[1]*CELL_SIZE))
    for x in range(pos[0], pos[0]+size[0]):
        for y in range(pos[1], pos[1]+size[1]):
            grid[f"{x},{y}"] = rect

def draw_colliders(surface, camera, grid):
    for key,val in grid.items():
        pos = key.split(',')
        x = int(pos[0])*CELL_SIZE - camera['pos'][0]
        y = int(pos[1])*CELL_SIZE - camera['pos'][1]
        if val is not None:
            col_surface = pygame.Surface((CELL_SIZE, CELL_SIZE), pygame.SRCALPHA)
            pygame.draw.rect(col_surface, BLUE_A, col_surface.get_rect())
            surface.blit(col_surface, (x,y))
 