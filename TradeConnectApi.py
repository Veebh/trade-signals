from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from flask_cors import CORS


app = Flask(__name__)
CORS(app) 
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('connect')
def handle_connect():
    print('Client connected')

@socketio.on('disconnect')
def handle_disconnect():
    print('Client disconnected')

@app.route('/send_notification')
def send_notification():
    message = 'New notification!'
    socketio.emit('notification', {'message': message})
    return 'Notification sent'

if __name__ == '__main__':
    socketio.run(app, debug=True)
    app.run(debug=True)