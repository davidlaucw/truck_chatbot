#import numpy as np
import pandas as pd
import csv
from datetime import datetime as dt

logs = []
fleet=[]
def log(message):
    logs.append([dt.now().strftime('%Y-%m-%d %H:%M:%S'),message])
def start():
    message = "Hello. I am your truck chatbox."
    print(message)
    log(message)

start()
i = 0
while True:
    messageNewTruck = 'Adding the truck {} in your fleet, please input the specifications, or enter "stop" to stop:'.format(i+1)
    newTruck = input(messageNewTruck)
    log(messageNewTruck)
    log(newTruck)
    if newTruck == 'stop':
        break
    else:
        fleet.append([i+1,newTruck])
    i+=1

messageEND = 'Your fleet of trucks is listed below (number,spec):'
print(messageEND)
log(messageEND)
print(fleet)
log(fleet)

#print(logs)

df = pd.DataFrame(logs, columns= ['time', 'message'])
df.to_csv(dt.now().strftime('%Y%m%d%H%M%S')+'.csv',index=False,quoting=csv.QUOTE_NONNUMERIC)