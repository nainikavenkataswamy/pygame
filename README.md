# Shooting Game  

A Python-based shooting game developed using the **Pygame** library. Engage in different game modes (Freeplay, Ammo, and Timed), aim and shoot at moving targets, and achieve high scores while exploring dynamic levels with increasing difficulty. The game offers features like high-score tracking, a dynamic scoring system, a functional pause menu, and visually appealing assets for an engaging user experience.

---

## Table of Contents  

1. [Project Overview](#project-overview)  
2. [Folder Structure](#folder-structure)  
3. [Game Features](#game-features)  
4. [Detailed Module Descriptions](#detailed-module-descriptions)  
5. [Installation](#installation)  
6. [How to Run the Game](#how-to-run-the-game)  
7. [Testing](#testing)  
---

## Project Overview  

This project is a classic shooting game where players can:  
- Select from **three distinct game modes**: Freeplay, Ammo, and Timed.  
- Aim at targets using a virtual gun, and earn points based on accuracy.  
- Progress through increasingly difficult levels with faster-moving targets.  
- Compete with personal high scores tracked in a local file.  
- Enjoy immersive gameplay with sound effects and custom visuals.  

Whether you're a casual gamer or a competitive shooter, this game offers a fun and challenging experience!

---

## Folder Structure  

Below is the directory structure of the project, with an explanation for each folder and file:  

```
Shooting_Game/
├── assets/  
│   ├── banners/          # Banner images for game menus
│   ├── bgs/              # Backgrounds for gameplay and menus
│   ├── font/             # Fonts for score and menu displays
│   ├── guns/             # Gun assets (images/icons) for the player
│   ├── menus/            # Assets for menus (main menu, pause menu, etc.)
│   ├── sounds/           # Sound effects and music used in the game
│   ├── targets/          # Target sprites used for gameplay
├── scores/  
│   └── high_scores.txt   # Text file to track high scores for each mode
├── tests/  
│   ├── images/           # Image resources used for UI tests
│   ├── test_macos.py     # Automated tests for macOS environments
│   └── test_winos.py     # Automated tests for Windows environments
├── utils/  
│   ├── assets_utils.py   # Manages asset loading (fonts, images, sounds)
│   ├── game_variables.py # Global variables for game state and configuration
│   ├── game_pause.py     # Implements pause menu functionality
│   ├── gun_utils.py      # Gun mechanics (aiming, shooting)
│   ├── game_info.py      # Displays score, level, and other game info
│   ├── move_level.py     # Controls level transitions and target movement
├── main.py               # Main game script
├── requirements.txt      # List of Python dependencies
└── README.md             # Documentation for understanding and using the project
```

---

## Game Features  

### 1. **Game Modes**  
- **Freeplay Mode:** Play without restrictions. Shoot as many targets as possible without worrying about time or ammo.  
- **Ammo Mode:** You start with a limited number of bullets. Maximize your score before running out of ammo.  
- **Timed Mode:** You have a set amount of time to earn the highest score possible.  

### 2. **Dynamic Scoring System**  
- Each successful target hit earns you points based on accuracy and speed.  
- Displays total shots, hits, and misses for performance tracking.  

### 3. **Levels and Increasing Difficulty**  
- Targets move faster with each level.  
- Levels are automatically transitioned once certain score thresholds are met.  

### 4. **Pause Menu**  
- Accessed via a key press.  
- Options to resume, restart, or exit to the main menu.  

### 5. **High Scores**  
- Tracks high scores for all three game modes.  
- Scores are stored in the `high_scores.txt` file and are loaded at the start of the game.  

### 6. **Sound Effects and Music**  
- Engaging background music and realistic sound effects for shooting and hitting targets.  

---

## Detailed Module Descriptions  

### `main.py`  
The core script that initializes and runs the game. This file:  
- Sets up the main game loop.  
- Loads game assets and initializes variables.  
- Handles user input, such as shooting and pausing.  
- Manages game states (e.g., pause, game over).  

### `utils/assets_utils.py`  
- Handles loading and managing all game assets like images, fonts, and sounds.  
- Ensures efficient use of memory by preloading assets at startup.  

### `utils/game_variables.py`  
- Manages key variables like player score, game mode, and level.  
- Allows for centralized access and modification of shared variables.  

### `utils/game_pause.py`  
- Implements a user-friendly pause menu.  
- Provides options to resume, restart, or quit the game.  

### `utils/gun_utils.py`  
- Calculates gun position and draws it on the screen based on mouse input.  
- Simulates shooting mechanics and manages hit detection.  

### `utils/game_info.py`  
- Displays essential information like score, level, shots fired, and time remaining.  
- Updates dynamically during gameplay.  

### `utils/move_level.py`  
- Handles target movement patterns.  
- Manages level transitions by modifying game difficulty dynamically.  

### `tests/test_macos.py` and `tests/test_winos.py`  
- Automated testing scripts to verify game functionality on macOS and Windows.  
- Use `PyAutoGUI` and other libraries to simulate user input and check UI responses.  

---

## Installation  

### Prerequisites  
- Python 3.8 or higher.  
- Libraries listed in `requirements.txt`.  

### Steps  

1. Clone the repository:  
   ```bash  
   git clone <repository_url>  
   cd Shooting_Game  
   ```  

2. Install dependencies:  
   ```bash  
   pip install -r requirements.txt  
   ```  

3. Ensure the `assets` folder is in the same directory as `main.py` for resources like images, sounds, and fonts.

---

## How to Run the Game  

1. Navigate to the project directory.  
   ```bash
   cd Shooting_game
   ```
2. Activate your virtual environment (if using one):  

   ```bash  
   source .venv/bin/activate  # macOS/Linux  
   .venv\Scripts\activate  # Windows
   ```
3. Run the main script:  
   ```bash  
   python main.py
   ```

4. Use the mouse to aim and shoot at targets.
---

## Testing  

### Automated Tests  

#### macOS  
1. Update paths in `test_macos.py` for your setup.  
2. Run the tests:  
   ```bash  
   python tests/test_macos.py  
   ```  

#### Windows  
1. Update paths in `test_winos.py` for your setup.  
2. Run the tests:  
   ```bash  
   python tests/test_winos.py  
   ```  

### Manual Tests  
- Verify high-score tracking by completing multiple rounds of gameplay.  
- Check sound playback for gunshots and target hits.  
- Test level transitions by reaching high scores.  

---
### Reference
tutorials and chatgpt to clear concepts of the few functions.
 
