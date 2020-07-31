import pyautogui
print(pyautogui.size())
width, height = pyautogui.size()
print(pyautogui.position())
pyautogui.moveTo(10, 10, duration=1.5)
pyautogui.moveRel(200, 0, duration=1.5)
