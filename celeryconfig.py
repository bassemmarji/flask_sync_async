#Celery Configuration parameters
#Map to Redis server
broker_url = 'redis://localhost:6379/0'

#Backend used to store the tasks results
result_backend = 'redis://localhost:6379/0'

#A string identifying the default serialization to use Default json
task_serializer = 'json'
result_serializer = 'json'
accept_content = ['json']

#When set to false the local system timezone is used.
enable_utc = False

#To track the started state of a task, we should explicitly enable it
task_track_started = True

#Configure Celery to use a specific time zone.
#The timezone value can be any time zone supported by the pytz library
#timezone = 'Asia/Beirut'
#enable_utc = True
