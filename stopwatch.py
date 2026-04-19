import time
import pynput
import threading

start_event = threading.Event()   # key event to start
stop_event = threading.Event()    # key event to stop

# defining keyboard listener function
def keyboard_listener():

    # defining on_press function
    def on_press(key):
        # catching keylogs
        try:
            k = key.char
        except AttributeError:
            k = key

        # triggering key events if they match
        if k == 's':
            start_event.set()   # triggering start key event if 's' is pressed
        elif k == 'q':
            stop_event.set()   # triggering stop key event if 'q' is pressed
            return False   # exiting keyboard listener

    # setting up keyboard listener
    with pynput.keyboard.Listener(on_press=on_press, daemon=True) as listener:
        listener.join()

# starting keyboard listener thread
threading.Thread(target=keyboard_listener).start()

print(('-' * 15) + 'Stopwatch' + ('-' * 15))
print("> Press 's' to start and 'q' to stop!\n")
clock = 0.00   # changing time variable
print(f'\r{clock: >21.2f}', end='')   # printing the current clock

# declaring terminal color codes
RED = '\033[91m' 
GREEN = '\033[92m'
RESET = '\033[0m'   # to reset colors to default

# main while loop
while not stop_event.is_set():  
    if start_event.is_set():
        time.sleep(0.01)   # stopwatch delay
        clock += 0.01   # adding 0.01 seconds to the time each iteration
        clock = round(clock, 2)   # handling floating point errors
        print(f'{GREEN}\r{clock: >21.2f}{RESET}', end='')   # printing updated time with green color
    else:
        time.sleep(0.01)   # short wait time to avoid high cpu usage

print(f'{RED}\r{clock: >21.2f}{RESET}', end='') # printing stopped time with red color
