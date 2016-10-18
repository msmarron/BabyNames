# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 08:52:21 2015

@author: matthewbrown
"""

import os
import csv

path = "C:\\Users\\matthewbrown\\Documents\\Personal Stuff\\Baby Names\\names\\"
filenames = os.listdir(path)

filenames.sort(None,None,True)

Names = [["Name", "Sex","Occurence","Year","Rank"]]

for filename in filenames:
    occurance = 5000000
    rank = 0
    if filename[0] == 'y':
        with open(path + filename, "r") as csvfile:
            namereader = csv.reader(csvfile)
            for row in namereader:
                    if row[1] == 'F':
                        if int(row[2]) != occurance:
                            rank += 1
                        row.append(filename[3:7:1])
                        row.append(rank)
                        Names.append(row)
                        occurance = int(row[2])


with open(path + "Compiled Names.csv", "w") as csvfile:
    namewriter = csv.writer(csvfile)
    namewriter.writerows(Names)
    