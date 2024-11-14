# Set Browser

This repository contains two Python scripts designed to automate the process of setting your default browser on a Windows machine. It is particularly useful if your job enforces Microsoft Edge as the default browser, and you want to easily switch it back to your preferred browser.

## Scripts

### 1. `set_default_browser.py`

This script automates the process of opening Windows Settings, navigating to the "Default Apps" section, and changing the default web browser to your preferred choice.

#### How it works

- Opens Windows Settings app (`ms-settings:`).
- Clicks through the necessary UI elements to reach the "Default Web Browser" section.
- Sets the default browser by simulating mouse clicks.

You can modify the coordinates in the script to suit your screen resolution and specific browser choice.

#### Usage

1. Run `set_default_browser.py`.
2. The script will automatically change your default browser to your preferred choice by clicking the necessary UI elements.

### 2. `get_coordinates.py`

This script helps you get the screen coordinates needed for `set_default_browser.py`. It continuously prints the current mouse position every 3 seconds, allowing you to manually identify the pixel coordinates you need for clicking specific UI elements.

#### How it works

- You move your mouse to the desired location.
- The script prints the current mouse position every 3 seconds.
- Once you have the necessary coordinates, you can use them in `set_default_browser.py`.

#### Usage

1. Run `get_coordinates.py`.
2. Move your mouse to the target location and the script will print the coordinates in the terminal.
3. Use these coordinates in `set_default_browser.py` to make it work with your system.

## Requirements

- Python 3.x
- `pyautogui` library (for simulating mouse movements and clicks)

You can install `pyautogui` with pip:

```bash
pip install pyautogui
```

## How to Use

1. Clone or download this repository.
2. Run `get_coordinates.py` to get the screen coordinates for the UI elements in your Settings app.
3. Update `set_default_browser.py` with the appropriate coordinates based on your screen.
4. Run `set_default_browser.py` to set your default browser.

## Notes

- The script relies on screen coordinates, so it might need adjustments based on your screen resolution and UI scaling.
- You may need to run the script with administrator privileges if required by your system.

## Motivation

I created this project because my workplace enforces Microsoft Edge as the default browser, and I needed an easy way to automate the process of switching back to my preferred browser. These scripts provide a simple solution to quickly change the default web browser on Windows.

## License

This project is licensed under the GNU General Public License v3.0 (GPL-3.0). See the [LICENSE](LICENSE) file for details.
