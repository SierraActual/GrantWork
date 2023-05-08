import pyautogui

def test_func():
    if 1 == 1:
        exit('This worked')

def main():
    print('testing')
    test_func()
    print('Did not work.')

if __name__ == '__main__':
    main()