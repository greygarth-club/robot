import gpiozero
from time import sleep

class Wheels:
    def __init__(self, right_for, right_back, left_for, left_back, sensor = None):
        self.right = gpiozero.Motor(right_for, right_back)
        self.left = gpiozero.Motor(left_for, left_back)
        self.sensor = sensor
        self.speed = 1.0
        self.powerRatio = 1.0

    def setSpeed(self, speed):
        if (speed >= 0.0 and speed <= 1.0):
            self.speed = speed

    def calibrate(self, powerRatio):
        self.powerRatio = powerRatio

    def forward(self, t):
        self.goForward()
        sleep(t)
        self.stop()

    def forwardUntilClose(self, dist = 20):
        if self.sensor != None:
            self.goForward()
            while self.sensor.isFurther(dist):
                sleep(0.1)
            self.stop()

    def backward(self, t):
        self.goBackward()
        sleep(t)
        self.stop()

    def backwardUntilFurther(self, dist = 80):
        if self.sensor != None:
            self.goBackward()
            while self.sensor.isCloser(dist):
                sleep(0.1)
            self.stop()

    def turn_right(self, t):
        self.right.backward(self.speed)
        self.left.forward(self.speed)
        sleep(t)
        self.stop()

    def turn_left(self, t):
        self.right.forward(self.speed)
        self.left.backward(self.speed)
        sleep(t)
        self.stop()

    def goForward(self):
        self.right.forward(self.speed)
        self.left.forward(self.speed * self.powerRatio)

    def goBackward(self):
        self.right.backward(self.speed)
        self.left.backward(self.speed * self.powerRatio)

    def stop(self):
        self.right.stop()
        self.left.stop()
