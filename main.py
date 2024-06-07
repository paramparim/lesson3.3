import pygame
import random

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Игра Тир")
icon = pygame.image.load("img/5930147.png")
pygame.display.set_icon(icon)

target_img = pygame.image.load("img/target.png")
target_width = 50
target_height = 50

target_x = random.randomint(0, SCREEN_WIDTH - target_width)
target_y = random.randomint(0, SCREEN_HEIGHT - target_height)

color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
icon = pygame.image.load("5930147.png")


running = True
while running:
    pass

pygame.quit()