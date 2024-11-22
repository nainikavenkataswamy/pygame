import pygame


# Function to draw score and game information on the screen
def draw_score(
    screen: pygame.Surface,
    font: pygame.font.Font,
    points: int,
    total_shots: int,
    time_passed: int,
    mode: int,
    ammo: int,
    time_remaining: int,
) -> None:
    points_text = font.render(f"Points: {points}", True, "black")
    screen.blit(points_text, (240, 458))

    shots_text = font.render(f"Total shots: {total_shots}", True, "black")
    screen.blit(shots_text, (240, 488))

    time_text = font.render(f"Time: {time_passed}", True, "black")
    screen.blit(time_text, (240, 518))

    if mode == 0:  # Freeplay mode
        mode_text = font.render("Freeplay", True, "black")
    elif mode == 1:  # Ammo mode
        mode_text = font.render(f"Ammo: {ammo}", True, "black")
    elif mode == 2:  # Timed mode
        mode_text = font.render(f"Time remaining: {time_remaining}", True, "black")

    screen.blit(mode_text, (240, 548))
