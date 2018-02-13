# coding:utf-8
# TX2用于通过串口向树莓派发送电机控制指令程序
import serial
import json

# 波特率
baudrate = 19200

ser = serial.Serial()
ser.baudrate = baudrate
ser.port = '/dev/ttyTHS2'


def init():
    global ser

    ser.open()
    print('using {}'.format(ser.name))


def start():
    jsonObject = {
        'type': 'start'
    }
    print('start')
    ser.write(bytes(json.dumps(jsonObject) + '\0'))


def shutdown():
    jsonObject = {
        'type': 'shutdown'
    }
    print('shutdown')
    ser.write(bytes(json.dumps(jsonObject) + '\0'))


def loadBalls():
    jsonObject = {
        'type': 'load',
        'payload': 'load'
    }
    print('start load balls')
    ser.write(bytes(json.dumps(jsonObject) + '\0'))


def unloadBalls():
    jsonObject = {
        'type': 'load',
        'payload': 'unload'
    }
    print('start unload balls')
    ser.write(bytes(json.dumps(jsonObject) + '\0'))


def stopLoadMotor():
    jsonObject = {
        'type': 'load',
        'payload': 'pause'
    }
    print('stop load motor')
    ser.write(bytes(json.dumps(jsonObject) + '\0'))


def move(pos):
    if not (type(pos) == int and 0 <= pos <= 9):
        print('wrong parameter : position {}'.format(pos))
        return
    jsonObject = {
        'type': 'position',
        'payload': pos
    }
    print('move to position {}'.format(pos))
    ser.write(bytes(json.dumps(jsonObject) + '\0'))


# 必须结束程序前调用
def destroy():
    global ser
    if ser.is_open:
        ser.close()
