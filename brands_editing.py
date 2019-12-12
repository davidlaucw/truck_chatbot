# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 13:40:17 2019

@author: david
"""

import re
f = open("brands.txt", "r", encoding="utf-8")
fe = open("brands_edited.txt", "a", encoding="utf-8")
for line in f:
  fe.write(re.sub(' \(.*?\)', '', line))
f.close()
fe.close()


lines_seen = set() # holds lines already seen
outfile = open("brands_edited2.txt", "w", encoding="utf-8")
for line in open("brands_edited.txt", "r", encoding="utf-8"):
    if line not in lines_seen: # not a duplicate
        outfile.write(line)
        lines_seen.add(line)
outfile.close()