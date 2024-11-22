import pygame
import math

lasers = ["red", "purple", "green"]


# Function to draw the gun based on mouse position
def draw_gun(guns, lasers, level, WIDTH, HEIGHT, screen):
    mouse_pos = pygame.mouse.get_pos()  # Get mouse position
    gun_point = (WIDTH / 2, HEIGHT - 200)  # Define gun position
    clicks = pygame.mouse.get_pressed()  # Get mouse click state

    # Calculate angle between gun and mouse position
    delta_x, delta_y = mouse_pos[0] - gun_point[0], mouse_pos[1] - gun_point[1]
    slope = delta_y / delta_x if delta_x != 0 else -1000000
    rotation = math.degrees(math.atan(slope))

    # Flip gun based on mouse position
    gun = guns[level - 1]
    if mouse_pos[0] < WIDTH / 2:
        gun = pygame.transform.flip(gun, True, False)
        rotation = 90 - rotation
        gun_pos = (WIDTH / 2 - 90, HEIGHT - 250)
    else:
        rotation = 270 - rotation
        gun_pos = (WIDTH / 2 - 30, HEIGHT - 250)

    # Draw rotated gun
    if mouse_pos[1] < 600:
        screen.blit(pygame.transform.rotate(gun, rotation), gun_pos)

        # Fire laser if mouse click
        if clicks[0]:
            pygame.draw.circle(screen, lasers[level - 1], mouse_pos, 5)
