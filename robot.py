import wheels
import sensors
from time import sleep


#wheels.turn_left(0.2)
#wheels.forward(0.2)
#wheels.forward(0.2)
#wheels.forward(0.2)
#wheels.backward(0.2)
#wheels.turn_right(0.2)

sensor = sensors.Sensors(15, 14)
wheels = wheels.Wheels(27, 22, 25, 24, sensor)
wheels.setSpeed(0.7)
wheels.calibrate(1.1)
for i in range(10):
    wheels.forwardUntilClose(40)
    wheels.backwardUntilFurther(60)
