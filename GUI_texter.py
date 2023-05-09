import pyautogui
import time
import csv

# Preset variables below. Change as needed.
message1 = 'Hey'
message2 = ", this is Grant with the Breathe Oxygen Bar. I just tried calling you about the sales position you applied for. Please call back at your nearest convenience, or simply pick the time/location you'd like to schedule an interview with this link: https://calendly.com/breatheoxygen/zoom-interview (You may need to respond to this message for the link to appear)"
message3 = "Thanks!" 
message4 = "Grant Barnes"
message5 = "865.321.2915"
message6 = "https://breatheoxygenbar.com/"

csv_file_path = '/Users/grantbarnes/Documents/GrantWork/GrantCSV.csv'  #TODO Replace with the path to your CSV file

TESTNAME = 'USER_NAME_WILL_GO_HERE' #TODO Change if you want. This is jut the name that will go in our test text to ourselves.
TESTNUMBER = '8653212915' #TODO Insert your own phone number here for when we do the initial test.


def get_names_numbers(csv):
    # Open and read our CSV to store names and numbers
    NAMES_AND_NUMBERS = [] 

    #TODO edit to read NAMES and NUMBERS properly
    with open(csv, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row:  # Skip empty rows
                name = row[1].split(' ')
                number = row[3].replace('+1 ', '').replace(' ', '')
                NAMES_AND_NUMBERS.append([name[0], number])
        del NAMES_AND_NUMBERS[0]
            
    
    return NAMES_AND_NUMBERS


def test_text():
    cont = input("[?] The following function will test to ensure you are set up correctly. Continue? (y/n) ").strip()
    # Exits if user does not wish to perform test
    if cont != ('y' or 'Y'):
        return
    time.sleep(1)
    # Minimize terminal
    alt_tab()
    # Sends a text message to the user's own number as defined by global variables at start.
    send_text(TESTNAME, TESTNUMBER)
    alt_tab()
    # Check to ensure it worked properly. Exit if user indicates it did not.
    didWork = input('[?] Did the test message send the sample message to your own number? (y/n) ').strip()
    if didWork != ('y' or 'Y'):
        exit('[-] Please ensure all other windows are closed and iMessage is maximized. Exiting...')
    return True


def send_text(name, number):
    print(f"[+] Sending message to {number}...")
    time.sleep(1)

    try:

        #TODO GUI command to enter number at top of iMessage
        pyautogui.moveTo(293, 63)
        pyautogui.click()
        time.sleep(1)
        pyautogui.typewrite(f'{number}')
        time.sleep(.5)
        pyautogui.press('enter')
        

        #TODO GUI command to send the message
        pyautogui.moveTo(500, 896)
        pyautogui.click()
        time.sleep(.5)
        pyautogui.typewrite(f'{message1} {name}{message2}')
        pyautogui.hotkey('alt', 'enter')
        pyautogui.hotkey('alt', 'enter')
        pyautogui.typewrite(message3)
        pyautogui.hotkey('alt', 'enter')
        pyautogui.typewrite(message4)
        pyautogui.hotkey('alt', 'enter')
        pyautogui.typewrite(message5)
        pyautogui.hotkey('alt', 'enter')
        pyautogui.typewrite(message6)
        time.sleep(.5)
        pyautogui.press('enter')
        time.sleep(1)

    except:
        alt_tab()
        exit(f"[-] Failed to send text to {number}. Exiting...")

    print(f"[+] Message successfully sent to {number}.")


def setup_prompts():
    windows = input('[?] Have you made sure the only window open is iMessage? (y/n) ').strip()
    if windows != ('y' or 'Y'):
        exit('[-] Please close all windows other than iMessage. Exiting...')
    full = input('[?] Is iMessage currently running at fullscreen behind this terminal window? (y/n) ').strip()
    if full !=('y' or 'Y'):
        exit('[-] Please ensure iMessage is running at fullscreen behind this terminal. Exiting...')
    tabFix = input('[?] Please click on the iMessage window, then reopen this terminal (command+tab). (When complete enter "y")  ').strip()
    if tabFix != ('y' or 'Y'):
        exit('[-] You must ensure you click on the iMessage window, then back to terminal, then type "y". Exiting...')


def time_prompt(people):
    counter = 0
    for row in people:
        counter += 1
    counter = counter * 17 / 60
    timeEst = input(f"[?] Estimated time to complete your project is {counter} minutes. Do you wish to continue? (y/n)  ").strip()
    if timeEst != ('y' or 'Y'):
        exit('[-] User indicated time not optimal. Exiting...')


def alt_tab():
    # Literally performs the alt + tab function.
    pyautogui.keyDown('command')
    pyautogui.keyDown('tab')
    time.sleep(.5)
    pyautogui.keyUp('command')
    pyautogui.keyUp('tab')


def main():
    # Prompt user about setup
    setup_prompts()

    # Send a test text if the user chooses to
    test_text()

    # Generate a list name/number combos for use in send_text
    print("[+] Reading CSV to gather names and numbers...")
    try:
        people = get_names_numbers(csv_file_path)
    except:
        print("[-] Unable to read and extract from CSV file. Exiting...")
        exit()
    
    # Sends texts according to parameters generated from CSV
    print("[+] Successfully read CSV and gathered info.")

    # Ask user if time is okay
    time_prompt(people)

    #Launch timer
    print('[+] Launching in 5...')
    for i in range(4, 0, -1):
        time.sleep(1)
        print(f'[+] {i}...')
    time.sleep(1)

    print('[+] Beggining text sequence. Do not touch computer until complete...')
    # Tab out of terminal
    time.sleep(2)
    alt_tab()

    # Start texting all numbers in csv
    for person in people:
        send_text(person[0], person[1])

    # Tab back into terminal
    time.sleep(1)
    alt_tab
    
    # Success message
    print("[+] Successfully texted all numbers from list.")


if __name__ == "__main__":
    main()