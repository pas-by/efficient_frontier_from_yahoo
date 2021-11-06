#!/usr/bin/env python
# -*- coding: utf-8 -*-

#   File Name   : mergeTables.py
#   description :
#
#         begin : 2021-11-06
# last modified : 2021-11-06

import csv
import pandas as pd
import yfin_test001
import numpy as np
import yfin_test001

def getPriceTable(sourceDir, code):
	#  fetch the price of a stock (last yrear, monthly)
	data = pd.read_csv(sourceDir + code);
	return data;

def computeLogReuturn(code, priceTable):
    # assign the numpy log function to a new function called ln
    ln = np.log

    adjusted_prices = priceTable["Close"];
    t0 = ln(adjusted_prices);
    t1 = ln(adjusted_prices);

    # remove the 1'st row
    t1 = t1.drop(t1.index[0], axis=0);

    # remove the last row
    t0 = t0.drop(t0.index[t0.index.size - 1], axis=0);

    # to compute the 'Log Return'
    logReturn = t1.to_numpy() - t0.to_numpy();

    # convert a NumPy array to a Pandas series
    logReturn = pd.Series(logReturn);
    logReturn = logReturn.rename(code);

    return logReturn;

sourceDir = './out';
sourceDir += '/';

file = open(sourceDir + "myList002.txt");  #  list of code name
csvreader = csv.reader(file);

stocks = []
for row in csvreader:
    stocks.append(row[0])

"""
#  碼農的測試碼
for x in stocks:
	print(getPriceTable(sourceDir, x));

print(computeLogReuturn(stocks[0], getPriceTable(sourceDir, stocks[0])));
"""
#  create an Empty DataFrame object
returnMatrix = pd.DataFrame()

for x in stocks:
    returnMatrix = pd.concat([returnMatrix, computeLogReuturn(x, getPriceTable(sourceDir, x))], axis=1);

#  碼農的測試碼
#  returnMatrix.to_excel('test.xlsx');

pd.set_option("display.max_rows", None);

# annual return
#  print(returnMatrix.sum());

yfin_test001.efficientFrontier(returnMatrix)
