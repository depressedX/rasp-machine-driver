from flask import Flask

app = Flask(__name__)

types = [(0, 47), (0, 50), (55, 55), (-55, 55), (75, 47), (-75, 47), (20, 51), (-20, 51), (-30, 47), (-30, 47)]


@app.route('/')
def root():
    return 'hello world!'


@app.route('/start')
def start():
    return 'OK'


@app.route('/shutdown')
def shutdown():
    return 'OK'


# action: load unload pause
@app.route('/load/<action>')
def load(action):
    return 'OK %' % action


@app.route('/position/<int:action>')
def action(action):
    return 'action %d' % action


if __name__ == '__main__':
    app.run()
