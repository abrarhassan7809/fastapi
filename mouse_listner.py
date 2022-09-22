import time
from pynput.keyboard import Key, Listener, Controller
from pynput.mouse import Button, Listener, Controller

mouse = Controller()
# pos = mouse.position
# print(pos)
# def click_left():
#     time.sleep(2)
#     mouse.click(Button.left)
#     print('left button is clicked')
#
# def click_right():
#     time.sleep(2)
#     mouse.click(Button.right)
#     print('right button is clicked')

# -------------------------
# def auto_mouse_move():
#     pyautogui.click(20, 300, duration=1)
#     pyautogui.click(550, 48, duration=1)
#     time.sleep(1)
#     pyautogui.typewrite("open youtube")
#     pyautogui.hotkey('enter')
#     pyautogui.click(362, 329, duration=1)
#     time.sleep(1)
#     pyautogui.hotkey('enter')
#
# auto_mouse_move()

# --------------------

# def write_file(x, y):
#     print(f"The current position is {(x, y)}")
#
# with Listener(on_move=write_file) as l:
#     l.join()

# ----------------------------
# mouse.move(670, 370)
# pos = mouse.position
# print(pos)

# -----------------------------

def on_scroll(x, y, dx, dy):
    # mouse.click(Button.right)
    print(f"{x}, {y}, {dx}, {dy}")

# Collect events until released
with Listener(on_scroll=on_scroll) as listener:
    listener.join()

# -------------------------------
