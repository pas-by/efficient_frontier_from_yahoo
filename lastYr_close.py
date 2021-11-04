#!/usr/bin/env python
# -*- coding: utf-8 -*-

#   File Name   : lastYr_close.py
#   description :
#
#         begin : 2021-11-04
# last modified : 2021-11-04

import pandas as pd
import yfin_test001

myStockList = ['0001.HK', '0002.HK'];

for code in myStockList:
    print(code)
    closeLastYr = yfin_test001.closePriceOfLastYear(code)
    print(len(closeLastYr.index))
    print(closeLastYr)

    #  write to csv file
    closeLastYr.to_csv(code);

