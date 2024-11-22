import pyautogui
import time
import subprocess
import os
import Quartz
from AppKit import NSWorkspace

# Define the game folder and virtual environment folder
game_folder = "Replace this with folder path"
venv_folder = ".venv"

# Define image paths for buttons
freeplay = "./images/image1.png"
pause = "./images/image2.png"
menu = "./images/image3.png"
reset = "./images/image4.png"
accuracy = "./images/image5.png"
resume = "./images/image7.png"
countdown = "./images/image8.png"
exit = "./images/image10.png"


# Function to run all commands in a single terminal session
def run_in_single_terminal(command):
    subprocess.run(
        ["osascript", "-e", f'tell application "Terminal" to do script "{command}"']
    )

command = f"cd {game_folder} && source {venv_folder}/bin/activate && python main.py"

# Open the terminal and execute the entire command in a single terminal session
run_in_single_terminal(command)

# Wait for the game to load (adjust as necessary)
time.sleep(
    10
)


# Function to get the window list using Quartz and AppKit
def get_window_list():
    window_list = []
    window_info_list = Quartz.CGWindowListCopyWindowInfo(
        Quartz.kCGWindowListOptionOnScreenOnly, Quartz.kCGNullWindowID
    )
    for window_info in window_info_list:
        window_list.append(window_info)
    return window_list


# Function to get a window with a specific title
def get_window_with_title(title):
    for window in get_window_list():
        window_title = window.get("kCGWindowName", "No Title")
        if window_title == title:
            return window
    return None


# Function to click on a button image with error handling and confidence matching
def click(button_image_path):
    print(f"Looking for {button_image_path}...")

    # Use the confidence parameter to allow for minor image variations
    try:
        button_location = pyautogui.locateOnScreen(
            button_image_path, confidence=0.8
        )  

        if button_location:
            print(f"Button found at {button_location}")

            # Get the game window by title (search for a window containing 'shooting Game')
            game_window = get_window_with_title("shooting Game")

            if game_window:
                print(
                    f"Activating window: {game_window.get('kCGWindowName', 'No Title')}"
                )

                # Activate the game window (focus on it)
                workspace = NSWorkspace.sharedWorkspace()
                app = workspace.frontmostApplication()
                app.activateWithOptions_(
                    4
                )

                time.sleep(1)  

            # Get the center of the button location and move the mouse to it
            button_center = pyautogui.center(button_location)
            print(f"Moving mouse to {button_center}")
            pyautogui.moveTo(button_center)
            time.sleep(0.1)

            # Simulate a click (mouse down and up)
            print("Simulating mouse down and up.")
            pyautogui.mouseDown(button_center)
            time.sleep(0.1)  # Small delay to simulate realistic clicking
            pyautogui.mouseUp(button_center)
            time.sleep(0.1)  # Pause before the next action
        else:
            print(f"Button not found: {button_image_path}")
    except pyautogui.ImageNotFoundException:
        print(f"Error: Could not locate the image '{button_image_path}' on the screen.")


# Click through the game steps
click(freeplay)
click(pause)
click(resume)
click(pause)
click(menu)
click(reset)
click(accuracy)
click(pause)
click(resume)
click(pause)
click(menu)
click(reset)
click(countdown)

# Wait for the countdown to complete
time.sleep(6)

# Exit the game
click(exit)
