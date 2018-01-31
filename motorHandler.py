# coding:utf-8
import time
import RPi.GPIO as GPIO

# 上电机脉冲针脚
UP_PULSE_PIN = 40

# 下电机脉冲针脚
DOWN_PULSE_PIN = 38

# 进卸球脉冲\方向针脚
LOAD_PULSE_PIN = 37
LOAD_DIRECTION_PIN = 36

# 步进电机脉冲\方向针脚
PWM_PULSE_PIN = 33
PWM_DIRECTION_PIN = 32

# 步进电机最大旋转角度
MAX_ROTATION_THETA = 75

# 步进电机单步移动角度
SINGLE_STEP_ANGLE = 1.8 / 4
# 步进电机当前角度
curAngle = 0
# 步进电机移动速度因子
pwmSpeedFactor = .01
# 脉冲持续时间
pwmPulseFactor = .01

# 上下旋装载占空比区间
minUpDutyCycle = 20
maxUpDutyCycle = 55
minDownDutyCycle = 20
maxDownDutyCycle = 55
minLoadDutyCycle = 20
maxLoadDutyCycle = 50

# 电机频率
upFrequency = 512
downFrequency = 512
loadFrequency = 100

# 装载电机方向
loadMotorDirection = GPIO.LOW

upMotor = None
downMotor = None
loadMotor = None


# 发出一个脉冲信号
def pulse(channel, long):
    GPIO.output(channel, GPIO.HIGH)
    time.sleep(long)
    GPIO.output(channel, GPIO.LOW)


# PWM电机旋转角度[-max, max]
def movePWM(angle):
    global curAngle

    if angle > MAX_ROTATION_THETA or angle < -MAX_ROTATION_THETA:
        print('out of bounds!', angle)
        return

    delta = angle - curAngle
    reversed = False
    
    if delta > 0:
        # 顺时针旋转
        GPIO.output(PWM_DIRECTION_PIN, GPIO.HIGH)
    else:
        # 逆时针旋转
        GPIO.output(PWM_DIRECTION_PIN, GPIO.LOW)
        delta = -delta
        reversed = True
    steps = int(delta / SINGLE_STEP_ANGLE)
    for i in range(steps):
        pulse(PWM_PULSE_PIN, pwmPulseFactor)
        time.sleep(pwmSpeedFactor)
    curAngle = curAngle + (-1 if reversed else 1) * steps * SINGLE_STEP_ANGLE

    print('moveto ', angle, ' now ', curAngle)


# 修改上旋电机占空比
def changeUpDutyCycle(dc):
    upMotor.ChangeDutyCycle(dc)


# 修改下旋电机占空比
def changeDownDutyCycle(dc):
    downMotor.ChangeDutyCycle(dc)


# 修改上旋电机速度 [0,1]
def changeUpSpeed(rate):
    if not (0 <= rate <= 1):
        print('参数非法 ', str(rate))
        return
    upMotor.ChangeDutyCycle((maxUpDutyCycle - minUpDutyCycle) * rate)


# 修改下旋电机速度 [0,1]
def changeDownSpeed(rate):
    if not (0 <= rate <= 1):
        print('参数非法 ', rate)
        return
    downMotor.ChangeDutyCycle((maxDownDutyCycle - minDownDutyCycle) * rate)


# 开始装载\卸载
def startLoadMotor():
    loadMotor.start(minLoadDutyCycle)


# 暂停装载\卸载
def stopLoadMotor():
    loadMotor.stop()


# 装载球
def loadBalls():
    global loadMotorDirection
    loadMotorDirection = False
    GPIO.output(LOAD_DIRECTION_PIN, loadMotorDirection)


# 卸载球
def unloadBalls():
    global loadMotorDirection
    loadMotorDirection = True
    GPIO.output(LOAD_DIRECTION_PIN, loadMotorDirection)


# 修改装\卸载球的速度
def changeLoadMotorSpeed(rate):
    if not (0 <= rate <= 1):
        print('参数非法 ', rate)
        return
    loadMotor.ChangeDutyCycle((maxLoadDutyCycle - minLoadDutyCycle) * rate)


def init():
    global loadMotor, upMotor, downMotor
    try:
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(UP_PULSE_PIN, GPIO.OUT)
        GPIO.setup(DOWN_PULSE_PIN, GPIO.OUT)
        GPIO.setup(LOAD_PULSE_PIN, GPIO.OUT)
        GPIO.setup(LOAD_DIRECTION_PIN, GPIO.OUT)
        GPIO.setup(PWM_PULSE_PIN, GPIO.OUT)
        GPIO.setup(PWM_DIRECTION_PIN, GPIO.OUT)

        upMotor = GPIO.PWM(UP_PULSE_PIN, upFrequency)
        downMotor = GPIO.PWM(DOWN_PULSE_PIN, downFrequency)
        loadMotor = GPIO.PWM(LOAD_PULSE_PIN, loadFrequency)

        # 启动电机
        upMotor.start(minUpDutyCycle)
        downMotor.start(minDownDutyCycle)

        # debug
        # movePWM(-70)

        time.sleep(5)
        print('启动成功')
    except SyntaxError:
        print('初始化失败 重新执行')
        print(Exception)


def destroy():
    GPIO.cleanup()


if __name__ == '__main__':
    print('run main')
