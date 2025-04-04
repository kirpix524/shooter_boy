import os

def load_images(path):
    # Загружаем все изображения из папки
    images = [
        os.path.join(path, f)
        for f in os.listdir(path)
        if f.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp'))
    ]
    return images


