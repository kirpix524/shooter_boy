
def load_settings():
    settings = {}
    with open("settings.txt", "r") as file:
        for line in file:
            key, value = line.strip().split(" = ")
            settings[key] = value
    return settings

settings = load_settings()

SCREEN_WIDTH = int(settings["SCREEN_WIDTH"])
SCREEN_HEIGHT = int(settings["SCREEN_HEIGHT"])
CAPTION = settings["CAPTION"]
MONSTERS_IMAGES_PATH = settings["MONSTER_PATH"]
BACKGROUND_IMAGES_PATH = settings["BG_PATH"]
# Настройки
MONSTER_SIZE = (int(settings["MONSTER_SIZE_W"]), int(settings["MONSTER_SIZE_H"]))  # размер монстров
LEVEL_START_MONSTERS = int(settings["LEVEL_START_MONSTERS"])  # количество монстров на первом уровне