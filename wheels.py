import gpiozero
from time import sleep

class Wheels:
    def __init__(self, right_for, right_back, left_for, left_back):
        self.right = gpiozero.Motor(right_for, right_back)
        self.left = gpiozero.Motor(left_for, left_back)

    def forward(self, t):
        self.right.forward()
        self.left.forward()
        sleep(t)
        self.right.stop()
        self.left.stop()

    def backward(self, t):
        self.right.backward()
        self.left.backward()
        sleep(t)
        self.right.stop()
        self.left.stop()

    def turn_left(self, t):
        self.right.backward()
        self.left.forward()
        sleep(t)
        self.right.stop()
        self.left.stop()

    def turn_right(self, t):
        self.right.forward()
        self.left.backward()
        sleep(t)
        self.right.stop()
        self.left.stop()
