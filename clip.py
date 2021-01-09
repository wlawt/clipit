import cv2
import pyautogui
import numpy as np
import keyboard
import os
import urllib
import ray
import subprocess

from datetime import datetime
from mic import record_to_file
# from win10toast import ToastNotifier

# Run funcs in parallel
ray.init()
toaster = ToastNotifier()

@ray.remote
def VideoRecord(file):
  codec = cv2.VideoWriter_fourcc(*"XVID")
  out = cv2.VideoWriter(file, codec, 30, (1920, 1080))

  while True:
    img = pyautogui.screenshot()
    frame = np.array(img)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    out.write(frame)

    if keyboard.is_pressed('F8'):
      # icon_path="./clipit/public/logo.jpg"
      # toaster.show_toast("Clip It","Stopping recording...", duration=5)
      print("%s Key pressed." % 'F8')
      break
  
  out.release()
  cv2.destroyAllWindows()

@ray.remote
def MicRecord(micPath):
  record_to_file(micPath)

while True:
  if keyboard.is_pressed('F4'):
    # toaster.show_toast("Clip It","Starting to record...", duration=5)
    print("Starting to record")

    fileName = datetime.now().strftime("%d%m%Y%H%M%S") # avoid name conflict

    orgClip = "./clipit/clips/" + fileName + ".avi"
    micPath = "./clipit/clips/" + fileName + ".wav"
    clipPath = "./clipit/clips/" + fileName + ".mp4"
    
    # Run concurrently
    out_vid = VideoRecord.remote(orgClip)
    out_mic = MicRecord.remote(micPath)

    vid, mic = ray.get([out_vid, out_mic])

    # Convert .avi to .mp4 with audio (.wav)
    cmd = "ffmpeg -i " + orgClip + " -i " + micPath + " -c:v copy -c:a aac " + clipPath
    subprocess.call(cmd, shell=True)

    # Remove .avi and .wav files
    os.remove(orgClip)
    os.remove(micPath)