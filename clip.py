import cv2
import pyautogui
import numpy as np
import keyboard
from datetime import datetime

while True:
  if keyboard.is_pressed('F2'):
    print("Starting to record")

    fileName = datetime.now().strftime("%d%m%Y%H%M%S")
    file = "./clips/" + fileName + ".avi"

    codec = cv2.VideoWriter_fourcc(*"XVID")
    out = cv2.VideoWriter(file, codec, 60, (1920, 1080))

    while True:
      img = pyautogui.screenshot()
      frame = np.array(img)
      frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
      out.write(frame)

      if keyboard.is_pressed('F4'):
        print("%s Key pressed." % 'F4')
        break
    
    out.release()
    cv2.destroyAllWindows()
