import pygame
from settings import *
from camera import *
from player import *
from grid import *
from collision import *


pygame.init()

def init():
    #initialize all of the game here
    pygame.display.set_caption("ITECH 210 Final")
    config = {}
    
    #collider grid
    collider_grid = grid
    for x in range(LEVEL[0]//CELL_SIZE):
        for y in range(LEVEL[1]//CELL_SIZE):
            collider_grid[f"{x},{y}"] = None
    config['collider_grid'] = collider_grid
    
    #add colliders to the grid
    add_collider_to_grid((0,18), (34,3), collider_grid)
    add_collider_to_grid((36,18), (75,3), collider_grid)
    

    #camera
    config['camera'] = camera

    #objects
    objects = []
    config['objects'] = objects

    #player
    config['player'] = player
    objects.append(player)

    
    game_loop(screen, clock, config)

def update(dt, objects):
    #all update calls are made here
    for obj in objects:
        obj['update'](dt)

def draw(surface, camera, objects):
    #all draw calls are made from here
    for obj in objects:
        obj['draw'](surface, camera)

def game_loop(screen, clock, config):
    #where the main game loop happens
    camera = config['camera']
    grid = config['collider_grid']
    objects = config['objects']
    player = config['player']

    running = True

    while running:
        dt = clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        update(dt, objects)
        update_camera(player)
        
        screen.fill(BLACK)
        draw(screen, camera, objects)

        #debug mode
        if debug:
            draw_colliders(screen, camera, grid)
            draw_grid(screen, camera, grid)
        
        pygame.display.flip()

    pygame.quit()

if __name__ == '__main__':
    init()