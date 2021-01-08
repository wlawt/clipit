import cv2
import pyautogui
import numpy as np
import keyboard
import ffmpy
import os
import urllib
from multiprocessing import Process
import subprocess
# import time
from datetime import datetime
from selenium import webdriver
from mic import record_to_file

def VideoRecord():
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

def AVRecord(micPath):
    vid_thread = Process(target=VideoRecord())
    vid_thread.start()

    mic_thread = Process(target=record_to_file(micPath))
    mic_thread.start()

    mic_thread.join()
    vid_thread.join()

while True:
  if keyboard.is_pressed('F4'):
    print("Starting to record")

    fileName = datetime.now().strftime("%d%m%Y%H%M%S") # avoid name conflict

    file = "./clipit/clips/" + fileName + ".avi"
    micPath = "./clipit/clips/" + fileName + ".wav"
    clipPath = "./clipit/clips/" + fileName + ".mp4"

    AVRecord(micPath)

    #video_thread = threading.Thread(target=AVRecord(fileName, micPath))
    #video_thread.start()

    # mic_thread = threading.Thread(target=record_to_file(micPath))
    # mic_thread.start()
    

    #cmd = "ffmpeg -ac 2 -channel_layout stereo -i " +  micPath + " -i " + file + " -pix_fmt yuv420p " + clipPath
    cmd = "ffmpeg -i " + file + " -i " + micPath + " -c:v copy -c:a aac " + clipPath
    subprocess.call(cmd, shell=True)

    # Convert .avi to .mp4
    """ mp4_file = "./clipit/clips/" + fileName + ".mp4"
    ff = ffmpy.FFmpeg(
      inputs={file:None},
      outputs={mp4_file:None}
    )

    ff.run()
    os.remove(file) # remove .avi file """

""" print("Reloading with new site")
    driver = webdriver.Chrome()
    driver.get("http://localhost:3000")
    driver.refresh()
    time.sleep(3)
    driver.quit() """