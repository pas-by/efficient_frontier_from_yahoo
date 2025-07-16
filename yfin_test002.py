#!/usr/bin/env python
# -*- coding: utf-8 -*-

#  File Name    : yfin_test002.py
#  description  :
#        begin  : 2021-09-22
# last modified : 2025-07-16

import yfin_test001

if __name__ == "__main__":
    # 程罪員的測試碼
    stockCode = "MO";

    print(f"Stock code : {stockCode}");
    logReturn = yfin_test001.returnOfLastYear(stockCode);

    print(logReturn);
    print(f"return of last year : {logReturn.sum():.4f}");
