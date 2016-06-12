import picamera
import os

camera = picamera.PiCamera()
camera.hflip = True
camera.vflip = True
keep = 10
tempFile = 'control/static/images/tmp_view.jpg'
viewFile = 'control/static/images/view.jpg'
while True:
    camera.capture('control/static/images/tmp_view.jpg')
    for i in reversed(range(keep)):
        fl1 = viewFile + str(i)
        fl2 = viewFile + str(i+1)
        if os.path.isfile(fl1):
            os.rename(fl1, fl2)
    os.rename(viewFile, viewFile + '0')
    os.rename(tempFile, viewFile)
