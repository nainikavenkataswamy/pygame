# Game state variables with type annotations
level: int = 1
points: int = 0
total_shots: int = 0
mode: int = 0  # 0: Freeplay, 1: Ammo, 2: Timed
ammo: int = 0
best_freeplay: int = 0
best_ammo: int = 0
best_timed: int = 0
time_passed: int = 0
time_remaining: int = 0
counter: int = 1

shot: bool = False
clicked: bool = False
menu: bool = True
game_over: bool = False
pause: bool = False
write_values: bool = False
new_coords: bool = True
