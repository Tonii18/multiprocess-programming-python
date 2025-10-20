import random_data as data

dates = data.getDates()
times = data.getTimes()
events = data.getEvents()
ips = data.getIps()
messages = data.getMessages()

line = (dates + times + events + ips + messages)
print(line)