from flask import render_template, jsonify
from random import randint
from init import app
import tasks

#Render the predefined template index.html
@app.route("/",methods=['GET'])
def index():
    return render_template('index.html')

#Defining the route for running A Synchronous Task
@app.route("/runSyncTask",methods=['POST'])
def long_sync_task():
    print("Running","/runSyncTask")
    #Generate a random number between MIN_WAIT_TIME and MAX_WAIT_TIME
    n = randint(app.config['MIN_WAIT_TIME'],app.config['MAX_WAIT_TIME'])
    #Call the function long_sync_task included within tasks.py
    task = tasks.long_sync_task(n=n)
    #Return the random wait time generated
    return jsonify({ 'waittime': n })

if __name__ == "__main__":
    app.run(debug=True)
