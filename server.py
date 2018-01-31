# coding:utf-8
from flask import Flask
import driver

app = Flask(__name__)

positionTypes = [(0, 27), (0, 30), (55, 35), (-55, 35), (75, 27), (-75, 27), (20, 31), (-20, 31), (-30, 27), (-30, 27)]


@app.route('/')
def root():
    return 'hello world!'


@app.route('/start')
def start():
    driver.init()
    return 'OK'


@app.route('/shutdown')
def shutdown():
    driver.destroy()
    return 'OK'


# action: load unload pause
@app.route('/load/<action>')
def load(action):
    if action == 'load':
        driver.loadBalls()
        driver.startLoadMotor()
    elif action == 'unload':
        driver.unloadBalls()
        driver.startLoadMotor()
    elif action == 'pause':
        driver.stopLoadMotor()
    else:
        return 'bad action : {}'.format(action)
    return 'OK {}'.format(action)


@app.route('/position/<int:position>')
def position(position):
    if not(0 <= position <= 9):
        return 'out of bounds {}'.format(position)
    driver.changeUpDutyCycle(positionTypes[position][1])
    driver.changeDownDutyCycle(positionTypes[position][1])
    driver.movePWM(positionTypes[position][0])
    return 'move to position %d' % position


@app.route('/move/<int:angle>')
def move(angle):
    driver.movePWM(angle)
    return 'move to %d' % angle 


if __name__ == '__main__':
    try:
        app.run(host='0.0.0.0')
    finally:
        driver.destroy()