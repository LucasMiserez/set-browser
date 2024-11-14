import pyautogui
import time
        
def get_coordinates_on_click():
    print("Move your mouse to the desired location, after 3 seconds you will see your coordinates .")
    print("Press Ctrl + C to stop the script.")
    
    while True:
        print(f"Mouse clicked at: {pyautogui.position()}")
        time.sleep(3) 

if __name__ == "__main__":
    get_coordinates_on_click()