"""This file contains random data which will be used for generating logs files"""

import random

# Functions to generate random data which return an array of a kind

times = 20 # Times the loops will create random data

def generateDates():
    dates = []

    for i in range(times):
        year = 2025
        month = random.randint(1, 13)
        day = random.randint(1, 32)

        full_date = str(year) + ' - ' + str(month) + ' - ' + str(day)
        dates.append(full_date)
    
    return dates


def generateTimes():
    times = []
    
    for i in range(times):
        hours = random.randint(25)
        minutes = random.randint(60)
        seconds = random.randint(60)

        if hours < 10:
            hours = '0' + hours
        
        if minutes < 10:
            minutes = '0' + minutes

        if seconds < 10:
            seconds = '0' + seconds

        full_hour = str(hours) + ':' + str(minutes) + ':' + str(seconds)
        times.append(full_hour)

    return times


def generateEvents():
    events = ['WARNING', 'ERROR', 'INFO']

    full_events = []
    
    for i in range(times):
        index = random.randint(0, len(events) - 1)
        full_events.append(events[index])

    return full_events


def generateIps():
    adresses = []

    for i in range(times):
        first_section = random.randint(0, 256)
        second_section = random.randint(0, 256)
        third_section = random.randint(0, 256)
        fourth_section = random.randint(0, 256)

        ip_adress = str(first_section) + '.' + str(second_section) + '.' + str(third_section) + '.' + str(fourth_section)
        adresses.append(ip_adress)

    return adresses


def generateMessages():
    messages = [
        'Server started successfully on port 8080',
        'User authentication request received',
        'Disk space is below 15%',
        'Failed to connect to database',
        'New user admin created',
        'Cache cleared successfully',
        'Timeout while fetching data from API',
        'Deprecated function getUserData called',
        'Backup completed at 02:45 AM',
        'Session token validated successfully'
    ]

    full_messages = []

    for i in range(times):
        index = random.randint(0, len(messages) - 1)
        new_message = messages[index]
        full_messages.append(new_message)

    return full_messages

dates = generateDates()
times = generateTimes()
events = generateEvents()
ips = generateIps()
messages = generateMessages()

# Functions that return a random value for the specified array

def getDates():
    index = random.randint(0,len(dates) - 1)
    return dates[index]

def getTimes():
    index = random.randint(0,len(times) - 1)
    return times[index]

def getEvents():
    index = random.randint(0,len(events) - 1)
    return events[index]

def getIps():
    index = random.randint(0,len(ips) - 1)
    return ips[index]

def getMessages():
    index = random.randint(0,len(messages) - 1)
    return messages[index]

