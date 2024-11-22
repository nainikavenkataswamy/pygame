import pygame

# Initialize Pygame
pygame.init()

# Set frames per second
FPS = 60
clock = pygame.time.Clock()

# Load fonts
font = pygame.font.Font("./assets/font/myFont.ttf", 28)
big_font = pygame.font.Font("./assets/font/myFont.ttf", 55)

# Set the window title
pygame.display.set_caption(" Shooting Game")

# Load images for menus and game over screen
menu_img = pygame.image.load("./assets/menus/mainMenu.png")
game_over_img = pygame.image.load("./assets/menus/gameOver.png")
pause_img = pygame.image.load("./assets/menus/pause.png")

# Initialize mixer for sounds
pygame.mixer.init()
pygame.mixer.music.load("./assets/sounds/bg_music.mp3")
plate_sound = pygame.mixer.Sound("./assets/sounds/Broken plates.wav")
plate_sound.set_volume(0.1)
bird_sound = pygame.mixer.Sound("./assets/sounds/Drill Gear.mp3")
bird_sound.set_volume(0.2)
laser_sound = pygame.mixer.Sound("./assets/sounds/Laser Gun.wav")
laser_sound.set_volume(0.2)
pygame.mixer.music.play()
pygame.mixer.music.set_volume(0.5)

# Set up screen dimensions
# WIDTH = 900
# HEIGHT = 800
WIDTH = 700
HEIGHT = 600
screen = pygame.display.set_mode([WIDTH, HEIGHT])
