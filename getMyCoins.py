#!/usr/bin/env python
# -*- coding: utf-8 -*-

#   File Name   : getMyCoins.py
#   description :
#
#         begin : 2021-09-24
# last modified : 2023-08-05

import csv
import pandas as pd
import yfin_test001

file = open("stocks_2024.txt")
#  file = open("myCryptoList003.txt")
#  file = open("my_hk_stocks.txt")
#  file = open("my_hk_stocks_01.txt")

csvreader = csv.reader(file)

myCoins = []
for row in csvreader:
    myCoins.append(row[0])

# 程罪員的測試碼
print(myCoins)

# create an Empty DataFrame object
returnMatrix = pd.DataFrame()

for code in myCoins:
    print(code)
    retLastYr = yfin_test001.returnOfLastYear(code)
    print(len(retLastYr.index))

    if(len(retLastYr.index)>1):
        returnMatrix = (pd.concat([returnMatrix, retLastYr], axis=1))

# 程罪員的測試碼
print(returnMatrix);

yfin_test001.efficientFrontier(returnMatrix)
