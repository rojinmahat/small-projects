import pyautogui
import time
import keyboard
import threading

#set the state of auto clicker to running or stopped
def running_state(start_key, end_key):
    global running
    global exit_flag
    while True:
        if keyboard.is_pressed('esc'):
            exit_flag = True
            print("Exiting auto-clicker...")
            break
        elif keyboard.is_pressed(start_key):
            running = True
            print("Auto-clicking started...")
            time.sleep(1)  # Debounce delay
        elif keyboard.is_pressed(end_key):
            running = False
            print("Auto-clicking stopped...")
            time.sleep(1)  # Debounce delay
        time.sleep(0.1)  # Reduce CPU usage
    return 0

#auto clicker function
def auto_clicker(delay, click_key):
    global running
    global exit_flag

    while (exit_flag == False):
        if running:
            pyautogui.click(button=click_key)
            time.sleep(delay/1000.0)  # Convert ms to seconds
        else:
            time.sleep(0.1)#chill when not running
    return 0

running = False
exit_flag = False

#get the CPS
delay = float(input("time delay between each clicks(ms): "))

#get the start and end key
start_key = input("Enter the key to start auto-clicking (e.g., 's' for start): ").lower()
end_key = input("Enter the key to stop auto-clicking (e.g., 'e' for end): ").lower()

#get the key to be pressed
click_key = input("Enter the key to be auto-clicked:\n (left, right, middle): ").lower()
if click_key not in ['left', 'right', 'middle']:
    print("Invalid click key. Please enter 'left', 'right', or 'middle'.")
    exit()

print(f"Press '{start_key}' to start auto-clicking and '{end_key}' to stop. Press 'esc' to exit.")

#get the threads working on both functions at once
stateThread = threading.Thread(target=running_state, args=(start_key, end_key))
clickThread = threading.Thread(target=auto_clicker, args=(delay, click_key))

stateThread.start()
clickThread.start()

stateThread.join()
clickThread.join()

print("Auto-clicker has been terminated.")

# works. not the most effecient but it works. 
# highest reached with 1ms dwlay is ~9.1cps due to python and system limitations