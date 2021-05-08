#Gevent is a coroutine based concurrency library for Python
from gevent import monkey
#For dynamic modifications of a class or module
monkey.patch_all()
from flask import render_template, jsonify, session, request
from random import randint
import uuid
import tasks
from init import app, socketio
from flask_socketio import join_room

@app.route("/",methods=['GET'])
def index():
    # create a unique session ID and store it within the Flask session
    if 'uid' not in session:
        sid = str(uuid.uuid4())
        session['uid'] = sid
        print("Session ID stored =", sid)
    return render_template('index2.html')

#Run an Asynchronous Task With Automatic Feedback
@app.route("/runAsyncTaskF",methods=['POST'])
def long_async_taskf():
    print("Running", "/runAsyncTaskF")
    # Generate a random number between MIN_WAIT_TIME and MAX_WAIT_TIME
    n = randint(app.config['MIN_WAIT_TIME'], app.config['MAX_WAIT_TIME'])

    data = {}
    data['sessionid'] = str(session['uid'])
    data['waittime']  = n
    data['namespase'] = '/runAsyncTaskF'

    task = tasks.long_async_taskf.delay(data)
    return jsonify({ 'taskid':task.id
                    ,'sessionid':data['sessionid']
                    ,'waittime':data['waittime']
                    ,'namespace':data['namespase']
                    })

@socketio.on('connect', namespace='/runAsyncTaskF')
def socket_connect():
    #Display message upon connecting to the namespace
    print('Client Connected To NameSpace /runAsyncTaskF - ',request.sid)

@socketio.on('disconnect', namespace='/runAsyncTaskF')
def socket_connect():
    # Display message upon disconnecting from the namespace
    print('Client disconnected From NameSpace /runAsyncTaskF - ',request.sid)

@socketio.on('join_room', namespace='/runAsyncTaskF')
def on_room():
    room = str(session['uid'])
    # Display message upon joining a room specific to the session previously stored.
    print(f"Socket joining room {room}")
    join_room(room)

@socketio.on_error_default
def error_handler(e):
    # Display message on error.
    print(f"socket error: {e}, {str(request.event)}")

if __name__ == "__main__":
    # Run the application with socketio integration.
    socketio.run(app,debug=True)