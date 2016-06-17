# -*- coding: utf-8 -*-
"""
csv-reader
@author: Aramayis
"""

import csv

def num_datapoints(filename):
    """ Reads csv file and returns number of lines in file, where each line
    represents data for a different timestamp.
    
    Keyword arguments:
    filename -- file path for the data e.g. Data/apple_stocks.csv
    
    """
    num = 0
    with open(filename, newline='') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in csvreader:
            num += 1
    return num - 1      
