# coding:utf-8
# tx2平台上的GPIO包接口适配
from periphery import GPIO

OUT = 'out'
IN = 'in'

BOARD = None

pinObjects = {}


def setmode(mode):
    pass


def setup(channel, state):
    pinObjects[channel] = GPIO(channel, state)


def output(channel, value):
    pinObjects[channel].write(value)


def cleanup():
    for pinObject in pinObjects:
        pinObject.write(False)
        pinObject.close()
