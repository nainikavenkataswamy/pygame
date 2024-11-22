from typing import Tuple
import pygame
from pygame import Rect


# Function to display the pause screen.
def draw_pause(
    screen: pygame.Surface,
    pause_img: pygame.Surface,
    resume_level: int,
    level: int,
    pause: bool,
    menu: bool,
    points: int,
    total_shots: int,
    time_remaining: float,
    time_passed: float,
    clicked: bool,
    new_coords: bool,
) -> Tuple[int, bool, bool, int, int, float, float, bool, bool]:
    screen.blit(pause_img, (0, 0))  # Draw pause background
    mouse_pos, clicks = pygame.mouse.get_pos(), pygame.mouse.get_pressed()

    # Define button areas
    buttons = {
        "resume": Rect((120, 481), (180, 75)),
        "menu": Rect((350, 481), (180, 75)),
    }

    # Button interactions
    if clicks[0] and not clicked:
        if buttons["resume"].collidepoint(mouse_pos):
            level, pause = resume_level, False
        elif buttons["menu"].collidepoint(mouse_pos):
            pygame.mixer.music.play()  # Resume music when returning to menu
            level, pause, menu, points, total_shots, time_passed, time_remaining = (
                0,
                False,
                True,
                0,
                0,
                0,
                0,
            )
            clicked, new_coords = True, True

    return (
        level,
        pause,
        menu,
        points,
        total_shots,
        time_passed,
        time_remaining,
        clicked,
        new_coords,
    )
