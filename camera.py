import pygame
from settings import *

camera = {
    'pos': [0, 0],
    'view_port': (WIDTH, HEIGHT)
}

def update_camera(target):
    target_x = target['rect'].centerx - camera['view_port'][0] // 2

    camera['pos'][0] += (target_x - camera['pos'][0]) * 0.10
    camera['pos'][1] = 0
    camera['pos'][0] = max(0, min(camera['pos'][0], LEVEL[0] - camera['view_port'][0]))


camera = {
    'pos': [0, 0],
    'view_port': (WIDTH, HEIGHT)
}