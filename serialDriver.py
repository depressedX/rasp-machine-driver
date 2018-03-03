# coding:utf-8
# 树莓派通过串口从TX2接受电机控制信号
import serial
import json
import driver

positionTypes = [(0, 27), (0, 30), (55, 35), (-55, 35), (75, 27), (-75, 27), (20, 31), (-20, 31), (-30, 27), (-30, 27)]


def handleSignal(signal):
    signal_type = signal['type']
    if signal_type == 'start':
        print('start')
        driver.init()
    elif signal_type == 'shutdown':
        print('shutdown')
        driver.destroy()
    elif signal_type == 'load':
        payload = signal['payload']
        if payload == 'load':
            print('start load balls')
            driver.loadBalls()
            driver.startLoadMotor()
        elif payload == 'unload':
            print('start unload balls')
            driver.unloadBalls()
            driver.startLoadMotor()
        elif payload == 'pause':
            print('pause load motor')
            driver.stopLoadMotor()
        else:
            print('wrong action {}'.format(payload))
    elif signal_type == 'position':
        pos = signal['payload']
        if type(pos) == int and 0 <= pos <= 9:
            print('move to position {}'.format(pos))
            driver.changeUpDutyCycle(positionTypes[pos][1])
            driver.changeDownDutyCycle(positionTypes[pos][1])
            driver.movePWM(positionTypes[pos][0])
        else:
            print('wrong position {}'.format(pos))
    else:
        print('wrong signal type {}'.format(signal_type))


def listen():
    # 波特率
    baudrate = 19200

    ser = serial.Serial('/dev/ttyAMA0', baudrate)
    print('listening on {}'.format(ser.name))

    buffer_string = bytes()
    try:
        while True:
            x = ser.read(1)
            if str(x) == '\0':
                # 已经结束
                handleSignal(json.loads(buffer_string))
                print('receive data: {}'.format(buffer_string))
                buffer_string = bytes()
            else:
                buffer_string = buffer_string + x

    finally:
        ser.close()
