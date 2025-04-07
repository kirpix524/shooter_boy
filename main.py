import pygame
import random
import funcs as f

from settings import SCREEN_HEIGHT, SCREEN_WIDTH, CAPTION, MONSTERS_IMAGES_PATH, BACKGROUND_IMAGES_PATH, MONSTER_SIZE, LEVEL_START_MONSTERS


pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption(CAPTION)

bg_images = f.load_images(BACKGROUND_IMAGES_PATH)
# Проверка, есть ли изображения
if not bg_images:
    raise FileNotFoundError(f"Нет подходящих файлов в папке {BACKGROUND_IMAGES_PATH}")

# Загрузка изображений монстров
monster_images_paths = f.load_images(MONSTERS_IMAGES_PATH)
if not monster_images_paths:
    raise FileNotFoundError(f"Нет подходящих файлов в папке {MONSTERS_IMAGES_PATH}")

background_path = random.choice(bg_images)
background_image = pygame.image.load(background_path).convert()
background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

monster_images = [pygame.image.load(path).convert_alpha() for path in monster_images_paths]
monster_images = [pygame.transform.scale(img, MONSTER_SIZE) for img in monster_images]

# Уровни
level = 1
monsters = f.generate_monsters(monster_images, LEVEL_START_MONSTERS, SCREEN_WIDTH, SCREEN_HEIGHT, MONSTER_SIZE)

game_running = True
clock = pygame.time.Clock()

while game_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # Переход на следующий уровень
                level += 1
                monsters = f.generate_monsters(monster_images, LEVEL_START_MONSTERS + level - 1, SCREEN_WIDTH, SCREEN_HEIGHT, MONSTER_SIZE)

    # Отрисовка
    screen.blit(background_image, (0, 0))

    for monster in monsters:
        screen.blit(monster[0], monster[1])

    pygame.display.flip()
    clock.tick(60)