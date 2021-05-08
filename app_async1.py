from flask import render_template, jsonify, session,request
from random import randint
import uuid
import tasks
from init import app
from celery.result import AsyncResult

@app.route("/",methods=['GET'])
def index():
    # create a unique ID to assign for the asynchronous task
    if 'uid' not in session:
        sid = str(uuid.uuid4())
        session['uid'] = sid
        print("Session ID stored =", sid)
    return render_template('index1.html')

#Run an Asynchronous Task
@app.route("/runAsyncTask",methods=['POST'])
def long_async_task():
    print("Running", "/runAsyncTask")
    #Generate a random number between MIN_WAIT_TIME and MAX_WAIT_TIME
    n = randint(app.config['MIN_WAIT_TIME'],app.config['MAX_WAIT_TIME'])
    sid = str(session['uid'])
    task = tasks.long_async_task.delay(n=n,session=sid)
    #print('taskid',task.id,'sessionid',sid,'waittime',n )
    return jsonify({'taskid':task.id,'sessionid':sid,'waittime':n })

#Get The Result of The Asynchronous Task
@app.route('/getAsyncTaskResult', methods=['GET', 'POST'])
def result():
    task_id = request.args.get('taskid')
    # grab the AsyncResult
    result = AsyncResult(task_id)
    # print the task id
    print("Task ID = ", result.task_id)
    # print the Asynchronous result status
    print("Task Status = ", result.status)
    return jsonify({'taskid': result.task_id, 'taskstatus': result.status})

if __name__ == "__main__":
   app.run(debug=True)
