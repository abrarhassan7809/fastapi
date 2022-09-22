from fastapi import FastAPI
from pynput.keyboard import Key, Controller as KeyboardController
from pynput.mouse import Listener, Controller as MouseController

keyboardController = KeyboardController()
mouse_controller = MouseController()

app = FastAPI()

@app.get("/get-key/{item}")
def key_pressed(item: str):
    try:
        key = "Key." + item
        keyboardController.tap(eval(key))
        return f"{key} key pressed"
    except Exception as e:
        print(e)
        return "Error is found"

@app.get("/start-scroll/{item1}/{item2}")
def scrolling(item1: float, item2: float):

    mouse_controller.scroll(item1, item2)

@app.get("/mouse-move/{item1}/{item2}")
def mouse(item1: float, item2: float):

    mouse_controller.move(item1, item2)
