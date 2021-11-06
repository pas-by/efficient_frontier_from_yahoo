#!/usr/bin/env python
# -*- coding: utf-8 -*-

#   File Name   : lastYr_close.py
#   description :
#
#         begin : 2021-11-04
# last modified : 2021-11-04

import pandas as pd
import yfin_test001

#  碼農的測試碼
myStockList = ['0001.HK', '0002.HK'];

stockDF =  pd.read_csv('filter_result_20211103.csv');
myStockList = stockDF['a'].values.tolist();

for code in myStockList:
    print(code)
    try:
        closeLastYr = yfin_test001.closePriceOfLastYear(code)
        print(len(closeLastYr.index))
        print(closeLastYr)

        #  write to csv file
        closeLastYr.to_csv('./temp/' + code);
    except:
        pass;


for code in myStockList:
    try:
        closeLastYr = pd.read_csv('./temp/' + code);
        print(closeLastYr);
    except:
        pass;

#  碼農的測試碼
print(stockDF);
