import pygame
from settings import *

def create_enemy(grid_x, grid_y, left_bound, right_bound):
    return {
        'rect': pygame.Rect(grid_x * CELL_SIZE, grid_y * CELL_SIZE, 32, 32),
        'direction': 1,
        'speed': 1.5,
        'left_bound': left_bound * CELL_SIZE,
        'right_bound': right_bound * CELL_SIZE
    }

def update_enemies(enemies):
        for enemy in enemies:
            enemy['rect'].x += enemy['direction'] * enemy['speed']

            if enemy['rect'].left <= enemy['left_bound']:
                enemy['direction'] = 1

            if enemy['rect'].right >= enemy['right_bound']:
                enemy['direction'] = -1
def draw_enemies(surface,camera,enemies):
    for enemy in enemies:
        pygame.draw.rect(
            surface, 
            DARK_RED,
            (
                enemy['rect'].x - int(camera['pos'][0]),
                enemy['rect'].y - int(camera['pos'][1]),
                enemy['rect'].width,
                enemy['rect'].height
            )
        ) 
def check_enemy_damage(player, enemies, config, start_respawn):
    for enemy in enemies:
        if (
            player['rect'].colliderect(enemy['rect'])
            and not player['is_respawning']
            and player['invincible_timer'] <= 0
        ):
            config['health'] = max(0, config['health'] - 1)
            player['invincible_timer'] = 90
            if config['health'] <= 0:
                config['game_over'] = True
                return

            
            return