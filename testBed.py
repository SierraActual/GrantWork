import pyautogui

def test_func():
    if 1 == 1:
        exit('This worked')

def main():
    pyautogui.keyDown('command')
    pyautogui.keyDown('m')
    pyautogui.keyUp('command')
    pyautogui.keyUp('m')
if __name__ == '__main__':
    main()