from flask import Flask
app = Flask(__name__)

types = [(0,47),(0,50),(55,55),(-55,55),(75,47),(-75,47),(20,51),(-20,51),(-30,47),(-30,47)]


@app.route('/<int:action>')
def movePWM(action):
    func
    return 'action : %d'%action
    


if __name__ == '__main__':
    app.run()