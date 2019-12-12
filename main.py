#import numpy as np
import csv
from datetime import datetime as dt
import sys
import pandas as pd
#import re

logs = []
fleet = []
def log(side, message):
    logs.append([dt.now().strftime('%Y-%m-%d %H:%M:%S'), side, message])

def qna(message, num=False, isInt=False):
    value = input(message)
    log('bot', message)
    log('user', value)
    if num is False:
        return value
    else:
        return isNumberMsg(value, isInt=isInt)

def msg(message):
    print(message)
    log('bot', message)
    
def isNumberMsg(value, isInt=False):
    try:
        value = float(value)
    except ValueError:
        return qna('Please enter a number: ', num=True, isInt=isInt)
    if isInt:
        if int(value)-value == 0 and int(value) > 0:
            return int(value)
        else:
            return qna('Please enter an integer > 0: ', num=True, isInt=isInt)
    else:
        return value

name = qna("Hello. What is your name? ")
companyName = qna("Hi {}, what is the name of your company? ".format(name))
while True:
    haveTruck = qna('Do you own trucks (y/n)? ')
    if haveTruck.lower() == 'y':
        #numTruck = qna('How many trucks do you have? ',num=True,isInt=True)
        brands = qna('What brands are they? (Please separate them with comma without spaces.) ')
        brands = brands.split(",")
        for brand in brands:
            #trucksInSameBrand = qna('How many {} trucks do you have? '.format(brand),num=True,isInt=True)
            numModels = qna('How many {}\'s models are there? '.format(brand), num=True, isInt=True)
            model = []
            for i in range(numModels):
                model.append(qna('What is the model {}? '.format(i+1)))
                model.append(qna('What is the engine size in liter? ', num=True))
                model.append(qna('How many axles do each of them have? ', num=True, isInt=True))
                model.append(qna('What is the weight of each of them in kg? ', num=True))
                model.append(qna('What is the maximum load of each of them in kg? ', num=True))
                model.append(qna('How many such trucks do you have? ', num=True, isInt=True))
                fleet.append([brand, model])
        break

    elif haveTruck.lower() == 'n':
        msg('Thank you, {}. Good bye.'.format(name))
        df = pd.DataFrame(logs, columns=['time', 'side', 'message'])
        df.to_csv(dt.now().strftime('%Y%m%d%H%M%S')+'.csv', index=False, quoting=csv.QUOTE_NONNUMERIC)
        sys.exit()

    else:
        msg('Please enter "y" or "n" only.')

msg('Thank you, {}! {}\'s fleet of trucks is listed below (brand,[model name, engine size, axle number, weight, max load, numbers]):'.format(name, companyName))
msg(fleet)

df = pd.DataFrame(logs, columns=['time', 'side', 'message'])
df.to_csv(dt.now().strftime('%Y%m%d%H%M%S')+'.csv', index=False, quoting=csv.QUOTE_NONNUMERIC)


# def isNumber(s):
#     try:
#         float(s)
#         return float(s)
#     except:
#         return None

# def isNumberMsg(value, isInt=False):
#     if isInt:
#         try:
#             int(value)
#             if value > 0:
#                 return int(value)
#             else:
#                 return int(qna('Please enter an integer > 0: ', num=True, isInt=isInt))
#         except:
#             print(value,type(value))
#             return int(qna('Please enter an integer > 0 (NaN): ', num=True, isInt=isInt))
#     else:
#         try:
#             float(value)
#             return float(value)
#         except:
#             return float(qna('Please enter a number. ', num=True))
