#!/usr/bin/env python
import time
from flask import Flask, render_template, session, request
from flask_socketio import SocketIO, emit, join_room, leave_room, close_room, rooms, disconnect
from libs.SevenSegment import SevenSegment

async_mode = None

room_name = 'The Library'

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, async_mode=async_mode)
thread = None
count = 0


def countdown_thread():
    global thread
    global count

    # Init the display
    display = SevenSegment()
    display.begin()
    socketio.sleep(2)
    display.clear()
    display.write_display()

    colon = True

    # Keep track of time so each iteration of the loop will be as close to 1 second as possible
    next_call = time.time()

    while count >= 0:
        # Format count
        mins, secs = divmod(count, 60)
        timeformat = '{:02d}.{:02d}'.format(mins, secs)
        webtimeformat = '{:02d}:{:02d}'.format(mins, secs)

        # Write count to display
        display.clear()
        display.print_float(float(timeformat))
        display.set_colon(colon)
        display.write_display()

        # Send time to the UI
        socketio.emit('countdown_response', {'countdown': webtimeformat}, namespace='/etv')
        count -= 1

        # Sleep for as close to 1 second between iterations as possible
        next_call += 1
        socketio.sleep(max(0, next_call - time.time()))

    display.clear()
    display.write_display()

    thread = None


@app.route('/')
def index():
    return render_template('index.html', async_mode=socketio.async_mode, room_name=room_name)


@socketio.on('start_reset_event', namespace='/etv')
def start_reset(countdown_minutes):
    global thread
    global count
    count = int(countdown_minutes['data']) * 60
    if thread is None:
        thread = socketio.start_background_task(target=countdown_thread)


@socketio.on('stop_event', namespace='/etv')
def stop():
    global count
    count = 0


@socketio.on('add_event', namespace='/etv')
def add(mins):
    global count
    count += int(mins['data']) * 60


@socketio.on('subtract_event', namespace='/etv')
def subtract(mins):
    global count
    count -= int(mins['data']) * 60


if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', debug=True)
