import pyautogui


class MouseController:

    def __init__(self):
        self.screen_width, self.screen_height = pyautogui.size()

        # Disable PyAutoGUI fail-safe because the cursor is controlled by hand
        pyautogui.FAILSAFE = False

    def move(self, x, y):
        pyautogui.moveTo(x, y, duration=0.05)

    def left_click(self):
        pyautogui.click(button="left")

    def right_click(self):
        pyautogui.click(button="right")

    def double_click(self):
        pyautogui.doubleClick()

    def scroll(self, amount):
        pyautogui.scroll(amount)