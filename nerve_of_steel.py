"""
This program is used as an example for MGTC28.
timer.py is a simple Python script that will allow user to set timer duration.
Upon timer expiry, user will see the time up meme and sound notification.
timer.py uses the time library to help keep track of time
"""



from PIL import Image
import time
from random import randint
im = Image.open("display_last.jpg")
print("Players stand")
time.sleep(randint(5,25))
#print("Times up! Last to sit down wins")
im.show()

