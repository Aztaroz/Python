# from pynput.keyboard import Controller

# keyboard = Controller()

# keyboard.type("F5")

import pyautogui
import time

while True:
    time.sleep(5)
    pyautogui.hotkey('F5')
    

# print(pyautogui.FAILSAFE)
# i = 0
'''
for x in range(5):
    if i >= 3:
        pyautogui.alert("message box")
        i = 0
    else:
        pyautogui.write('Hi')
    i+=1
'''