import time
from fastapi import FastAPI
from pynput.keyboard import Key, Controller as KeyboardController
# from pynput.mouse import Button, Controller as MouseController

mKeyboardController = KeyboardController()

app = FastAPI()

@app.get("/get-key/{item}")
def key_pressed(item: str):
    try:
        key = "Key." + item
        mKeyboardController.tap(eval(key))
        return f"{key} key pressed"
    except Exception as e:
        print(e)
        return "Error is found"

# @app.get("/mouse-left-key")
# def mouse_left_key():
#     time.sleep(2)
#     key_controller.click(Button.left)
#     key_controller.release(Button.left)
#     return "left button is clicked"

# @app.get("/up-scroll")
# def up_scroll():
#     pyautogui.scroll(10)
#     return "Up scrolling"
