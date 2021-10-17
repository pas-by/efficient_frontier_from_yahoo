#!/usr/bin/env python
# -*- coding: utf-8 -*-

#   File Name   : getMyCoins.py
#   description :
#
#         begin : 2021-09-24
# last modified : 2021-09-24

import csv
import pandas as pd
import yfin_test001

file = open("myCryptoList003.txt")
csvreader = csv.reader(file)

myCoins = []
for row in csvreader:
    myCoins.append(row[0])

# 程罪員的測試碼
print(myCoins)

# create an Empty DataFrame object
returnMatrix = pd.DataFrame()

for code in myCoins:
    returnMatrix = pd.concat(
        [returnMatrix, yfin_test001.returnOfLastYear(code)], axis=1
    )

# 程罪員的測試碼
# print(returnMatrix);

yfin_test001.efficientFrontier(returnMatrix)
