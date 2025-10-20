"""This file contains random data which will be used for generating logs files"""  
import random

dates = ['a','b','c']
times = [1,2,3]
events = ['hola', 'adios']
ips = ['1.2.3','4.5.6']
messages = ['hola mundo', 'adios mundo']

def getDates():
    index = random.randint(0,len(dates))
    return dates[index]

def getTimes():
    index = random.randint(0,len(times))
    return times[index]

def getEvents():
    index = random.randint(0,len(events))
    return events[index]

def getIps():
    index = random.randint(0,len(ips))
    return ips[index]

def getMessages():
    index = random.randint(0,len(messages))
    return messages[index]

