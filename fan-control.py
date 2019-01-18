from gpiozero import DigitalOutputDevice, MotionSensor
fan = DigitalOutputDevice(17)
sensor = MotionSensor(27)

while True:
    sensor.when_motion = fan.toggle

