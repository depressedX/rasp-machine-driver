# coding:utf-8
import time
import GPIO as GPIO

# 上电机脉冲针脚
UP_PULSE_PIN = 40

# 下电机脉冲针脚
DOWN_PULSE_PIN = 40

# 进卸球脉冲\方向针脚
LOAD_PULSE_PIN = 40
LOAD_DIRECTION_PIN = 40

# 步进电机脉冲\方向针脚
PWM_PULSE_PIN = 40
PWM_DIRECTION_PIN = 40

# 步进电机最大旋转角度
MAX_ROTATION_THETA = 40

# 步进电机单步移动角度
SINGLE_STEP_ANGLE = 1.8 / 4
# 步进电机当前角度
curAngle = 0
# 步进电机移动速度因子
pwmSpeedFactor = .05

upMotor = None
downMotor = None
loadMotor = None

upMotorFrequency = 100
downMotorFrequency = 100
loadMotorFrequency = 50
upMotorDutyCycle = 50
downMotorDutyCycle = 50
loadMotorDutyCycle = 50
loadMotorDirection = GPIO.LOW


# 发出一个脉冲信号
def pulse(channel, long):
    GPIO.output(channel, GPIO.HIGH)
    time.sleep(long)
    GPIO.output(channel, GPIO.LOW)


# PWM电机旋转角度[-max, max]
def movePWM(angle):
    global curAngle

    delta = angle - curAngle
    if delta > 0:
        # 顺时针旋转
        GPIO.output(PWM_DIRECTION_PIN, GPIO.LOW)
        delta = -delta
    else:
        # 逆时针旋转
        GPIO.output(PWM_DIRECTION_PIN, GPIO.HIGH)
    steps = int(delta / SINGLE_STEP_ANGLE)
    for i in range(steps):
        pulse(PWM_PULSE_PIN, .05)
        time.sleep(pwmSpeedFactor)
    curAngle = steps * SINGLE_STEP_ANGLE


# 修改上旋电机速度 [0,1]
def changeUpSpeed(rate):
    pass


# 修改上旋电机速度 [0,1]
def changeDownSpeed(rate):
    pass


# 修改装\卸载球的速度
def changeLoadMotorSpeed(rate):
    pass


# 开始装载球
def startLoadBalls():
    pass


# 暂停装载\卸载
def stopLoadMotor():
    pass


# 开始卸载球
def startUnloadBalls():
    pass


try:
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(UP_PULSE_PIN, GPIO.OUT)
    GPIO.setup(DOWN_PULSE_PIN, GPIO.OUT)
    GPIO.setup(LOAD_PULSE_PIN, GPIO.OUT)
    GPIO.setup(LOAD_DIRECTION_PIN, GPIO.OUT)
    GPIO.setup(PWM_PULSE_PIN, GPIO.OUT)
    GPIO.setup(PWM_DIRECTION_PIN, GPIO.OUT)

    upMotor = GPIO.PWM(UP_PULSE_PIN, upMotorFrequency)
    downMotor = GPIO.PWM(DOWN_PULSE_PIN, downMotorFrequency)
    loadMotorFrequency = GPIO.PWM(LOAD_PULSE_PIN, loadMotorFrequency)
except RuntimeError:
    print(RuntimeError)
finally:
    GPIO.cleanup()
