import random_data as data

dates = data.getDates()
times = data.getTimes()
events = data.getEvents()
ips = data.getIps()
messages = data.getMessages()

line = (str(dates) + ' : ' + str(times) + ' : ' + str(events) + ' : ' + str(ips) + ' : ' + str(messages))
print(line)