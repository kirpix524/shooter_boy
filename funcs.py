import os
import random

def load_images(path):
    # Загружаем все изображения из папки
    images = [
        os.path.join(path, f)
        for f in os.listdir(path)
        if f.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp'))
    ]
    return images

def generate_monsters(monster_images, count, screen_w, screen_h, monster_size):
    monsters = []
    for _ in range(count):
        image = random.choice(monster_images)
        x = random.randint(0, screen_w - monster_size[0])
        y = random.randint(0, screen_h - monster_size[1])
        monsters.append((image, (x, y)))
    return monsters

