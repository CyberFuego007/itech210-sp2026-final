import pygame 
from settings import *
from collision import *
from grid import *


def get_player_input():
    player_input = {
        'LEFT':False,
        'RIGHT':False,
        'JUMP':False,
    }
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_a]:
            player_input['LEFT'] = True
    if pressed[pygame.K_d]:
        player_input['RIGHT'] = True
    if pressed[pygame.K_SPACE]:
        player_input['JUMP'] = True

    return player_input
 
def draw_player(surface, camera):
    pos = (player['pos'][0]-camera['pos'][0], player['pos'][1]-camera['pos'][1])
    pygame.draw.rect(surface, GREEN, (pos, player['size']))

def update_player(dt): 
    input = get_player_input()
    
    #check for on ground
    ghost_rect = player['rect'].move(0,1) #1 pixel below player
    on_ground = len(get_collisions(ghost_rect)) > 0

   #print("Player pos:", player['rect'].topleft, "On ground:", on_ground) *used to find level

    #movement adjustment
    friction = 0.03
    max_speed = 4.5
    air_control = 0.08
    jump_strength = -50 #adjust to fix jump height

    #gravity section
    if on_ground:
       if player['force'][1] > 0:
            player['force'][1] =0
    else:
        player['force'][1] += GRAVITY * dt
           
    #get inputs
    if input.get('LEFT'):
        if on_ground:
            player['force'][0] -= player['speed'] * dt
        else:
            player['force'][0] -= player['speed'] * air_control * dt
    if input.get('RIGHT'):
        if on_ground:
            player['force'][0] += player['speed'] * dt
        else:
            player['force'][0] += player['speed'] * air_control * dt
    if input.get('JUMP') and on_ground:
        player['force'][1] = jump_strength
        player['force'][0] *= 0.9
    
    #friction
    if not input.get('LEFT') and not input.get('RIGHT'):
        if player['force'][0] > 0:
            player['force'][0] -= friction * dt
            if player['force'][0] < 0:
                player['force'][0] = 0
        elif player['force'][0] < 0:
            player['force'][0] += friction * dt
            if player['force'][0] > 0:
                player['force'][0] = 0

    #horizontal speed
    if player['force'][0] > max_speed:
        player['force'][0] = max_speed
    if player['force'][0] < -max_speed:
        player['force'][0] = -max_speed

   #fall speed
    player['force'][1] = min(player['force'][1], GRAVITY*8)

    #keep player inbounds on screen
    #left wall
    if player['rect'].left <= 0 and player['force'][0] < 0:
        player['force'][0] = 0
    #right wall will work on this later!
    #if player['rect'].right >= WIDTH and player['force'][0] > 0:
        #player['force'][0] = 0


    move_player(player)
    

def move_player(player):
    test_rect = player['rect'].move(player['force'])
    hits = get_collisions(test_rect)
    
    if len(hits) == 0:
        player['pos'] = test_rect.topleft
        player['rect'].topleft = player['pos']
    else:
        #handle x position
        test_x = player['rect'].move((player['force'][0], 0))
        hits_x = get_collisions(test_x)
        for h in hits_x:
            if player['force'][0]>0: #moving right
                test_x.x = h.left - player['size'][0]
            if player['force'][0]<0: #moving left
                test_x.x = h.right
            
            player['force'][0] = 0

        player['pos'] = test_x.topleft
        player['rect'].topleft = player['pos']

        #handle y position
        test_y = player['rect'].move((0,player['force'][1]))
        hits_y = get_collisions(test_y)

        for h in hits_y:
            if player['force'][1]>0: #moving down
                test_y.y = h.top - player['size'][1]
            if player['force'][1]<0: #moving up
                test_y.y = h.bottom
            
            player['force'][1] = 0

        player['pos'] = test_y.topleft
        player['rect'].topleft = player['pos']

#player spawn
spawn_x = 100
spawn_y = 544


player = {
    'spawn_x': spawn_x,
    'spawn_y': spawn_y,
    'pos': [spawn_x, spawn_y],
    'size': [32,32],
    'rect': pygame.Rect([spawn_x, spawn_y], [32,32]),
    'speed': .4,
    'force':  [0.0, 0.0], 
    'update': update_player,
    'draw': draw_player,
    'color': GREEN
}