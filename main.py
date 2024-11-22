import pygame
import math
from utils.assets_utils import *
from utils.game_info import draw_score
from utils.game_variables import *
from utils.gun_utils import *
from utils.move_level import move_level
from utils.game_pause import draw_pause

# Initialize Pygame
pygame.init()

# Initialize lists for backgrounds, banners, guns, and target images
bgs = []
banners = []
guns = []
target_images = [[], [], []]

# Define target configurations for each level
targets = {1: [10, 5, 3], 2: [12, 8, 5], 3: [15, 12, 8, 3]}

# Load images for backgrounds, banners, guns, and targets
for i in range(1, 4):
    # Load background, banner, and gun images
    bgs.append(pygame.image.load(f"./assets/bgs/{i}.png"))
    banners.append(pygame.image.load(f"./assets/banners/{i}.png"))
    guns.append(
        pygame.transform.scale(pygame.image.load(f"./assets/guns/{i}.png"), (100, 100))
    )

    # Determine the target count based on the level (3 for 1-2, 4 for 3)
    target_count = 3 if i < 3 else 4

    # Load target images
    for j in range(1, target_count + 1):
        target_size = (120 - (j * 18), 80 - (j * 12))
        target_images[i - 1].append(
            pygame.transform.scale(
                pygame.image.load(f"./assets/targets/{i}/{j}.png"), target_size
            )
        )

# Read high scores from file
file = open("./scores/high_scores.txt", "r")
read_file = file.readlines()
file.close()
best_freeplay = int(read_file[0])
best_ammo = int(read_file[1])
best_timed = int(read_file[2])


# Function to draw the targets on the screen
def draw_level(coords):
    target_rects = [
        [] for _ in range(len(coords))
    ]  # Create a list to hold target rectangles
    for i in range(len(coords)):
        for j in range(len(coords[i])):
            target_rects[i].append(
                pygame.rect.Rect(
                    (coords[i][j][0] + 20, coords[i][j][1]), (60 - i * 12, 60 - i * 12)
                )
            )
            screen.blit(
                target_images[level - 1][i], coords[i][j]
            )  # Draw each target image
    return target_rects


# Function to check if a shot hits any target
def check_shot(targets, coords):
    global points
    mouse_pos = pygame.mouse.get_pos()
    level_sounds = {
        1: bird_sound,
        2: plate_sound,
        3: laser_sound,
    }  # Map levels to sounds
    sound = level_sounds.get(level)  # Get the sound based on the current level

    # Iterate over targets and check for hits
    for i, target_row in enumerate(targets):
        for j, target in enumerate(target_row):
            if target.collidepoint(mouse_pos):
                coords[i].pop(j)
                points += 10 + 10 * (i**2)
                if sound:
                    sound.play()
                break
    return coords


# Function to draw the main menu
def draw_menu():
    global game_over, pause, mode, level, menu, time_passed, total_shots, points, ammo, time_remaining, best_timed, best_freeplay, best_ammo, write_values, clicked, new_coords
    game_over, pause = False, False
    screen.blit(menu_img, (0, 0))  # Draw menu background
    mouse_pos = pygame.mouse.get_pos()
    clicks = pygame.mouse.get_pressed()

    # Define button areas
    buttons = {
        "freeplay": pygame.rect.Rect((110, 400), (230, 80)),
        "ammo": pygame.rect.Rect((370, 400), (230, 80)),
        "time": pygame.rect.Rect((110, 510), (230, 80)),
        "reset": pygame.rect.Rect((370, 510), (230, 80)),
    }

    # Display best scores on the menu
    screen.blit(font.render(f"{best_freeplay}", True, "black"), (266, 435))
    screen.blit(font.render(f"{best_ammo}", True, "black"), (505, 435))
    screen.blit(font.render(f"{best_timed}", True, "black"), (273, 532))

    # Button interactions
    if clicks[0] and not clicked:
        if buttons["freeplay"].collidepoint(mouse_pos):
            mode, level, menu, time_passed, total_shots, points = 0, 1, False, 0, 0, 0
            new_coords = True
        elif buttons["ammo"].collidepoint(mouse_pos):
            mode, level, menu, ammo, time_passed, total_shots, points = (
                1,
                1,
                False,
                81,
                0,
                0,
                0,
            )
            new_coords = True
        elif buttons["time"].collidepoint(mouse_pos):
            mode, level, menu, time_remaining, time_passed, total_shots, points = (
                2,
                1,
                False,
                30,
                0,
                0,
                0,
            )
            new_coords = True
        elif buttons["reset"].collidepoint(mouse_pos):
            best_freeplay, best_ammo, best_timed = 0, 0, 0
            write_values = True
            new_coords = True
        clicked = True


# Function to draw the game over screen
def draw_game_over():
    global clicked, level, pause, game_over, menu, points, total_shots, time_remaining, time_passed, run

    display_score = time_passed if mode == 0 else points
    screen.blit(game_over_img, (0, 0))  # Draw game over background
    mouse_pos = pygame.mouse.get_pos()
    clicks = pygame.mouse.get_pressed()

    # Button areas
    exit_button = pygame.rect.Rect((120, 481), (180, 75))
    menu_button = pygame.rect.Rect((350, 481), (180, 75))

    # Display final score
    screen.blit(big_font.render(f"{display_score}", True, "black"), (505, 428))

    # Button interactions
    if menu_button.collidepoint(mouse_pos) and clicks[0] and not clicked:
        clicked = True
        (
            level,
            pause,
            game_over,
            menu,
            points,
            total_shots,
            time_passed,
            time_remaining,
        ) = (0, False, False, True, 0, 0, 0, 0)
    elif exit_button.collidepoint(mouse_pos) and clicks[0] and not clicked:
        run = False


# Main game loop
run = True
while run:
    clock.tick(FPS)
    if level != 0:
        if counter < 60:
            counter += 1
        else:
            counter = 1
            time_passed += 1
            if mode == 2:
                time_remaining -= 1

    if new_coords:
        one_coords = [[], [], []]
        two_coords = [[], [], []]
        three_coords = [[], [], [], []]

        # Set initial positions for targets in level 1
        for i in range(3):
            my_list = targets[1]
            for j in range(my_list[i]):
                one_coords[i].append(
                    (WIDTH // (my_list[i]) * j, 300 - (i * 150) + 30 * (j % 2))
                )

        # Set initial positions for targets in level 2
        for i in range(3):
            my_list = targets[2]
            for j in range(my_list[i]):
                two_coords[i].append(
                    (WIDTH // (my_list[i]) * j, 300 - (i * 150) + 30 * (j % 2))
                )

        # Set initial positions for targets in level 3
        for i in range(4):
            my_list = targets[3]
            for j in range(my_list[i]):
                three_coords[i].append(
                    (WIDTH // (my_list[i]) * j, 300 - (i * 100) + 30 * (j % 2))
                )
        new_coords = False

    screen.fill("black")  # Clear screen
    screen.blit(bgs[level - 1], (0, 0))  # Draw background
    screen.blit(banners[level - 1], (0, HEIGHT - 200))

    # Check which game state to draw
    if menu:
        level = 0
        draw_menu()
    if game_over:
        level = 0
        draw_game_over()
    if pause:
        level = 0
        (
            level,
            pause,
            menu,
            points,
            total_shots,
            time_remaining,
            time_passed,
            clicked,
            new_coords,
        ) = draw_pause(
            screen,
            pause_img,
            resume_level,
            level,
            pause,
            menu,
            points,
            total_shots,
            time_remaining,
            time_passed,
            clicked,
            new_coords,
        )

    # Draw targets and check for shots based on the current level
    if level == 1:
        target_boxes = draw_level(one_coords)
        one_coords = move_level(one_coords, level, WIDTH)
        if shot:
            one_coords = check_shot(target_boxes, one_coords)
            shot = False
    elif level == 2:
        target_boxes = draw_level(two_coords)
        two_coords = move_level(two_coords, level, WIDTH)
        if shot:
            two_coords = check_shot(target_boxes, two_coords)
            shot = False
    elif level == 3:
        target_boxes = draw_level(three_coords)
        three_coords = move_level(three_coords, level, WIDTH)
        if shot:
            three_coords = check_shot(target_boxes, three_coords)
            shot = False

    # Draw the gun and score if in play mode
    if level > 0:
        draw_gun(guns, lasers, level, WIDTH, HEIGHT, screen)
        draw_score(
            screen, font, points, total_shots, time_passed, mode, ammo, time_remaining
        )

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_position = pygame.mouse.get_pos()
            if (0 < mouse_position[0] < WIDTH) and (
                0 < mouse_position[1] < HEIGHT - 200
            ):
                shot = True
                total_shots += 1
                if mode == 1:
                    ammo -= 1  # Reduce ammo in ammo mode
            if (520 < mouse_position[0] < 669) and (455 < mouse_position[1] < 536):
                resume_level = level
                pause = True
                clicked = True
            if (520 < mouse_position[0] < 669) and (516 < mouse_position[1] < 570):
                menu = True
                pygame.mixer.music.play()
                clicked = True
                new_coords = True
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1 and clicked:
            clicked = False

    # Check if all targets are hit to advance to the next level or end the game
    if level > 0:
        if target_boxes == [[], [], []] and level < 3:
            level += 1
        if (
            (level == 3 and target_boxes == [[], [], [], []])
            or (mode == 1 and ammo == 0)
            or (mode == 2 and time_remaining == 0)
        ):
            new_coords = True
            pygame.mixer.music.play()
            if mode == 0:
                if time_passed < best_freeplay or best_freeplay == 0:
                    best_freeplay = time_passed
                    write_values = True
            if mode == 1:
                if points > best_ammo:
                    best_ammo = points
                    write_values = True
            if mode == 2:
                if points > best_timed:
                    best_timed = points
                    write_values = True
            game_over = True

    # Write high scores to file if necessary
    if write_values:
        file = open("./scores/high_scores.txt", "w")
        file.write(f"{best_freeplay}\n{best_ammo}\n{best_timed}")
        file.close()
        write_values = False

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
