#!/usr/bin/env python
# -*- coding: utf-8 -*-

#   File Name   : getHSI.py
#   description : 列出恆生指數成份股。
#                 產生過去十二月的 'matrix of return'。
#
#         begin : 2021-09-20
# last modified : 2021-09-22

import pandas as pd
import yfin_test001

a = pd.read_excel("suggest elements on 2021-10-23.xlsx")
# print(a)

# print column names
print(a.columns)

# note : a space found at the end!!!
codes = a["Code "]
# print(codes)

#  create an empty list
constituents = []

# to iterate over rows
for index, row in a.iterrows():
    co = "{:0>4}.HK".format(row["Code "])

    # 程罪員的測試碼
    # print(co)

    constituents.append(co)

# 程罪員的測試碼
print(constituents)

# create an Empty DataFrame object
returnMatrix = pd.DataFrame()

for code in constituents:
    returnMatrix = pd.concat(
        [returnMatrix, yfin_test001.returnOfLastYear(code)], axis=1
    )

# 程罪員的測試碼
# print(returnMatrix);

yfin_test001.efficientFrontier(returnMatrix)
