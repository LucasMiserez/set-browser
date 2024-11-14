import pyautogui
import subprocess
import time

def open_settings():
    subprocess.run("start ms-settings:", shell=True)
    time.sleep(1)


def close_settings():
    time.sleep(1)
    subprocess.run(['taskkill', '/f', '/im', 'SystemSettings.exe'], check=True)

def click(x, y):
    time.sleep(0.8) 
    pyautogui.click(x, y)


def main():
    open_settings()  # Open the Settings app
    click(406, 380)  # Apps
    click(76, 275) # Standard Apps
    click(447, 794) # Current Webbrowser
    click(514, 643) # Browser at the bottom
    close_settings()


if __name__ == "__main__":
    main()
