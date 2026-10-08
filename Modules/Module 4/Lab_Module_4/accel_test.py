import machine
import time
from bmi270 import BMI270

i2c = machine.I2C(1, scl=machine.Pin(15), sda=machine.Pin(14))
imu = BMI270(i2c)

while True:
    x, y, z = imu.read_accel()
    print(f"x={x:+.2f}  y={y:+.2f}  z={z:+.2f}")
    time.sleep(0.2)