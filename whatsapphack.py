import pyautogui
import time

time.sleep(4)

count = 0

while count<=10:
    pyautogui.typewrite("Test")
    pyautogui.press("enter")
    count= count + 1

