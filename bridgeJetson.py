# coding:utf-8
# 树莓派与jetson TX2的串口通信驱动程序 TX2端
import GPIOTX2Adapter as GPIO
import time

# 0xxxx postition:x
# 100xx load load:0 unload:1 pause:2
# 1010x start:0 shutdown:1

# 准备信号管脚 高电平就绪
readySignalPin = 0

# 数据管脚
dataPins = (5, 1, 2, 3, 4)


def init():
    GPIO.setmode(GPIO.BOARD)

    GPIO.setup(readySignalPin, GPIO.OUT)
    GPIO.setup(readySignalPin, False)
    for pin in dataPins:
        GPIO.setup(pin, GPIO.OUT)
        GPIO.setup(pin, False)


def destroy():
    GPIO.cleanup()


# 改为就绪状态
def makeItReady():
    GPIO.setup(readySignalPin, True)

    # 单线程同步操作 保证0.1s内数据被读取
    time.sleep(.1)

    GPIO.setup(readySignalPin, False)


# 向数据管道写入数据
def writeData(dataStr):
    print('write {}'.format(dataStr))
    for index, pin in enumerate(dataPins):
        GPIO.output(pin, True if dataStr[index] == '1' else False)


def start():
    writeData('10100')


def shutdown():
    writeData('10101')


def __dec2FixedBinary(num, len):
    binArr = bin(num)[2:]
    res = ('{0:0>' + str(len) + '}').format(binArr)
    return res


def reachPosition(position):
    writeData('0{}'.format(__dec2FixedBinary(position, 4)))


def loadBalls():
    writeData('10000')


def unloadBalls():
    writeData('10001')


def pauseLoadMotor():
    writeData('10010')


if __name__ == '__main__':
    reachPosition(1)
