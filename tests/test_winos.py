import pyautogui
import time
import pygetwindow as gw
import os

game_folder = os.getcwd()

freeplay = "./images/image1.png"
pause = "./images/image2.png"
menu = "./images/image3.png"
reset = "./images/image4.png"
accuracy = "./images/image5.png"
resume = "./images/image7.png"
countdown = "./images/image8.png"
exit = "./images/image10.png"

# Open the Run window
pyautogui.hotkey("win", "r")
time.sleep(1)
pyautogui.write("cmd")
pyautogui.press("enter")
time.sleep(1)

# Navigate to the game folder
pyautogui.write(f"cd {os.path.dirname(game_folder)}")
pyautogui.press("enter")
time.sleep(1)

# Run the main.py script
pyautogui.write("python main.py")
pyautogui.press("enter")
time.sleep(5)


def click(button_image_path):
    button_location = pyautogui.locateOnScreen(button_image_path, confidence=0.7)

    if button_location:
        print(f"Button found at {button_location}")

        window = gw.getWindowsWithTitle("shooting Game")
        if window:
            game_window = window[0]
            game_window.activate()
            time.sleep(1)

        button_center = pyautogui.center(button_location)
        print(f"Moving mouse to {button_center}")
        pyautogui.moveTo(button_center)
        time.sleep(0.1)

        print("Simulating mouse down and up.")
        pyautogui.mouseDown(button_center)
        time.sleep(0.1)
        pyautogui.mouseUp(button_center)
        time.sleep(0.1)
    else:
        print("Button not found.")


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
time.sleep(60)
click(exit)
