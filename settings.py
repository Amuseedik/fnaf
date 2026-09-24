import pygame

pygame.init()

info = pygame.display.Info()

WIDTH = info.current_w # 1707
HEIGHT = info.current_h # 1067
print(WIDTH, HEIGHT)
FPS = 60
TITLE = "FNAF"
COLORS = {
    "black": (0, 0, 0),
    "red": (255, 0, 0) ,
    "green": (0, 255, 0) ,
    "yellow": (255, 255, 0) ,
    "blue": (0, 0, 255),
    "orange": (255, 165, 0),
    "white": (255, 255, 255),

    "light_gray": (120, 126, 140),
    "gray": (128, 128, 128),
    "dark" : (18,20,26),
    "wall": (82, 78, 68),  # тусклая серо-бежевая стена
    "floor": (45, 43, 40),  # тёмный пол
    "desk": (92, 58, 38)  # старый деревянный стол
}
FONT_NAME = "arial"
LEFT_DOOR_RECT = (0, 120, 180, 450)

RIGHT_DOOR_RECT = (1100, 120, 180, 450)

FLOOR_Y = 600

DESK_RECT = (350, 430, 580, 220)

ENERGY_BAR_RECT = (0.825*WIDTH,34,0.1*WIDTH,34)

ENERGY_LOW = (10)

ENERGY_PRE_LOW = 30
