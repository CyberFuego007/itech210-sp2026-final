import pygame
from settings import *
from collision import *

def reset_player_for_chase(player):
    player['spawn_x'] = 100
    player['spawn_y'] = 544
    player['rect'].topleft = (player['spawn_x'], player['spawn_y'])
    player['pos'] = [float(player['spawn_x']), float(player['spawn_y'])]
    player['force'] = [0.0, 0.0]

def load_chase_level(config, collider_grid):
    config['current_level'] = 'chase'
    config['message'] = "The Witch chase begins! How bout dat?"

    collider_grid.clear()

    for x in range(LEVEL[0] // CELL_SIZE):
        for y in range(LEVEL[1] // CELL_SIZE):
            collider_grid[f"{x},{y}"] = None

    add_collider_to_grid((0, 18), (75, 3), collider_grid)

#no addons in chase level
    config['hazards'] = []
    config['feathers'] = []
    config['fish'] = []
    config['enemies'] = []

#sinking ice
    config['sinking_ice'] = []

    sinking_locations = [
        (10, 18), (11, 18), (12, 18),
        (20, 18), (21, 18), (22, 18),
        (32, 18), (33, 18), (34, 18),
        (45, 18), (46, 18), (47, 18),
        (58, 18), (59, 18), (60, 18),
    ]

    for x, y in sinking_locations:
        config['sinking_ice'].append({
            'rect': pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE),
            'timer': None
        })

    config['exit_zone'] = pygame.Rect(
        73 * CELL_SIZE,
        15 * CELL_SIZE,
        2 * CELL_SIZE,
        3 * CELL_SIZE
    )

    reset_player_for_chase(config['player'])

#add witch
    config['witch'] = {
        'rect': pygame.Rect(0, 16 * CELL_SIZE, 32, 64),
        'speed': 2
    }

def update_sinking_ice(player, config):
    if config['current_level'] != "chase":
        return
    for ice in config['sinking_ice'][:]:
        if player['rect'].colliderect(ice['rect']) and ice['timer'] is None:
            ice['timer'] = 30
        if ice['timer'] is not None:
            ice['timer'] -= 1
            if ice['timer'] <= 0:
                config['sinking_ice'].remove(ice)
                grid_x = ice['rect'].x // CELL_SIZE
                grid_y = ice['rect'].y // CELL_SIZE

                config['collider_grid'][f"{grid_x},{grid_y}"] = None

def draw_sinking_ice(surface, camera, config):
    if config['current_level'] != "chase":
        return
    for ice in config['sinking_ice']:
        color = CYAN
        if ice['timer'] is not None:
            color = RED
            pygame.draw.rect(
                surface,
                color,
                (
                    ice['rect'].x - int(camera['pos'][0]),
                    ice['rect'].y - int(camera['pos'][1]),
                    ice['rect'].width,
                    ice['rect'].height 
                )
            )    
def update_witch(player, config):
    if config['current_level'] != "chase":
        return
    witch = config['witch']

    if witch['rect'].x < player['rect'].x - 80:
        witch['rect'].x += witch['speed']

    if witch['rect'].colliderect(player['rect']):
        config['game_over'] = True   

def draw_witch(surface, camera, config):
    if config['current_level'] != "chase":
        return

    witch=config.get('witch')
    if witch is None:
        return

    pygame.draw.rect(
        surface,
        PURPLE,
        (
            witch['rect'].x - int(camera['pos'][0]),
            witch['rect'].y - int(camera['pos'][1]),
            witch['rect'].width,
            witch['rect'].height
        )
    )         
