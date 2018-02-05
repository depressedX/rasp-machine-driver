# coding:utf-8
# 树莓派与jetson TX2的并口通信驱动程序 树莓派端
import GPIO
import driver

# 准备信号管脚 高电平就绪
readySignalPin = 0

# 数据管脚
dataPins = (5, 1, 2, 3, 4)

# 旋转电机移动位置
positionTypes = [(0, 27), (0, 30), (55, 35), (-55, 35), (75, 27), (-75, 27), (20, 31), (-20, 31), (-30, 27), (-30, 27)]


def init():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(readySignalPin, GPIO.IN)
    for pin in dataPins:
        GPIO.setup(pin, GPIO.IN)
    driver.init()


def booleanArray2Str(arr):
    res = ''
    for i in arr:
        res = res + ('1' if arr[i] else '0')
    return res


def binary2Dec(str):
    return int(str, 2)


def parseDataAndExecute(data):
    # 0xxxx postition:x
    # 100xx load load:0 unload:1 pause:2
    # 1010x start:0 shutdown:1
    if not data[0]:
        position = binary2Dec(booleanArray2Str(data[1:]))
        if not (0 <= position <= 9):
            print('out of bounds {}'.format(position))
            return
        driver.changeUpDutyCycle(positionTypes[position][1])
        driver.changeDownDutyCycle(positionTypes[position][1])
        driver.movePWM(positionTypes[position][0])
        print('move to position %d' % position)
    elif binary2Dec(booleanArray2Str(data[0:3])) == 4:
        loadType = binary2Dec(data[3:])
        if loadType == 0:
            driver.loadBalls()
            driver.startLoadMotor()
            print('start load balls')
        elif loadType == 1:
            driver.unloadBalls()
            driver.startLoadMotor()
            print('start unload balls')
        elif loadType == 2:
            driver.stopLoadMotor()
            print('pause load motor')
        else:
            print('bad action : {}'.format(loadType))
    elif binary2Dec(booleanArray2Str(data[0:4])) == 10:
        if data[4]:
            print('shutdown')
            driver.destroy()
        else:
            print('start')
            driver.init()


# 开始监听
def listen():
    init()
    print('start listening...')
    try:
        while True:
            isReady = GPIO.input(readySignalPin)
            if not isReady:
                continue
            data = []
            for dataPin in dataPins:
                data.append(GPIO.input(dataPin))
            print('receive {}'.format(data))
            parseDataAndExecute(data)
    finally:
        GPIO.cleanup()
        driver.destroy()


if __name__ == '__main__':
    listen()
