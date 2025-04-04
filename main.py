import pygame
import random
import funcs as f

from settings import SCREEN_HEIGHT, SCREEN_WIDTH, CAPTION, MONSTERS_IMAGES_PATH, BACKGROUND_IMAGES_PATH


pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption(CAPTION)

bg_images = f.load_images(BACKGROUND_IMAGES_PATH)
# Проверка, есть ли изображения
if not bg_images:
    raise FileNotFoundError(f"Нет подходящих файлов в папке {BACKGROUND_IMAGES_PATH}")

background_path = random.choice(bg_images)
background_image = pygame.image.load(background_path).convert()
background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

game_running = True
while game_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False

    screen.blit(background_image, (0, 0))
    pygame.display.flip()