import cv2
import pyautogui
import numpy as np
import keyboard
import ffmpy
import os
import urllib
# import time
from datetime import datetime
from selenium import webdriver

while True:
  if keyboard.is_pressed('F4'):
    print("Starting to record")

    fileName = datetime.now().strftime("%d%m%Y%H%M%S") # avoid name conflict
    file = "./clipit/clips/" + fileName + ".avi"

    codec = cv2.VideoWriter_fourcc(*"XVID")
    out = cv2.VideoWriter(file, codec, 30, (1920, 1080))

    while True:
      img = pyautogui.screenshot()
      frame = np.array(img)
      frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
      # time.sleep(0.16)
      out.write(frame)

      if keyboard.is_pressed('F8'):
        print("%s Key pressed." % 'F8')
        break
    
    out.release()
    cv2.destroyAllWindows()

    # Convert .avi to .mp4
    mp4_file = "./clipit/clips/" + fileName + ".mp4"
    ff = ffmpy.FFmpeg(
      inputs={file:None},
      outputs={mp4_file:None}
    )

    ff.run()
    os.remove(file) # remove .avi file

""" print("Reloading with new site")
    driver = webdriver.Chrome()
    driver.get("http://localhost:3000")
    driver.refresh()
    time.sleep(3)
    driver.quit() """