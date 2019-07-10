class Autoclickr(object):

    def __init__(self, enabled = False, delay = 0, startKey = "left", stopKey = "right"):

        import pyautogui
        import keyboard
        import time

        self.pyClick = pyautogui.click
        self.pyPress = keyboard.is_pressed
        self.pySleep = time.sleep

        self.enabled = enabled
        self.delay = delay
        self.startKey = startKey
        self.stopKey = stopKey

        self.clickThrough = False

    def click(self):
        try:
            if self.pyPress(self.startKey):
                self.clickThrough = True
            elif self.pyPress(self.stopKey):
                self.clickThrough = False
            else:
                pass

            if self.clickThrough:
                self.pyClick()
        except:
            pass

    def run(self):
        delay = self.delay
        startKey = self.startKey
        stopKey = self.stopKey

        while self.enabled:
            self.click()
            self.pySleep(self.delay)

clicker = Autoclickr(True, 0, 'left', 'right')
clicker.run()
