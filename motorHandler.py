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
    
    if angle > MAX_ROTATION_THETA or angle < -MAX_ROTATION_THETA:
    	print('out of bounds!')
    	return

    delta = angle - curAngle
    if delta > 0:
        # 顺时针旋转
        GPIO.output(PWM_DIRECTION_PIN, GPIO.LOW)
    else:
        # 逆时针旋转
        GPIO.output(PWM_DIRECTION_PIN, GPIO.HIGH)
        delta = -delta
    time.sleep(.05)
    steps = int(delta / SINGLE_STEP_ANGLE)
    for i in range(steps):
        pulse(PWM_PULSE_PIN, pwmPulseFactor)
        time.sleep(pwmSpeedFactor)
    curAngle = steps * SINGLE_STEP_ANGLE
    
    print('moveto ',angle,' now ',curAngle)


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

def init():
    #global upMotor, downMotor, loadMotorFre
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
        loadMotor = GPIO.PWM(LOAD_PULSE_PIN, loadMotorFrequency)
    except SyntaxError:
        print('初始化失败 重新执行')
        #GPIO.cleanup()
        print(Exception)
        
        
def destroy():
    GPIO.cleanup()


if __name__ == '__main__':
    print('run main')
