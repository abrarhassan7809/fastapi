import time
from fastapi import FastAPI
from pynput.keyboard import Key, Controller

keyboard = Controller()
app = FastAPI()

@app.get("/up-key")
def up_key():
    time.sleep(2)
    keyboard.press(Key.up)
    keyboard.release(Key.up)
    return "Up key pressed"

@app.get("/down-key")
def down_key():
    time.sleep(2)
    keyboard.press(Key.down)
    keyboard.release(Key.down)
    return "Down key pressed"

@app.get("/left-key")
def left_key():
    time.sleep(2)
    keyboard.press(Key.left)
    keyboard.release(Key.left)
    return "Left key pressed"

@app.get("/right-key")
def right_key():
    time.sleep(2)
    keyboard.press(Key.right)
    keyboard.release(Key.right)
    return "Right key pressed"
