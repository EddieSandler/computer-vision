import pyautogui as p
import time
import cv2


# im1 = p.screenshot()
# im2 = p.screenshot('my_screenshot.png')
# next_button_location= p.locateOnScreen('next.png')
# next_button_point = p.center(next_button_location)
# next_button_x, next_button_y= next_button_point
# p.click(next_button_x, next_button_y)  # clicks the center of where the next button was found
# p.click('next.png')

def chain_click_and_write(x, y, text, duration=1):
    #first tab
    p.moveTo(x, y, duration=duration)
    p.click()
    p.write(text, interval=0.1)
    time.sleep(0.5)  # Add a short delay
    p.press('enter')
    p.press('tab', presses=1, interval=0.2)
    p.write("260")
    p.press('tab', presses=1, interval=0.2)
    p.write("6")
    p.press('tab', presses=1, interval=0.2)
    p.write("2")
    p.moveTo(2388,1399)#ft
    p.click()
    p.moveTo(1230,1737) #sex
    p.click()
    p.moveTo(2307,1740)
    p.click()
    p.write("56")
    p.click()
    p.moveTo(1899,2037) #next button
    p.click()
    #moves to the Goal tab
    p.moveTo(1871,865)
    time.sleep(1)
    p.click()
    time.sleep(1)
    p.moveTo(1664,1337)#improve health
    p.click()
    p.moveTo(1890,1441)#next
    p.click()


    #moves to the Activity tab
    p.moveTo(1620,926)
    time.sleep(1)
    p.click()
    time.sleep(1)
    p.moveTo(1300,1220)
    p.sleep(1)
    p.click()
    p.moveTo(2378,917) #exercise
    time.sleep(1)
    p.click()
    p.moveTo(2118,1161)
    time.sleep(1)
    p.click()
    time.sleep(1)

    p.moveTo(1900,1580)
    time.sleep(1)
    p.click() #next button
    time.sleep(1)

    #Diet Tab
    p.moveTo(1610,844)
    time.sleep(1)
    p.click()
    p.moveTo(1172,984)
    time.sleep(1)
    p.click()

    p.moveTo(2451,853)
    time.sleep(1)
    p.click()
    p.moveTo(2092,882)
    time.sleep(1)
    p.click()
    p.moveTo(1691,1241)
    p.click()
    p.write("3")
    time.sleep(1)
    p.press('tab')
    p.moveTo(1892,1458)
    time.sleep(1)
    p.click()
    time.sleep(1)
    p.moveTo(1824,1245)
    p.click()

    #results page

    # full name
    p.click(10, 10)
    p.moveTo(1509,1039)
    time.sleep(1)
    p.click()

    p.write("Ed Sandler")
    time.sleep(1)

    p.moveTo(1506,1291)
    time.sleep(1)
    p.click()
    p.write("DoctorDropIt")
    time.sleep(1)


    p.moveTo(1874,1800)
    time.sleep(1)
    p.click()
    p.sleep(1)

    p.moveTo(1500,1099)
    time.sleep(1)
    p.click()
    time.sleep(10)


    p.click(10,10)
    p.moveTo(1522,1108)
    time.sleep(1)
    p.click()





chain_click_and_write(1039, 1051, "Ed", duration=1)

# print("Move your mouse to the target location.")
# time.sleep(5)  # Gives you 5 seconds to move the mouse to the target

# # Get the mouse position
# x, y = p.position()
# print(f"Mouse is at: x={x}, y={y}")
# p.write('Ed', interval=0.1)

# print(p.position())

def match_button(img):
    button_location = p.locateOnScreen(img, confidence=0.9)  # Adjust confidence as needed

    if button_location:
        x, y = p.center(button_location)  # Get the center of the button
        print(f"Button found at: {x}, {y}")
        p.moveTo(x, y, duration=1)
        p.click()
    else:
        print("Button not found!")


match_button("next.png")