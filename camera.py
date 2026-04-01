import pygame
from settings import *

def update_camera(target):
    camera['pos'][0] = min(max(0,target['pos'][0] - camera['view_port'][0]//2), LEVEL[0]-camera['view_port'][0])
    camera['pos'][1] = min(max(0,target['pos'][1] - camera['view_port'][1]//2), LEVEL[1]-camera['view_port'][1])

camera = {
    'pos': [0,0],
    'view_port': (WIDTH, HEIGHT)
}