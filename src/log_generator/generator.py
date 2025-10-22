import random_data as data
import random

# Function to create the file with the name specified
lines = random.randint(1000, 2001)

def create_file(name):
    file = open('logs/'+name, 'w')
    for i in range(lines):
        date = data.getDates()
        time = data.getTimes()
        event = data.getEvents()
        ip = data.getIps()
        message = data.getMessages()
        
        file.write(date + ' ' + time + ' ' + event + ' ' + ip + ' ' + message)
