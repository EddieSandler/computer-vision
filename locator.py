import pyautogui
import time

# im1 = pyautogui.screenshot()
# im2 = pyautogui.screenshot('my_screenshot.png')
# next_button_location= pyautogui.locateOnScreen('next.png')
# next_button_point = pyautogui.center(next_button_location)
# next_button_x, next_button_y= next_button_point
# pyautogui.click(next_button_x, next_button_y)  # clicks the center of where the next button was found
# pyautogui.click('next.png')

def chain_click_and_write(x, y, text, duration=1):
    pyautogui.moveTo(x, y, duration=duration)
    pyautogui.click()
    pyautogui.write(text, interval=0.1)
    time.sleep(0.5)  # Add a short delay
    pyautogui.press('enter')
    pyautogui.press('tab', presses=1, interval=0.2)
    pyautogui.write("260")
    pyautogui.press('tab', presses=1, interval=0.2)
    pyautogui.write("6")
    pyautogui.press('tab', presses=1, interval=0.2)
    pyautogui.write("2")
    pyautogui.moveTo(2388,1399)#ft
    pyautogui.click()
    pyautogui.moveTo(1230,1737) #sex
    pyautogui.click()
    pyautogui.moveTo(2307,1740)
    pyautogui.click()
    pyautogui.write("56")
    pyautogui.click()
    pyautogui.moveTo(1899,2037) #next button
    pyautogui.click()

chain_click_and_write(1039, 1051, "Ed", duration=1)

# print("Move your mouse to the target location.")
# time.sleep(5)  # Gives you 5 seconds to move the mouse to the target

# # Get the mouse position
# x, y = pyautogui.position()
# print(f"Mouse is at: x={x}, y={y}")
# pyautogui.write('Ed', interval=0.1)

# print(pyautogui.position())