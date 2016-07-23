import gpiozero

class Sensors:
    def __init__(self, range_echo, range_trig):
        self.range = gpiozero.DistanceSensor(range_echo, range_trig)

    def isCloser(self, distance):
        print(self.range.distance * 100)
        return self.range.distance * 100 < distance

    def isFurther(self,distance):
        print(self.range.distance * 100)
        return self.range.distance * 100 > distance
