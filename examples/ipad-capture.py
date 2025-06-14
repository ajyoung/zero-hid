# This script captures screenshots of every workout in the manually
# selected category of the iPad fitness app. 
# It requires that Full Keyboard Access is enabled in the iPad settings
# so that the iPad can be fully controlled by keypresses, requiring no
# mouse or touch input.
import time
import os
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
def run_grid_loop(num_rows=3, num_columns=3):
    total = num_rows * num_columns

    for i in range(total):
        print(f"\n=== Processing workout {i + 1} ===")

        # Tab to select the workout tile (repeat tab if not first tile)
        if i > 0 and i % num_columns == 0:
            send_key([], KeyCodes.KEY_DOWN)
        else:
            send_key([], KeyCodes.KEY_RIGHT)    

        # Open workout
        send_key([], KeyCodes.KEY_SPACE)
        wait(0.5)  # Allow workout page to load

        # Screenshot (using Cmd+Shift+3 as default full screenshot)
        send_key([KeyCodes.MOD_LEFT_GUI, KeyCodes.MOD_LEFT_SHIFT], KeyCodes.KEY_3)
        wait(3)

        # Go back
        send_key([], KeyCodes.KEY_UP)
        send_key([], KeyCodes.KEY_SPACE)
        wait(0.5)

    print("\n=== Finished current grid ===")

    # Scroll down after each set
    #print("Scrolling down for next set...")
    #send_key('page-down')  # Or try down arrow if Page Down is unsupported
    #wait(1.0)

# -- Run entire scraping session for Strength workouts --
def run_session():
    num_scrolls = 10  # Adjust based on number of pages

    for s in range(num_scrolls):
        print(f"\n--- Scroll set {s + 1} ---")
        run_grid_loop()
        wait(1.5)

# Entry point
if __name__ == "__main__":
    run_session()

