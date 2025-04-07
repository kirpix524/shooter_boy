import pygame
import random

import funcs as f

from settings import (SCREEN_HEIGHT, SCREEN_WIDTH, CAPTION,
                      MONSTERS_IMAGES_PATH, BACKGROUND_IMAGES_PATH,
                      MONSTER_SIZE, LEVEL_START_MONSTERS, LEVEL_START_BULLETS, CROSSHAIR_PATH, CROSSHAIR_SIZE)


pygame.init()
pygame.mouse.set_visible(False)  # Спрятать системный курсор
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption(CAPTION)

# Загрузка шрифта
font = pygame.font.SysFont(None, 36)

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

crosshair_img = pygame.image.load(CROSSHAIR_PATH).convert_alpha()
crosshair_img = pygame.transform.scale(crosshair_img, CROSSHAIR_SIZE)  # размер по вкусу

# Уровни
level = 1
shots_left = LEVEL_START_BULLETS
monsters = f.generate_monsters(monster_images, LEVEL_START_MONSTERS, SCREEN_WIDTH, SCREEN_HEIGHT, MONSTER_SIZE)

game_running = True
game_lost = False
clock = pygame.time.Clock()

while game_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if shots_left > 0:
                shots_left -= 1  # Тратим выстрел
                mouse_pos = pygame.mouse.get_pos()
                for monster in monsters[:]:  # копия списка
                    image, pos = monster
                    rect = pygame.Rect(pos, MONSTER_SIZE)
                    if rect.collidepoint(mouse_pos):
                        monsters.remove(monster)
                        break
    # Проверка на поражение
    if shots_left == 0 and monsters and not game_lost:
        game_lost = True
        lose_time = pygame.time.get_ticks()

    # Переход на следующий уровень, если монстров больше нет
    if not monsters:
        level += 1
        shots_left = LEVEL_START_BULLETS + (level - 1)  # Новое количество выстрелов
        monsters = f.generate_monsters(monster_images, LEVEL_START_MONSTERS + level - 1, SCREEN_WIDTH, SCREEN_HEIGHT,
                                       MONSTER_SIZE)

    # Отрисовка фона
    screen.blit(background_image, (0, 0))

    # Отрисовка монстров
    for monster in monsters:
        screen.blit(monster[0], monster[1])

    # Отрисовка текста уровня
    level_text = font.render(f"Уровень: {level}", True, (255, 0, 0))
    screen.blit(level_text, (10, 10))
    shots_text = font.render(f"Выстрелы: {shots_left}", True, (0, 0, 255))
    screen.blit(shots_text, (10, 50))

    mouse_x, mouse_y = pygame.mouse.get_pos()
    cursor_rect = crosshair_img.get_rect(center=(mouse_x, mouse_y))
    screen.blit(crosshair_img, cursor_rect.topleft)

    # Если проиграл — показываем сообщение
    if game_lost:
        lose_text = font.render("Вы проиграли!", True, (255, 0, 0))
        screen.blit(lose_text, (SCREEN_WIDTH // 2 - lose_text.get_width() // 2, SCREEN_HEIGHT // 2))

        # Через 2 секунды — сброс уровня
        if pygame.time.get_ticks() - lose_time > 2000:
            level = 1
            shots_left = LEVEL_START_BULLETS
            monsters = f.generate_monsters(monster_images, LEVEL_START_MONSTERS, SCREEN_WIDTH, SCREEN_HEIGHT,
                                           MONSTER_SIZE)
            game_lost = False
    pygame.display.flip()
    clock.tick(60)