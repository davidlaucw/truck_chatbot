#import numpy as np
import pandas as pd
import csv
from datetime import datetime as dt
import re

logs = []
fleet=[]
def log(message):
    logs.append([dt.now().strftime('%Y-%m-%d %H:%M:%S'),message])
def start():
    message = "Hello. I am your truck chatbox."
    print(message)
    log(message)
def isNumber(s):
    try:
        float(s)
        return float(s)
    except:
        return None

start()
i = 0
while True:
    messageNewTruck = 'Do you want to add the truck {} in your fleet? (y/n)'.format(i+1)
    newTruck = input(messageNewTruck)
    log(messageNewTruck)
    log(newTruck)
    if newTruck == 'y':
        messageAxle = 'What is the axle configuration? (nxn)'
        axle = input(messageAxle)
        log(messageAxle)
        log(axle)
        while (re.match('^[468]x[24]$',axle) or re.match('^10x[24]$',axle)) is None:
            messageNxN = 'Please enter the correct axle configuration.'
            axle = input(messageNxN)
            log(messageNxN)
            log(axle)
            
        messageWeight = 'What is the net weight of the truck in kg?'
        weight = input(messageWeight)
        log(messageWeight)
        log(weight)
        weight = isNumber(weight)
        while weight is None:
            messageNumberWeight = 'Please enter a number for the weight in kg.'
            weight = input(messageNumberWeight)
            log(messageNumberWeight)
            log(weight)
            weight = isNumber(weight)
        
        messageLoad = 'What is the load of the truck in kg?'
        load = input(messageLoad)
        log(messageLoad)
        log(load)
        load = isNumber(load)
        while load is None:
            messageNumberLoad = 'Please enter a number for the load in kg.'
            weight = input(messageNumberLoad)
            log(messageNumberLoad)
            log(load)
            load = isNumber(load)    
        fleet.append([i+1,axle,weight,load])
        i+=1
    elif newTruck == 'n':
        break
    else:
        messageyorn = 'Please enter y or n.'
        print(messageyorn)
        log(messageyorn)
        
messageEND = 'Your fleet of trucks is listed below (number,axle configuration,weight,load):'
print(messageEND)
log(messageEND)
print(fleet)
log(fleet)

#print(logs)

df = pd.DataFrame(logs, columns= ['time', 'message'])
df.to_csv(dt.now().strftime('%Y%m%d%H%M%S')+'.csv',index=False,quoting=csv.QUOTE_NONNUMERIC)