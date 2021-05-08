#Application configuration File
################################

#Secret key that will be used by Flask for securely signing the session cookie
# and can be used for other security related needs
SECRET_KEY = 'SECRET_KEY'

#Map to REDIS Server Port
BROKER_URL = 'redis://localhost:6379'

#Minimum interval of wait time for our task
MIN_WAIT_TIME = 1
#Maximum interval of wait time for our task
MAX_WAIT_TIME = 20
