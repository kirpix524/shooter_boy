
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