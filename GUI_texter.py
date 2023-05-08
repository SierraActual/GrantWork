import pyautogui
import time
import csv

message1 = 'Hey'
message2 = ', this is Grant with the Breathe Oxygen Bar. I just tried calling you \
    about the sales position you applied for. Please call back at your nearest convenience, \
    or simply pick the time/location you\'d like to schedule an interview with this link: \
    https://calendy.com/breatheoxygen/harmon-corner-interview\n(You may need to respond to \
    this message for the link to appear) Thanks!\n\nGrant Barnes\n865.321.2915\nhttps://breatheoxygenbar.com/'

csv_file_path = '/home/chris/Documents/Code/GrantWork/GrantCSV.csv'  #TODO Replace with the path to your CSV file

TESTNAME = 'Grant' #TODO Change if you want. This is jut the name that will go in our test text to ourselves.
TESTNUMBER = '8653212915' #TODO Insert your own phone number here for when we do the initial test.


def get_names_numbers():
    # Open and read our CSV to store names and numbers
    NAMES_AND_NUMBERS = [] 

    #TODO edit to read NAMES and NUMBERS properly
    with open(csv_file_path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row:  # Skip empty rows
                name = row[1].split(' ')
                number = row[3].replace('+1 ', '').replace(' ', '')
                NAMES_AND_NUMBERS.append([name[0], number])
        del NAMES_AND_NUMBERS[0]
            
    
    return NAMES_AND_NUMBERS


def test_text():
    cont = input("The following function will test to ensure you are set up correctly. Continue? (y/n) ")
    # Exits if user does not wish to perform test
    if cont != ('y' or 'Y'):
        return
    # Sends a text message to the user's own number as defined by global variables at start.
    send_text(TESTNAME, TESTNUMBER)
    # Check to ensure it worked properly. Exit if user indicates it did not.
    didWork = input('Did the test message send the sample message to your own number? (y/n) ')
    if didWork != ('y' or 'Y'):
        exit('Please ensure all other windows are closed and iMessage is maximized. Exiting...')
    return True


def send_text(name, number):
    print(f"[+] Sending message to {number}...")

    try:

        #TODO GUI command to enter number at top of iMessage
        '''
        pyautogui.moveTo(86, 81)
        pyautogui.click()
        time.sleep(1)
        pyautogui.typewrite(f'{number}')
        '''

        #TODO GUI command to send the message
        '''
        pyautogui.moveTo(86, 81)
        pyautogui.click()
        time.sleep(.5)
        pyautogui.typewrite(f'{message1} {name}{message2}')
        time.sleep(.5)
        pyautogui.press('enter')
        time.sleep(1)
        '''
        ... #<--- TODO remove this once actions complete.
    except:
        exit(f"[-] Failed to send text to {number}. Exiting...")

    print(f"[+] Message successfully sent to {number}.")


def main():
    windows = input('Have you made sure the only window open is iMessage? (y/n) ')
    if windows != ('y' or 'Y'):
        exit('Please close all windows other than iMessage. Exiting...')
    full = input('Is iMessage currently running at fullscreen behind this terminal window? (y/n) ')
    if full !=('y' or 'Y'):
        exit('Please ensure iMessage is running at fullscreen behind this terminal. Exiting...')

    test_text()

    # Generate a list name/number combos for use in send_text
    print("[+] Reading CSV to gather names and numbers...")
    try:
        people = get_names_numbers()
        print(people)
    except:
        print("[-] Unable to read and extract from CSV file. Exiting...")
        exit()
    
    # Sends texts according to parameters generated from CSV
    print("[+] Successfully read CSV and gathered info.")

    # Ask user if time is okay
    counter = 0
    for row in people:
        counter += 1
    counter = counter * 3 / 60
    timeEst = input(f"Estimated time to complete your project is {counter} minutes. Do you wish to continue? (y/n)")
    if timeEst != ('y' or 'Y'):
        exit('User indicated time not optimal. Exiting...')

    #Launch timer
    print('Launching in 5...')
    for i in range(4, 0, -1):
        time.sleep(1)
        print(f'{i}...')

    # Start texting all numbers in csv
    print('[+] Beggining text sequence. Do not touch computer until complete...')
    time.sleep(2)
    pyautogui.hotkey('alt', 'tab')
    
    for person in people:
        send_text(person[0], person[1])
    print("[+] Successfully texted all numbers from list.")


if __name__ == "__main__":
    main()

