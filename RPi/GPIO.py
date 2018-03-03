# coding:utf-8
# 树莓派平台GPIO
def setmode(mode_type):
    pass


def setup(channel, type):
    pass


def output(channel, state):
    pass


def cleanup():
    pass


def input(channel):
    pass


class PWM(object):
    def __init__(self, channel, frequency):
        pass

    def start(self, dc):
        pass

    def stop(self):
        pass

    def ChangeDutyCycle(self, dc):
        pass

    def ChangeFrequency(self, f):
        pass


BOARD = 1
OUT = 1
LOW = -1
HIGH = 1
IN = 0
