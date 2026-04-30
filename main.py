import pygame
from settings import *
from camera import *
from player import *
from grid import *
from collision import *
from enemies import *
from level import *

pygame.init()

def init():
    #initialize all of the game here
    pygame.display.set_caption("Chase Me Outside, How bout dat")
    config = {}
    
    #collider grid
    collider_grid = grid
    collider_grid.clear()
    for x in range(LEVEL[0]//CELL_SIZE):
        for y in range(LEVEL[1]//CELL_SIZE):
            collider_grid[f"{x},{y}"] = None
        config['collider_grid'] = collider_grid


    #background
    config['background'] = pygame.image.load("media/map.png").convert()


    #add colliders to the grid
    #ground
    add_collider_to_grid((0,18), (34,3), collider_grid) #0-33
    add_collider_to_grid((36,18), (16,3), collider_grid) #36-51 
    add_collider_to_grid((56,18), (19,3), collider_grid) #56-74
    #branches
    add_collider_to_grid((33,15), (2,1), collider_grid)
    add_collider_to_grid((38,13), (3,1), collider_grid)
    add_collider_to_grid((44,15), (3,1), collider_grid)
    add_collider_to_grid((50,14), (2,1), collider_grid)
    add_collider_to_grid((53,13), (3,1), collider_grid)
    
    config['collider_grid'] = collider_grid
    
    #hazards
    hazards = []

    #cracked ice/pit hazard
    hazards.append(pygame.Rect(34 * CELL_SIZE, 18 * CELL_SIZE, 2 * CELL_SIZE, 3 * CELL_SIZE ))
    hazards.append(pygame.Rect(52 * CELL_SIZE, 18 * CELL_SIZE, 6 * CELL_SIZE, 3 * CELL_SIZE ))
    config ['hazards'] = hazards

    #feathers
    feathers = []

    #early ground
    feathers.append(pygame.Rect(6 * CELL_SIZE, 16 * CELL_SIZE, 16, 16 ))
    feathers.append(pygame.Rect(14 * CELL_SIZE, 14 * CELL_SIZE, 16, 16 ))
    feathers.append(pygame.Rect(24 * CELL_SIZE, 16 * CELL_SIZE, 16, 16 ))

    #pit/branch
    feathers.append(pygame.Rect(33 * CELL_SIZE, 14 * CELL_SIZE, 16, 16 ))
    feathers.append(pygame.Rect(39 * CELL_SIZE, 12 * CELL_SIZE, 16, 16 ))
    feathers.append(pygame.Rect(44 * CELL_SIZE, 14 * CELL_SIZE, 16, 16 ))

    #next branch
    feathers.append(pygame.Rect(50 * CELL_SIZE, 13 * CELL_SIZE, 16, 16 ))
    feathers.append(pygame.Rect(53 * CELL_SIZE, 12 * CELL_SIZE, 16, 16 ))

    #last part of map
    feathers.append(pygame.Rect(62 * CELL_SIZE, 16 * CELL_SIZE, 16, 16 ))
    feathers.append(pygame.Rect(70 * CELL_SIZE, 14 * CELL_SIZE, 16, 16 ))
    
    config['feathers'] = feathers
    config['score'] = 0

    #fish
    fish = []

    #fish on map
    fish.append(pygame.Rect(31 * CELL_SIZE, 17 * CELL_SIZE, 16, 16))
    fish.append(pygame.Rect(51 * CELL_SIZE, 17 * CELL_SIZE, 16, 16))
    fish.append(pygame.Rect(64 * CELL_SIZE, 17 * CELL_SIZE, 16, 16))

    config['fish'] = fish
    config['health'] = 3
    config['max_health'] = 3

    #enemy
    enemies = []

    enemies.append(create_enemy(40, 17, 36, 51))
    enemies.append(create_enemy(60, 17, 56, 74))

    config['enemies'] = enemies

    #camera
    config['camera'] = camera

    #objects
    objects = []
    config['objects'] = objects

    #player
    config['player'] = player
    objects.append(player)
    
    #game over
    config['game_over'] = False

    #game won
    config['game_won'] = False
    
    #level
    config['current_leve'] = 'escape'
    config['message'] = ""
    config['game_won'] = False
    config['sinking_ice'] = []
    config['exit_zone'] = pygame.Rect(
        73 * CELL_SIZE,
        15 * CELL_SIZE,
        2 * CELL_SIZE,
        3 * CELL_SIZE
    )

    #sinking ice
    config['current_level'] = "escape"
    config['message'] = ""
    config['game_won'] = False
    config['sinking_ice'] = []

    #exit zone
    config['exit_zone'] = pygame.Rect(
        73 * CELL_SIZE,
        15 * CELL_SIZE,
        2 * CELL_SIZE,
        3 * CELL_SIZE
    )

    #gameloop
    game_loop(screen, clock, config)

def update(dt, objects, config):
    #all update calls are made here
    for obj in objects:
        obj['update'](dt)
    player = config['player']

     #respawn delay
    if player['is_respawning']:
        player['respawn_timer'] -= 1
        if player['respawn_timer'] <= 0:
            finish_respawn(player)
        return

    #hazards
    hazards = config['hazards'] 
    for hazard in hazards:
        if (
            player['rect'].colliderect(hazard) 
            and not player['is_respawning']
            and player['invincible_timer'] <= 0
        ):
            config['health'] = max(0, config['health'] - 1)
            
            if config['health'] <= 0:
                config['game_over'] = True
                
            start_respawn(player)
            return
    #update sinking ice
    update_sinking_ice(player, config)

    #enemies
    update_enemies(config['enemies'])
    check_enemy_damage(player, config['enemies'], config, start_respawn)

    #invincible countdown
    if player['invincible_timer'] > 0:
        player['invincible_timer'] -=1
    
    #feather
    feathers = config['feathers']
    for feather in feathers[:]:
        if player['rect'].colliderect(feather):
            feathers.remove(feather)
            config['score'] += 10
    
    #fish
    fish = config['fish']
    for fish_pickup in fish[:]:
        if player['rect'].colliderect(fish_pickup):
            if config['health'] < config['max_health']:
                config['health'] += 1
            config['fish'].remove(fish_pickup)

    #level transition
    if player['rect'].colliderect(config['exit_zone']):
        if config['current_level'] == "escape":
            if config['score'] >= 100:
                load_chase_level(config, config['collider_grid'])
            else:
                config['message'] = "Collect 100 points first!"

        elif config['current_level'] == "chase":
            config['message'] = "You reached shore!!"
            config['game_won'] = True
    


def draw(surface, camera, objects, config):
    #background draw
    bg_y = HEIGHT - config['background'].get_height() + CELL_SIZE
    surface.blit(config['background'], (-int(camera['pos'][0]), bg_y))

    #all draw calls are made from here
    for obj in objects:
        obj['draw'](surface, camera)
    for hazard in config['hazards']:
        pygame.draw.rect(
            surface,
            RED,
            (
                hazard.x - camera['pos'][0],
                hazard.y - camera['pos'][1],
                hazard.width,
                hazard.height
            )
        )
    #draw enemies
    draw_enemies(surface, camera, config['enemies'])

    #draw feather
    for feather in config['feathers']:
        pygame.draw.rect(
            surface,
            YELLOW,
            (
                feather.x - int(camera['pos'][0]),
                feather.y - int(camera['pos'][1]),
                feather.width,
                feather.height
            )
        )
    
    #draw fish
    for fish_pickup in config['fish'][:]:
        pygame.draw.rect(
            surface,
            CYAN,
            (
                fish_pickup.x - int(camera['pos'][0]),
                fish_pickup.y - int(camera['pos'][1]),
                fish_pickup.width,
                fish_pickup.height
            )
        )

    #draw score
    score_text = large_font.render(f"Score: {config['score']}", True, WHITE)
    surface.blit(score_text, (10, 60))

    #draw health
    health_text = large_font.render(f"Health: {config['health']}", True, WHITE)
    surface.blit(health_text, (10,10))

    #draw sinking ice
    draw_sinking_ice(surface, camera, config)

    #draw game over
    if config['game_over']:
        game_over_text = large_font.render("GAME OVER", True, RED)
        surface.blit(game_over_text, (WIDTH // 2 - 150, HEIGHT //2))
    
    #draw witch
    draw_witch(surface, camera, config)

    #draw exit zone
    pygame.draw.rect(
        surface,
        GREEN,
        (
            config['exit_zone'].x - int(camera['pos'][0]),
            config['exit_zone'].y - int(camera['pos'][1]),
            config['exit_zone'].width,
            config['exit_zone'].height
        )
    )
    #draw game won
    if config['game_won']:
        win_text = large_font.render("YOU MADE IT TO SHORE!", True, WHITE)
        surface.blit(win_text, (WIDTH // 2 - 250, HEIGHT // 2))



def start_respawn(player):
    #delay before respawn
    player['is_respawning'] = True
    player['respawn_timer'] = 45  #-.75 secs at 60 fps
    player['invincible_timer'] = 90
    player['force'] = [0.0, 0.0]

def finish_respawn(player):
    #spawn to beginning
    player['rect'].topleft = (player['spawn_x'], player['spawn_y'])
    player['pos'] = [float(player['spawn_x']), float(player['spawn_y'])]
    
    #reset movement    
    player['force'] = [0.0, 0.0]

    #turn off respawn state
    player['is_respawning'] = False

    #invincible (blinking)
    player['invincible_timer'] = 90 #1.5 seconds

def check_level_transition(player,config):
    if player['rect'].colliderect(config['exit_zone']):
        if config['score'] >= 100:
            config['current_level'] = "chase"
            config['message'] = "Witch chase begins! How bout dat?"
        else:
            config['message'] = "Collect all feathers!"

def game_loop(screen, clock, config):
    #where the main game loop happens
    camera = config['camera']
    grid = config['collider_grid']
    objects = config['objects']
    player = config['player']
    hazards = config['hazards']


    running = True

    while running:
        dt = clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        update(dt, objects, config)
        update_camera(player)
        
        #screen.fill(BLACK)
        draw(screen, camera, objects, config)

        #debug mode
        if debug:
            pass
            #draw_colliders(screen, camera, grid)
            #draw_grid(screen, camera, grid)
        
        pygame.display.flip()

    pygame.quit()

if __name__ == '__main__':
    init()