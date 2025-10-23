from . import random_data as data

import random
import os

lines = random.randint(1000, 2001)
directory = 'logs'

# It returns the number of files within the directory

def getSize(directory):
    content = os.listdir(directory)
    file_number = len(content)

    return file_number

# Function to create the file with the name specified

def create_file(name):

    os.makedirs(directory, exist_ok=True) # If the file doesn´t exists, it creates it

    file = open(directory+'/'+name+ '_' + str((getSize(directory) + 1)) + '.txt', 'w')
    for i in range(lines):
        date = data.getDates()
        time = data.getTimes()
        event = data.getEvents()
        ip = data.getIps()
        message = data.getMessages()
        
        file.write(date + ';' + time + ';' + event + ';' + ip + ';' + message + '\n')

    file.close()
