# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 13:20:34 2019

@author: david
"""
from spellchecker import SpellChecker

spell = SpellChecker(language=None,distance = 3)
spell.word_frequency.load_text_file('./brands_edited2.txt')


# find those words that may be misspelled
misspelled = spell.unknown(['manc'])

for word in misspelled:
    print(word,spell.candidates(word))


