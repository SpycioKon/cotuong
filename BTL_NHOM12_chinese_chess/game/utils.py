import pygame

pygame.font.init()

WIN_WIDTH = 900
WIN_HiGHT = 600

RED_SIDE = 1
BLUE_SIDE = 0

class Font:
    SCORE_TEXT_FONT = pygame.font.Font("./fonts/CursedTimerUlil-Aznm.ttf", 30)
    SCORE_FONT = pygame.font.Font("./fonts/CursedTimerUlil-Aznm.ttf", 30)
    NORMAL_FONT = pygame.font.Font("./fonts/Poppins-Bold.ttf", 30)
    WRITING_FONT = pygame.font.Font("./fonts/Allison-Regular.ttf", 30)

class ChessImage:
    BlueBodyGuard = pygame.image.load("./images/pieces/blue-bodyguard.png")
    BlueCannon = pygame.image.load("./images/pieces/blue-cannon.png")
    BlueCar = pygame.image.load("./images/pieces/blue-car.png")
    BlueElephants = pygame.image.load("./images/pieces/blue-elephant.png")
    BlueHourse = pygame.image.load("./images/pieces/blue-horse.png")
    BlueKing = pygame.image.load("./images/pieces/blue-king.png")
    BlueSoldier = pygame.image.load("./images/pieces/blue-pawn.png")

    RedBodyGuard = pygame.image.load("./images/pieces/red-bodyguard.png")
    RedCannon = pygame.image.load("./images/pieces/red-cannon.png")
    RedCar = pygame.image.load("./images/pieces/red-car.png")
    RedElephants = pygame.image.load("./images/pieces/red-elephant.png")
    RedHourse = pygame.image.load("./images/pieces/red-horse.png")
    RedKing = pygame.image.load("./images/pieces/red-king.png")
    RedSoldier = pygame.image.load("./images/pieces/red-pawn.png")

class Colour:
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 255, 0)
    YELLOW = (255, 255, 0)
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    PURPLE = (128, 0, 128)
    ORANGE = (255, 165, 0)
    GREY = (128, 128, 128)
    TURQUOISE = (64, 224, 208)

