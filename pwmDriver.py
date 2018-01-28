import GPIO as GPIO
import time

# PWM电机针脚
PWM_PULSE_PIN = 40
# 方向信号针脚
PWM_DIRECTION_PIN = 38

# 步进频率
FREQUENCY = 12000
# 占空比
DUTY_CIRCLE = .5
# 最大偏转角度
MAX_ANGLE = 45
# 转动一圈需要的周期数
STEPS_PER_CIRCLE = 6400

# 当前位置
curLocation = 0
# 当前方向
positiveDirection = True


# location [-100,100]
def move(location):
    # 越界
    if location < -100 or location > 100:
        return
    if location == curLocation:
        return
    elif location < curLocation:
        GPIO.output(PWM_DIRECTION_PIN, GPIO.HIGH)
    else:
        GPIO.output(PWM_DIRECTION_PIN, GPIO.LOW)
    angle = abs(curLocation - location) / 100 * MAX_ANGLE
    steps = angle / 360 * STEPS_PER_CIRCLE
    sleepTime = steps/FREQUENCY

    pwm.ChangeDutyCycle(.5)
    time.sleep(sleepTime)
    pwm.ChangeDutyCycle(0)

    pass


try:
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(PWM_PULSE_PIN, GPIO.OUT)
    GPIO.setup(PWM_DIRECTION_PIN, GPIO.OUT)

    pwm = GPIO.PWM(PWM_PULSE_PIN, FREQUENCY)
    pwm.start(0)
except SyntaxError:
    print(SyntaxError)
finally:
    GPIO.cleanup()
