from flask import Flask
from flask_socketio import SocketIO, join_room, leave_room, emit
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY') or os.urandom(24).hex()
socketio = SocketIO(app, cors_allowed_origins="*")

@socketio.on('join-room')
def handle_join_room(meeting_id, user_id):
    join_room(meeting_id)
    print(f'User {user_id} joined room {meeting_id}')
    socketio.emit('user-connected', user_id, room=meeting_id)

@socketio.on('disconnect')
def handle_disconnect():
    print('User disconnected')

if __name__ == '__main__':
    socketio.run(app)
