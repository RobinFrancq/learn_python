import time, datetime

# het aantal seconden sinds 1 jan 1970
epochseconds = time.time()
print(epochseconds)

# de datum en tijd krijgen volgens epoch
t = time.ctime(epochseconds)
print(t)

# Abdere manier met datetime
dt = datetime.datetime.today()
print('Current date: {}/{}/{}'.format(dt.day, dt.month, dt.year))
print('Current time: {}/{}/{}'.format(dt.hour, dt.minute, dt.second))

