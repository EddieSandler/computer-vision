import pyautogui as p
import time
import cv2

# button_location = p.locateOnScreen("next.png", confidence=0.9)
# download_button_location=p.locateOnScreen("download.png",confidence=.9)
# download_now_button_location=p.locateOnScreen("download_now.png",confidence=.9)
save_button_location = p.locateOnScreen("save.png", confidence=0.9)

# if button_location:
#     x, y = p.center(button_location)  # Get the center of the button
#     print(f"Button found at: {x}, {y}")
#     p.moveTo(x, y, duration=1)
#     p.click()

# else:
#     print("Button not found!")


# if download_button_location:
#     x, y = p.center(download_button_location)  # Get the center of the button
#     print(f"Button found at: {x}, {y}")
#     p.moveTo(x, y, duration=1)
#     p.click()

# else:
#     print("Button not found!")


# if download_now_button_location:
#     x, y = p.center(download_now_button_location)  # Get the center of the button
#     print(f"Button found at: {x}, {y}")
#     p.moveTo(x, y, duration=1)
#     p.click()

# else:
#     print("Button not found!")


if save_button_location:
    x, y = p.center(save_button_location)  # Get the center of the button
    print(f"Button found at: {x}, {y}")
    p.moveTo(x, y, duration=1)
    p.click()

else:
    print("Button not found!")
