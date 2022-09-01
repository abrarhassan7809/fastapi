import time
from pynput.keyboard import Key, Controller

keyboard = Controller()

time.sleep(2)
keyboard.press(Key.up)
keyboard.release(Key.up)
