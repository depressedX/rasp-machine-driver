# coding:utf-8
# 随机落点发球
import driver
import random

positionTypes = [(0, 27), (0, 30), (55, 35), (-55, 35), (75, 27), (-75, 27), (20, 31), (-20, 31), (-30, 27), (-30, 27)]


def changPosition(position):
    print('change to position {}'.format(position))
    driver.changeUpDutyCycle(positionTypes[position][1])
    driver.changeDownDutyCycle(positionTypes[position][1])
    driver.movePWM(positionTypes[position][0])


driver.init()
try:
    driver.stopLoadMotor()
    driver.loadBalls()
    while True:
        pos = random.randint(0, 9)
        changPosition(pos)
finally:
    driver.destroy()
