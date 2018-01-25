
# coding: utf-8
# c o
# In[ ]:

my_commands = {
    "#takePicture" : {"module": "camera", "method": "take_picture", "notes":""},
}

def get_my_commands():
    return my_commands

def take_picture(a_text):
    password = ""
    if len(a_text) > 0:
        password = a_text[0]
    if (password == "mypi"):
        camera.capture('image.jpg')
        return {"text": "I have taken a picture!", "photo":"image.jpg"}
    else:
        return {"text": "Wrong password!"}

import picamera
camera = picamera.PiCamera()


# In[ ]:



