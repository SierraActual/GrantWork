import pyautogui
import time

# minimize terminal
pyautogui.hotkey('alt', 'f9')


# Move the mouse to desktop file system and enter it
pyautogui.moveTo(86, 81)
pyautogui.click()
pyautogui.click()

# enter home folder
pyautogui.moveTo(92, 196)
pyautogui.click()

# Open file tab
pyautogui.moveTo(23, 70)
pyautogui.click()

# Hover over new doc and wait .5 secs
pyautogui.moveTo(130, 196)
time.sleep(.5)


pyautogui.moveTo(350, 288)
pyautogui.click()
time.sleep(.2)


# Type a string
pyautogui.typewrite('new file durrr')

# Press the 'enter' key
pyautogui.press('enter')