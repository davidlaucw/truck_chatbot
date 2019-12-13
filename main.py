# -*- coding: utf-8 -*-
"""
@author: Chun Wai (David), Lau
"""
#import numpy as np
import csv
from datetime import datetime as dt
#import sys
import pandas as pd
#import re
from spellchecker import SpellChecker

spell = SpellChecker(language=None,distance = 3)
spell.word_frequency.load_text_file('./brands_edited2.txt')

logs = []
fleet = []


def log(side, message):  # log a message with timestamp
    logs.append([dt.now().strftime('%Y-%m-%d %H:%M:%S'), side, message])


# log a question and answer pair with the option of checking if the input is a number
def qna(message, num=False, isInt=False, numRange=None, spellcheck=False):
    value = input(message)
    log('bot', message)
    log('user', value)
    if num is True:
        return isNumberMsg(value, isInt=isInt, numRange=numRange)
    elif spellcheck is True:
        return spellchecking(value)
    else:
        return value


def msg(message):  # log and print the bot message
    print(message)
    log('bot', message)


def isNumberMsg(value, isInt=False, numRange=None):  # check if the input is a number or integer
    try:
        value = float(value)
    except ValueError:
        return qna('Please enter a number: ', num=True, isInt=isInt, numRange=numRange)
    if isInt:
        if numRange is None:
            if int(value)-value == 0 and int(value) > 0:
                return int(value)
            else:
                return qna('Please enter an integer > 0: ', num=True, isInt=isInt, numRange=numRange)
        else:
            if int(value)-value == 0 and value >= numRange[0] and value <= numRange[1]:
                return value
            else:
                return qna('Please enter an integer between {} and {}: '.format(numRange[0], numRange[1]), num=True, isInt=isInt, numRange=numRange)
    else:
        if numRange is None:
            return value
        
        else:
            if value >= numRange[0] and value <= numRange[1]:
                return value
            else:
                return qna('Please enter a number between {} and {}: '.format(numRange[0], numRange[1]), num=True, isInt=isInt, numRange=numRange)


def spellchecking(word):
    if len(spell.unknown([word])) == 0:
        return word
    else:
        word = qna('For {}, do you mean {}? Please retype only the brand name: '.format(word,spell.candidates(word)))
        word = [x.strip() for x in word.split(',')]
        if len(word) == 2:
            return word[1]
        else:
            return word

name = qna("Hello. What is your name? ")
companyName = qna("Hi {}, what is the name of your company? ".format(name))
while True:
    haveTruck = qna('Do you own trucks (y/n)? ')
    if haveTruck.lower() == 'y':
        brands = qna('What brands are they? (Please separate them with commas.) ')
        brands = [x.strip() for x in brands.split(',')]
        for brand in brands:
            brand =  spellchecking(brand)
            numModels = qna('How many {}\'s models are there? '.format(brand), num=True, isInt=True)
            for i in range(numModels):
                truck = [brand]
                truck.append(qna('What is the model {}? '.format(i+1)))
                truck.append(qna('What is the engine size in liter? ', num=True))
                truck.append(qna('How many axles do each of them have? ', num=True, isInt=True, numRange=[2,10]))
                truck.append(qna('What is the weight of each of them in kg? ', num=True, numRange=[10000,60000]))
                truck.append(qna('What is the maximum load of each of them in kg? ', num=True, numRange=[10000,60000]))
                truck.append(qna('How many such trucks do you have? ', num=True, isInt=True))
                fleet.append(truck)
            
        msg('Thank you, {}! {}\'s fleet of trucks is listed below:'.format(name, companyName))
        msg('(brand, model name, engine size, num of axle, weight, max load, num of trucks)')
        msg(fleet)
        break

    elif haveTruck.lower() == 'n':
        msg('Thank you, {}. Good bye.'.format(name))
        break

    else:
        msg('Please enter "y" or "n" only.')

df = pd.DataFrame(logs, columns=['time', 'side', 'message'])
df.to_csv(dt.now().strftime('%Y%m%d%H%M%S')+'.csv', index=False, quoting=csv.QUOTE_NONNUMERIC)
