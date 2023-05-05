import pyautogui
import time
import csv

def get_names_numbers():
    # Open and read our CSV to store names and numbers
    csv_file = 'path/to/your/file.csv'  #TODO Replace with the path to your CSV file
    NAMES_AND_NUMBERS = [] 

    #TODO edit to read NAMES and NUMBERS properly
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row:  # Skip empty rows
                NAMES_AND_NUMBERS.append([row[0], row[1]])
    
    return NAMES_AND_NUMBERS


def send_text(name, number):
    print(f"[+] Sending message to {number}...")

    try:
        #TODO insert pyautogui code to send the text
        ...
    else:
        print(f"[-] Failed to send text to {number}. Exiting...")
        exit() #TODO check that this exits the whole program and not just this function
    
    print(f"[+] Message successfully sent to {number}.")


    #TODO BELOW IS SAMPLE CODE. NEED TO CODE IN FULL WITH iMESSAGE
    '''# minimize terminal
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
    pyautogui.typewrite(f'new file {datetime.now().strftime("%H:%M:%S")}')
    # Press the 'enter' key
    pyautogui.press('enter')
    # closefile browser
    pyautogui.hotkey("alt", "f4")'''


def main():
    # Generate a list name/number combos for use in send_text
    print("[+] Reading CSV to gather names and numbers...")
    try:
        people = get_names_numbers()
    else:
        print("[-] Unable to read and extract from CSV file. Exiting...")
        exit()
    
    # Sends texts according to parameters generated from CSV
    print("[+] Successfully read CSV and gathered info. Beggining text sequence...")
    for person in people:
        send_text(person[0], person[1])
    print("[+] Successfully texted all numbers from list.")


if __name__ == "__main__":
    main()

