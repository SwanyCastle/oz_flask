from flask import Flask, render_template
from flask_socketio import SocketIO

import yaml

secret_key = ""
with open("key.yaml", "r") as f:
    key = yaml.load(f, Loader=yaml.FullLoader)
    secret_key = key["secret_key"]

app = Flask(__name__)
app.config['SECRET_KEY'] = secret_key
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

def messageReceived(methods=['GET', 'POST']):
    print('message was received!!!')
    # DB 에다가 채팅 데이터 저장

@socketio.on('my event')
def handle_my_custom_event(json, methods=['GET', 'POST']):
    print(f'데이터 수신 완료: {str(json)}')
    socketio.emit('my response', json, callback=messageReceived)

if __name__ == '__main__':
    socketio.run(app, debug=True)