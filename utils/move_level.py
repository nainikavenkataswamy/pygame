from typing import List, Tuple


# Function to move targets based on the level
def move_level(
    coords: List[List[Tuple[int, int]]], level: int, WIDTH: int
) -> List[List[Tuple[int, int]]]:
    if level == 1 or level == 2:
        max_val = 3
    else:
        max_val = 4

    for i in range(max_val):
        for j in range(len(coords[i])):
            my_coords = coords[i][j]
            if my_coords[0] < -150:  # Reset target position if it goes off screen
                coords[i][j] = (WIDTH, my_coords[1])  # Reset the target's position
            else:
                coords[i][j] = (my_coords[0] - 2**i, my_coords[1])  # Move targets left

    return coords
