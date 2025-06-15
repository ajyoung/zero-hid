# This script captures screenshots of every workout in the manually
# selected category of the iPad fitness app. 
# It requires that Full Keyboard Access is enabled in the iPad settings
# so that the iPad can be fully controlled by keypresses, requiring no
# mouse or touch input.
import time
import os
import argparse
from zero_hid import Keyboard, KeyCodes

import time
import os

def send_key(list, keycode):
    #print(f"Sending: {keys}")
    with Keyboard() as k:
        k.press(list, keycode)
    #os.system(f'hid-keyboard keyboard {combo}')
    time.sleep(0.5)  # Short delay for key processing

def wait(seconds):
    print(f"Waiting {seconds}s")
    time.sleep(seconds)

# -- Navigation loop --
def run_grid_loop(num_rows=3, num_columns=3, start_workout=1, total_workouts=18):
    total = total_workouts

    for i in range(total + 1):
        print(f"\n=== Processing workout {i + 1} ===")

        # Tab to select the workout tile (repeat tab if not first tile)
        if i > 0 and i % num_columns == 0:
            send_key([], KeyCodes.KEY_DOWN)
            send_key([], KeyCodes.KEY_LEFT)
            send_key([], KeyCodes.KEY_LEFT)
        elif i > 0:
            send_key([], KeyCodes.KEY_RIGHT) 

        if (i + 1) < start_workout:
            print(f"\n=== Skipping workout {i + 1} due to start index ===")
            continue  

        if i == total:
            continue     

        # Open workout
        send_key([], KeyCodes.KEY_SPACE)
        wait(1)  # Allow workout page to load

        # Screenshot (using Cmd+Shift+3 as default full screenshot)
        send_key([KeyCodes.MOD_LEFT_GUI, KeyCodes.MOD_LEFT_SHIFT], KeyCodes.KEY_3)
        wait(4)

        # Go back
        send_key([], KeyCodes.KEY_UP)
        send_key([], KeyCodes.KEY_SPACE)
        wait(1)

    print("\n=== Finished current grid ===")

    # Scroll down after each set -- not needed since page down works
    #print("Scrolling down for next set...")
    #send_key('page-down')  # Or try down arrow if Page Down is unsupported
    #wait(1.0)

# Entry point
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Capture screenshots of workouts from iPad fitness app')
    parser.add_argument('num_workouts', type=int, help='Number of workouts to capture')
    parser.add_argument('--start', type=int, default=1, help='Workout number to start from (1-based)')
    parser.add_argument('--rows', type=int, default=3, help='Number of rows in the workout grid')
    parser.add_argument('--columns', type=int, default=3, help='Number of columns in the workout grid')
    
    args = parser.parse_args()
    run_grid_loop(args.rows, args.columns, args.start, args.num_workouts)

